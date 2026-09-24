import sys
import os
sys.path.insert(0, os.getcwd())
try:
    from services.cv_segmentation import segment_sticker_sheet
    from services.sticker_analyzer import generate_sticker_metadata, semantic_search_stickers
except ImportError:
    segment_sticker_sheet = None
    generate_sticker_metadata = None
    semantic_search_stickers = None
import base64
import os
import json
import uuid
import datetime
import random
from functools import lru_cache
from flask import Flask, render_template, request, jsonify, redirect, url_for, Response, send_from_directory
from config import Config, DATA_DIR

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static'),
    static_url_path='/static'
)
app.config.from_object(Config)


@app.before_request
def redirect_legacy_vercel_domain():
    """Consolidate the public Vercel alias into the canonical domain."""
    if request.host.split(':', 1)[0].lower() == 'memourscrapbook.vercel.app':
        canonical_url = f"{app.config['SITE_URL']}{request.full_path}"
        if canonical_url.endswith('?'):
            canonical_url = canonical_url[:-1]
        return redirect(canonical_url, code=308)

# Data loader helpers
def load_json_data(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_json_data(filename, data):
    try:
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Notice: Storage read-only on serverless ({e})")

@lru_cache(maxsize=1)
def get_products():
    return load_json_data('products.json')

@lru_cache(maxsize=1)
def get_inspirations():
    return load_json_data('inspirations.json')

@lru_cache(maxsize=1)
def get_blogs():
    blogs = load_json_data('blogs.json') + load_json_data('guides_extra.json')
    content_dir = os.path.join(DATA_DIR, 'guide_content')
    for blog in blogs:
        blog.setdefault('url', f"/guide/{blog['slug']}")
        blog.setdefault('thumbnail', blog.get('cover_image'))
        blog.setdefault('is_featured', False)
        content_file = blog.get('content_file')
        if content_file:
            # Article filenames are maintained in project data, never taken from a URL.
            filename = os.path.basename(content_file)
            with open(os.path.join(content_dir, filename), 'r', encoding='utf-8') as article:
                blog['content'] = article.read()
    return sorted(blogs, key=lambda blog: blog.get('published_date', ''), reverse=True)

@lru_cache(maxsize=1)
@lru_cache(maxsize=1)
def get_company_info():
    return load_json_data('company_info.json')

def get_orders():
    return load_json_data('orders.json')

# Context Processor for Global template variables (e.g. Company info)
@app.context_processor
def inject_global_data():
    return {
        'company': get_company_info(),
        'current_year': datetime.datetime.now().year,
        'site_url': app.config['SITE_URL']
    }

@app.template_filter('format_vnd')
def format_vnd_filter(amount):
    try:
        val = int(amount)
        return f"{val:,}".replace(",", ".") + " đ"
    except (ValueError, TypeError):
        return f"{amount} đ"

# ----------------- SEO & SEARCH ENGINE CRAWLER ROUTES -----------------

@app.route('/favicon.ico')
def favicon():
    response = send_from_directory(app.static_folder, 'assets/favicon.ico', mimetype='image/vnd.microsoft.icon')
    response.headers['Cache-Control'] = 'public, max-age=604800, immutable'
    return response

@app.route('/robots.txt')
def robots_txt():
    base_url = app.config['SITE_URL']
    content = f"""User-agent: *
Allow: /
Disallow: /api/
Disallow: /checkout
Disallow: /order-success

User-agent: OAI-SearchBot
Allow: /
Disallow: /api/
Disallow: /checkout
Disallow: /order-success

Sitemap: {base_url}/sitemap.xml
"""
    return Response(content, mimetype='text/plain')

@app.route('/google6aHy4Rw-px9tN5fK78Ghss2zoohlbM6Mw0Cfrxb4KSU.html')
def google_verify():
    return "google-site-verification: google6aHy4Rw-px9tN5fK78Ghss2zoohlbM6Mw0Cfrxb4KSU.html"

@app.route('/google240b89cf199dd5f7.html')
def google_verify_new():
    return "google-site-verification: google240b89cf199dd5f7.html"

@app.route('/sitemap.xml')
def sitemap_xml():
    products = get_products()
    blogs = get_blogs()
    base_url = app.config['SITE_URL']
    
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    # Static main pages
    routes = [
        ('/', '1.0', 'daily'),
        ('/about', '0.8', 'weekly'),
        ('/products', '0.9', 'daily'),
        ('/studio', '0.9', 'weekly'),
        ('/inspiration', '0.8', 'weekly'),
        ('/guide', '0.8', 'daily'),
        ('/contact', '0.7', 'monthly'),
        ('/cart', '0.6', 'monthly'),
    ]
    now = datetime.date.today().isoformat()
    for route, priority, freq in routes:
        xml.append(f"""  <url>
    <loc>{base_url}{route}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

    # Dynamic Products
    for p in products:
        sku = p.get('sku')
        if sku:
            xml.append(f"""  <url>
    <loc>{base_url}/product/{sku}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    # Dynamic Guides / Blogs
    for b in blogs:
        slug = b.get('slug')
        if slug:
            lastmod = b.get('updated_date') or b.get('published_date') or now
            xml.append(f"""  <url>
    <loc>{base_url}/guide/{slug}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")
            
    xml.append('</urlset>')
    return Response('\n'.join(xml), mimetype='application/xml')

# ----------------- PAGE ROUTES -----------------

@app.route('/')
@app.route('/api/index')
@app.route('/api/index.py')
def index():
    products = get_products()
    inspirations = get_inspirations()
    blogs = get_blogs()
    company = get_company_info()
    
    featured_stickers = [p for p in products if p['category'] == 'sticker'][:3]
    featured_layouts = [p for p in products if p['category'] == 'layout'][:3]
    featured_books = [p for p in products if p['category'] == 'book'][:3]
    
    return render_template(
        'index.html',
        featured_stickers=featured_stickers,
        featured_layouts=featured_layouts,
        featured_books=featured_books,
        inspirations=inspirations[:4],
        blogs=blogs[:3],
        company=company
    )

@app.route('/about')
def about():
    company = get_company_info()
    return render_template('about.html', company=company)

@app.route('/products')
def products():
    all_products = get_products()
    category = request.args.get('category', 'all')
    theme = request.args.get('theme', 'all')
    style = request.args.get('style', 'all')
    is_3d_param = request.args.get('is_3d', 'all')
    sort_by = request.args.get('sort', 'default')
    search_q = request.args.get('q', '').strip().lower()
    
    filtered = all_products
    if category != 'all':
        filtered = [p for p in filtered if p['category'] == category or p.get('type') == category]
        
    if theme != 'all':
        filtered = [p for p in filtered if any(theme.lower() in t.lower() for t in p.get('themes', [])) or theme.lower() in p.get('attributes', {}).get('theme', '').lower()]
        
    if style != 'all':
        filtered = [p for p in filtered if style.lower() in p.get('style', '').lower()]

    if is_3d_param == 'true':
        filtered = [p for p in filtered if p.get('is_3d') is True]
    elif is_3d_param == 'false':
        filtered = [p for p in filtered if p.get('is_3d') is False]
        
    if search_q:
        filtered = [
            p for p in filtered if (
                search_q in p['name'].lower() or
                search_q in p['sku'].lower() or
                search_q in p.get('id', '').lower() or
                search_q in p['description'].lower() or
                any(search_q in tag.lower() for tag in p.get('tags', [])) or
                any(search_q in tag.lower() for tag in p.get('ai_keywords', []))
            )
        ]

    if sort_by == 'price_asc':
        filtered.sort(key=lambda x: x.get('price', 0))
    elif sort_by == 'price_desc':
        filtered.sort(key=lambda x: x.get('price', 0), reverse=True)
    elif sort_by == 'name_asc':
        filtered.sort(key=lambda x: x.get('name', ''))
        
    categories_stat = {
        'all': len(all_products),
        'sticker': len([p for p in all_products if p['category'] == 'sticker' or p.get('type') == 'sticker']),
        'layout': len([p for p in all_products if p['category'] == 'layout' or p.get('type') == 'layout']),
        'scrapbook': len([p for p in all_products if p['category'] == 'scrapbook' or p.get('type') == 'scrapbook' or p.get('category') == 'book']),
    }
    
    return render_template(
        'products.html',
        products=filtered,
        selected_category=category,
        selected_theme=theme,
        selected_style=style,
        selected_3d=is_3d_param,
        selected_sort=sort_by,
        search_q=search_q,
        categories_stat=categories_stat
    )

@app.route('/product/<id_or_sku>')
def product_detail(id_or_sku):
    all_products = get_products()
    target = None
    for p in all_products:
        if p['id'].lower() == id_or_sku.lower() or p['sku'].lower() == id_or_sku.lower():
            target = p
            break
            
    if not target:
        return redirect(url_for('products'))
        
    related = [p for p in all_products if p['category'] == target['category'] and p['sku'] != target['sku']][:3]
    return render_template('product_detail.html', product=target, related_products=related)

@app.route('/inspiration')
@app.route('/inspirations')
def inspirations():
    all_inspirations = get_inspirations()
    products = get_products()
    product_map = {p['sku']: p for p in products}
    
    return render_template(
        'inspirations.html',
        inspirations=all_inspirations,
        product_map=product_map
    )

@app.route('/inspiration/<insp_id>')
@app.route('/inspirations/<insp_id>')
def inspiration_detail(insp_id):
    return redirect(url_for('studio', remix=insp_id))

@app.route('/guide')
@app.route('/handbook')
def handbook():
    all_blogs = get_blogs()
    available_tags = sorted({tag for blog in all_blogs for tag in blog.get('tags', [])})
    tag = request.args.get('tag', 'all')
    search_q = request.args.get('q', '').strip().lower()
    
    filtered_blogs = all_blogs
    if tag != 'all':
        filtered_blogs = [b for b in filtered_blogs if tag.lower() in [t.lower() for t in b.get('tags', [])]]
        
    if search_q:
        filtered_blogs = [
            b for b in filtered_blogs if (
                search_q in b.get('title', '').lower() or
                search_q in b.get('excerpt', '').lower() or
                search_q in b.get('keywords', '').lower()
            )
        ]
        
    return render_template(
        'handbook.html',
        blogs=filtered_blogs,
        selected_tag=tag,
        search_q=search_q,
        available_tags=available_tags
    )

@app.route('/mau-luu-but-dep')
@app.route('/guide/mau-luu-but-dep')
def article_mau_luu_but_dep():
    all_blogs = get_blogs()
    related_blogs = [b for b in all_blogs if b.get('slug') != 'mau-luu-but-dep'][:3]
    return render_template('article_mau_luu_but.html', related_blogs=related_blogs)

@app.route('/guide/<slug>')
@app.route('/handbook/<slug>')
def handbook_detail(slug):
    if slug == 'mau-luu-but-dep':
        return redirect(url_for('article_mau_luu_but_dep'))
        
    all_blogs = get_blogs()
    target_blog = next((b for b in all_blogs if b['slug'] == slug or b['id'] == slug), None)
    if not target_blog:
        return redirect(url_for('handbook'))
        
    all_products = get_products()
    related_products = [p for p in all_products if p['sku'] in target_blog.get('related_skus', [])]
    target_tags = {tag.lower() for tag in target_blog.get('tags', [])}
    related_blogs = sorted(
        (b for b in all_blogs if b.get('slug') != slug),
        key=lambda b: len(target_tags & {tag.lower() for tag in b.get('tags', [])}),
        reverse=True
    )[:3]
    
    return render_template(
        'handbook_detail.html',
        blog=target_blog,
        related_products=related_products,
        related_blogs=related_blogs
    )


@app.route('/contact')
def contact():
    company = get_company_info()
    return render_template('contact.html', company=company)

@app.route('/studio')
def studio():
    products = get_products()
    inspirations = get_inspirations()
    preset_id = request.args.get('remix', '')
    target_sku = request.args.get('sku', '')
    
    stickers = [p for p in products if p.get('category') == 'sticker']
    layouts = [p for p in products if p.get('category') == 'layout']
    books = [p for p in products if p.get('category') in ('scrapbook', 'book')]
    patterns = [p for p in products if p.get('category') in ('pattern', 'paper')]
    
    active_preset = None
    if preset_id:
        active_preset = next((insp for insp in inspirations if insp['id'] == preset_id), None)
        
    active_product = None
    if target_sku:
        active_product = next((p for p in products if p['sku'].lower() == target_sku.lower() or p['id'].lower() == target_sku.lower()), None)
        
    return render_template(
        'studio.html',
        products=products,
        stickers=stickers,
        layouts=layouts,
        books=books,
        patterns=patterns,
        inspirations=inspirations,
        active_preset=active_preset,
        active_product=active_product
    )

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/order-tracking')
@app.route('/orders')
def order_tracking():
    order_code = request.args.get('code', '').strip()
    return render_template('order_tracking.html', initial_code=order_code)

# ----------------- API ENDPOINTS -----------------

@app.route('/api/products')
def api_products():
    return jsonify(get_products())

@app.route('/api/inspirations')
def api_inspirations():
    return jsonify(get_inspirations())

@app.route('/api/blogs')
@app.route('/api/handbook')
def api_blogs():
    return jsonify(get_blogs())

def call_gemini_ai_layout(prompt, products):
    """
    Direct HTTPS Client to Google Gemini Pro / Flash API
    Integrated with User's Gemini Pro Key and MEMOUR Product Catalog
    """
    api_key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    if not api_key:
        return None
        
    import urllib.request
    import urllib.error
    import json
    
    # Try Gemini Pro, Gemini 1.5 Pro, Gemini 2.5 Flash, Gemini Flash endpoints
    endpoint_urls = [
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={api_key}",
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}",
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={api_key}",
        f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={api_key}",
        f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}",
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}",
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    ]
    
    products_summary = [
        {
            "sku": p.get('sku'),
            "category": p.get('category', p.get('type', '')),
            "name": p.get('name'),
            "tags": p.get('tags', []),
            "style": p.get('style', ''),
            "emotion": p.get('emotion', '')
        }
        for p in products
    ]
    
    sys_instruction = (
        "You are MEMOUR AI Specialist for MEMOUR Studio (Brand identity: 'Memory' + 'Our', Slogan: 'Every memory has a story'). "
        "Analyze the user's prompt (mood, memories, themes, occasions) and choose the best matching items from the available products catalog: "
        "exactly 1 Scrapbook book (SCR-xxx), 2 Layouts (LAY-xxx), and 4 Stickers (STK-xxx). "
        "Return ONLY a pure valid JSON object (no markdown, no backticks) with keys: "
        "\"book_sku\": string, \"layout_skus\": [string, string], \"sticker_skus\": [string, string, string, string], "
        "\"ai_reasoning\": string (in inspiring Vietnamese connecting the memories with MEMOUR's philosophy: 'Every memory has a story'), "
        "\"bg_theme\": string (hex color code for paper canvas, e.g. #e8d8c3 for kraft, #f3e8ff for pastel, #18181b for black, #fdfbf7 for cream)."
    )
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"{sys_instruction}\n\nAvailable Products Catalog:\n{json.dumps(products_summary, ensure_ascii=False)}\n\nUser Prompt: {prompt}"}
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.3,
            "responseMimeType": "application/json"
        }
    }
    
    for url in endpoint_urls:
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                candidates = res_data.get('candidates', [])
                if candidates:
                    raw_text = candidates[0]['content']['parts'][0]['text'].strip()
                    if raw_text.startswith('```json'):
                        raw_text = raw_text[7:]
                    if raw_text.startswith('```'):
                        raw_text = raw_text[3:]
                    if raw_text.endswith('```'):
                        raw_text = raw_text[:-3]
                    return json.loads(raw_text.strip())
        except Exception as e:
            continue
            
    return None

@app.route('/api/ai-suggest', methods=['POST'])
def api_ai_suggest():
    """
    AI Recommendation & Layout Auto-Arranger:
    Powered by MEMOUR Google Gemini Pro with real-time semantic fallback engine.
    """
    data = request.get_json() or {}
    prompt = data.get('prompt', '').strip()
    mood = data.get('mood', 'auto').lower()
    
    products = get_products()
    product_by_sku = {p['sku']: p for p in products}
    
    # 1. Attempt Gemini Pro AI Call
    gemini_res = call_gemini_ai_layout(prompt, products) if prompt else None
    
    selected_book = None
    selected_layouts = []
    selected_stickers = []
    ai_reasoning = ""
    bg_theme = "#fdfbf7"
    
    if gemini_res and isinstance(gemini_res, dict):
        book_sku = gemini_res.get('book_sku', '')
        selected_book = product_by_sku.get(book_sku)
        
        for l_sku in gemini_res.get('layout_skus', []):
            if l_sku in product_by_sku and len(selected_layouts) < 2:
                selected_layouts.append(product_by_sku[l_sku])
                
        for s_sku in gemini_res.get('sticker_skus', []):
            if s_sku in product_by_sku and len(selected_stickers) < 4:
                selected_stickers.append(product_by_sku[s_sku])
                
        ai_reasoning = f"[MEMOUR Gemini Pro AI] {gemini_res.get('ai_reasoning', '')}"
        bg_theme = gemini_res.get('bg_theme', '#e8d8c3')

    # 2. Semantic Fallback Engine if Gemini response incomplete
    if not selected_book or len(selected_layouts) < 2 or len(selected_stickers) < 4:
        keywords = [w for w in prompt.lower().replace(',', ' ').replace('.', ' ').replace('?', ' ').split() if len(w) > 1]
        
        scored_stickers = []
        scored_layouts = []
        scored_books = []
        
        for p in products:
            score = 0
            ai_tags = [t.lower() for t in (p.get('tuKhoa', []) + p.get('tuKhoaLienQuan', []) + p.get('tags', []) + p.get('ai_keywords', []))]
            themes = [t.lower() for t in (p.get('chuDe', []) + p.get('themes', []))]
            style = ((p.get('phongCach', '') if isinstance(p.get('phongCach'), str) else " ".join(p.get('phongCach', []))) + " " + p.get('style', '')).lower()
            occasion = ((p.get('dipSuDung', '') if isinstance(p.get('dipSuDung'), str) else " ".join(p.get('dipSuDung', []))) + " " + p.get('occasion', '')).lower()
            emotion = ((p.get('camXuc', '') if isinstance(p.get('camXuc'), str) else " ".join(p.get('camXuc', []))) + " " + p.get('emotion', '')).lower()
            colors = [c.lower() for c in (p.get('mauSac', []) + p.get('colors', []))]
            desc = ((p.get('moTa', '') or '') + " " + (p.get('description', '') or '')).lower()
            name = ((p.get('ten', '') or '') + " " + (p.get('name', '') or '')).lower()
            
            for kw in keywords:
                if kw in ai_tags:
                    score += 6
                if any(kw in th for th in themes) or kw in occasion:
                    score += 5
                if kw in style or kw in emotion:
                    score += 4
                if kw in name:
                    score += 3
                if any(kw in c for c in colors) or kw in desc:
                    score += 2
                    
            p_category = p.get('category', p.get('type', ''))
            if p_category == 'sticker':
                scored_stickers.append((score, p))
            elif p_category == 'layout':
                scored_layouts.append((score, p))
            elif p_category in ['book', 'scrapbook']:
                scored_books.append((score, p))
                
        scored_stickers.sort(key=lambda x: x[0], reverse=True)
        scored_layouts.sort(key=lambda x: x[0], reverse=True)
        scored_books.sort(key=lambda x: x[0], reverse=True)
        
        if not selected_book:
            selected_book = scored_books[0][1] if scored_books else [p for p in products if p.get('type') in ('scrapbook', 'book')][0]
        if len(selected_layouts) < 2:
            selected_layouts = [item[1] for item in scored_layouts[:2]] if scored_layouts else [p for p in products if p.get('type') == 'layout'][:2]
        if len(selected_stickers) < 7:
            selected_stickers = [item[1] for item in scored_stickers[:7]] if scored_stickers else [p for p in products if p.get('type') == 'sticker'][:7]
            
        book_sku_lower = selected_book['sku'].lower()
        if '001' in book_sku_lower or 'kraft' in book_sku_lower:
            bg_theme = '#e8d8c3'
        elif '002' in book_sku_lower or 'holo' in book_sku_lower or 'pst' in book_sku_lower:
            bg_theme = '#f3e8ff'
        elif '003' in book_sku_lower or 'dark' in book_sku_lower or 'blk' in book_sku_lower:
            bg_theme = '#18181b'
        elif '004' in book_sku_lower or 'linen' in book_sku_lower:
            bg_theme = '#f5f5f4'
            
        book_theme_name = selected_book.get('theme', selected_book.get('attributes', {}).get('theme', 'Handmade Craft'))
        if not ai_reasoning:
            ai_reasoning = f"[MEMOUR AI] 'Every memory has a story' — Trợ lý AI đã phối hợp bộ linh kiện theo ý tưởng '{prompt}': Cuốn sổ {selected_book['sku']}, 2 khung ảnh nghệ thuật và {len(selected_stickers)} sticker dập nổi phân tầng cảm xúc."

    # Generate Rich, Full, Multi-Layered Scrapbook Collage (Canvas Base: 600 x 600)
    canvas_items = []
    
    # 1. Primary Polaroid Frame (Top-Center / Left)
    if len(selected_layouts) >= 1:
        canvas_items.append({
            'sku': selected_layouts[0]['sku'],
            'type': 'layout',
            'image': selected_layouts[0]['image'],
            'name': selected_layouts[0]['name'],
            'left': 220,
            'top': 225,
            'scale': 0.82,
            'angle': -4,
            'zIndex': 1
        })
        
    # 2. Secondary Polaroid Frame (Overlapping Right)
    if len(selected_layouts) >= 2:
        canvas_items.append({
            'sku': selected_layouts[1]['sku'],
            'type': 'layout',
            'image': selected_layouts[1]['image'],
            'name': selected_layouts[1]['name'],
            'left': 390,
            'top': 285,
            'scale': 0.78,
            'angle': 5,
            'zIndex': 2
        })
        
    # 3. Dynamic Curated 7 Sticker Anchors & Accents
    # Position layout coordinates around the frames for rich visual storytelling
    rich_positions = [
        {'left': 105, 'top': 95, 'angle': -14, 'scale': 0.72},   # Top-Left Header Badge
        {'left': 485, 'top': 115, 'angle': 12, 'scale': 0.75},   # Top-Right Ticket / Stamp
        {'left': 295, 'top': 75, 'angle': 2, 'scale': 0.68},     # Top-Center Washi Accent
        {'left': 95, 'top': 355, 'angle': 8, 'scale': 0.70},     # Left Mid
        {'left': 505, 'top': 345, 'angle': -10, 'scale': 0.72},  # Right Mid
        {'left': 135, 'top': 485, 'angle': -8, 'scale': 0.74},   # Bottom-Left Anchor
        {'left': 475, 'top': 490, 'angle': 14, 'scale': 0.76}    # Bottom-Right Accent
    ]
    
    for i, stk in enumerate(selected_stickers[:7]):
        pos = rich_positions[i] if i < len(rich_positions) else {'left': 300, 'top': 300, 'angle': 0, 'scale': 0.7}
        canvas_items.append({
            'sku': stk['sku'],
            'type': 'sticker',
            'image': stk['image'],
            'name': stk['name'],
            'price': stk.get('price', 2500),
            'left': pos['left'],
            'top': pos['top'],
            'scale': pos['scale'],
            'angle': pos['angle'],
            'zIndex': 10 + i
        })
        
    # 4. Handwriting Title Calligraphy Text
    title_text = "Every Memory Has A Story ✦"
    p_lower = prompt.lower()
    if any(w in p_lower for w in ['viet nam', 'di san', 'am thuc', 'non la', 'hue', 'ha noi', 'sai gon']):
        title_text = "Hành Trình Bản Sắc Việt 🇻🇳"
    elif any(w in p_lower for w in ['cam trai', 'camping', 'phuot', 'nui', 'rung', 'da ngoai']):
        title_text = "Explore & Wanderlust 🌲"
    elif any(w in p_lower for w in ['ban than', 'bestie', 'ky yeu', 'lop', 'hoc sinh', 'thanh xuan']):
        title_text = "Thanh Xuân & Bạn Thân ✨"
    elif any(w in p_lower for w in ['yeu', 'love', 'couple', 'hen ho', 'ky niem']):
        title_text = "Every Moment With You 💕"
    elif any(w in p_lower for w in ['sinh nhat', 'party', 'birthday', 'tuoi moi']):
        title_text = "Happy Birthday to Me! 🎉"
        
    canvas_items.append({
        'type': 'text',
        'text': title_text,
        'fontFamily': 'Patrick Hand',
        'fontSize': 34,
        'fill': '#78350f' if bg_theme != '#18181b' else '#fbbf24',
        'left': 300,
        'top': 540,
        'angle': -1,
        'zIndex': 30
    })
        
    return jsonify({
        'status': 'success',
        'ai_reasoning': ai_reasoning,
        'book': selected_book,
        'layouts': selected_layouts,
        'stickers': selected_stickers,
        'canvas_preset': {
            'bg_color': bg_theme,
            'items': canvas_items
        }
    })


@app.route('/api/orders', methods=['GET', 'POST'])
def api_orders():
    orders = get_orders()
    
    if request.method == 'POST':
        data = request.get_json() or {}
        order_code = 'SC-' + datetime.datetime.now().strftime('%y%m%d') + '-' + str(random.randint(1000, 9999))
        
        new_order = {
            'order_code': order_code,
            'customer_name': data.get('name', 'Khách hàng Gen Z'),
            'phone': data.get('phone', '0988888888'),
            'address': data.get('address', 'TP. Hồ Chí Minh'),
            'note': data.get('note', ''),
            'items': data.get('items', []),
            'total_amount': data.get('total_amount', 0),
            'discount_amount': data.get('discount_amount', 0),
            'final_amount': data.get('final_amount', 0),
            'status': 'Đang chuẩn bị tại Xưởng Thủ Công',
            'status_code': 'crafting',
            'created_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'timeline': [
                {'time': datetime.datetime.now().strftime('%H:%M %d/%m'), 'title': 'Tiếp nhận đơn hàng', 'desc': 'Hệ thống đã ghi nhận thiết kế và danh sách phụ kiện.'},
                {'time': (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%H:%M %d/%m'), 'title': 'Bắt đầu gia công thủ công', 'desc': 'Nghệ nhân xưởng đang dập nổi sticker và kiểm tra từng trang sổ.'}
            ]
        }
        
        orders.append(new_order)
        save_json_data('orders.json', orders)
        return jsonify({'status': 'success', 'order': new_order})
        
    # GET Search order
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({'status': 'error', 'message': 'Vui lòng nhập mã đơn hàng hoặc số điện thoại'})
        
    found = [
        o for o in orders if (
            query.lower() in o['order_code'].lower() or
            query in o['phone']
        )
    ]
    
    if found:
        return jsonify({'status': 'success', 'orders': found})
    else:
        return jsonify({'status': 'not_found', 'message': 'Không tìm thấy đơn hàng tương ứng.'})

@app.route('/api/contact-message', methods=['POST'])
def api_contact():
    data = request.get_json() or {}
    # Simulate saving contact/membership
    return jsonify({
        'status': 'success',
        'message': 'Cảm ơn bạn! Lời nhắn / Đăng ký thành viên của bạn đã được gửi thành công đến Xưởng ScrapCraft.'
    })


# ----------------- STICKER MANAGEMENT & COMPUTER VISION AI ROUTES -----------------


@app.route('/api/stickers/analyze-sheet', methods=['POST'])
def api_analyze_sticker_sheet():
    if 'sheet_image' not in request.files:
        return jsonify({'success': False, 'message': 'Không tìm thấy file ảnh tải lên'}), 400
        
    file = request.files['sheet_image']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'Vui lòng chọn file ảnh hợp lệ'}), 400

    try:
        img_bytes = file.read()
        filename_hint = file.filename.lower()
        
        # 1. Run Computer Vision Segmentation & Alpha Masking
        cv_result = segment_sticker_sheet(img_bytes, min_area_ratio=0.015)
        
        # 2. Extract AI Metadata for each detected sticker
        products = get_products()
        existing_stk_count = len([p for p in products if p.get('category') == 'sticker'])
        
        processed_stickers = []
        for idx, item in enumerate(cv_result['stickers'], start=existing_stk_count + 1):
            meta = generate_sticker_metadata(
                idx, 
                item['png_bytes'], 
                filename_context=filename_hint,
                visual_hints=filename_hint
            )
            meta['data_url'] = item['data_url']
            meta['bbox'] = item['bbox']
            meta['width'] = item['width']
            meta['height'] = item['height']
            processed_stickers.append(meta)
            
        return jsonify({
            'success': True,
            'total_detected': cv_result['total_detected'],
            'overlay_data_url': cv_result['overlay_data_url'],
            'stickers': processed_stickers
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'Lỗi Computer Vision: {str(e)}'}), 500

@app.route('/api/stickers/save-batch', methods=['POST'])
def api_save_sticker_batch():
    data = request.get_json() or {}
    stickers_to_save = data.get('stickers', [])
    if not stickers_to_save:
        return jsonify({'success': False, 'message': 'Không có dữ liệu sticker để lưu'}), 400

    try:
        os.makedirs('static/assets/stickers', exist_ok=True)
        products = get_products()
        
        saved_items = []
        for stk in stickers_to_save:
            sku = stk.get('sku') or f"STK-{len(products)+1:03d}"
            filename = f"{sku.lower().replace('-', '_')}.png"
            file_path = os.path.join('static/assets/stickers', filename)
            img_url = f"/static/assets/stickers/{filename}"
            
            # If data_url base64 is passed, save image file
            data_url = stk.get('data_url', '')
            if data_url and data_url.startswith('data:image'):
                b64_data = data_url.split(',', 1)[1]
                png_bytes = base64.b64decode(b64_data)
                with open(file_path, 'wb') as f:
                    f.write(png_bytes)
            
            stk['sku'] = sku
            stk['id'] = sku
            stk['image'] = img_url
            stk['imageUrl'] = img_url
            stk['thumbnailUrl'] = img_url
            stk['category'] = 'sticker'
            
            # Remove transient data_url to keep json database lightweight
            stk.pop('data_url', None)
            stk.pop('png_bytes', None)
            
            saved_items.append(stk)
            
        # Update products.json (Single Source of Truth)
        existing_non_stickers = [p for p in products if p.get('sku') not in [s['sku'] for s in saved_items]]
        updated_db = saved_items + existing_non_stickers
        
        with open('data/products.json', 'w', encoding='utf-8') as f:
            json.dump(updated_db, f, ensure_ascii=False, indent=2)
        get_products.cache_clear()
            
        return jsonify({
            'success': True,
            'saved_count': len(saved_items),
            'message': f'Đã lưu thành công {len(saved_items)} sticker vào cơ sở dữ liệu!'
        })
    except Exception as e:
        return jsonify({'success': False, 'message': f'Lỗi lưu sticker: {str(e)}'}), 500

@app.route('/api/stickers/ai-search', methods=['POST'])
def api_stickers_ai_search():
    data = request.get_json() or {}
    prompt = data.get('prompt', '').strip()
    if not prompt:
        return jsonify({'success': False, 'results': []})
        
    products = get_products()
    stickers = [p for p in products if p.get('category') == 'sticker']
    
    results = semantic_search_stickers(prompt, stickers, top_k=6)
    return jsonify({
        'success': True,
        'query': prompt,
        'results': results
    })

@app.route('/api/stickers', methods=['GET'])
def api_get_all_stickers():
    products = get_products()
    stickers = [p for p in products if p.get('category') == 'sticker']
    return jsonify(stickers)

@app.route('/api/stickers/<sku>', methods=['DELETE'])
def api_delete_sticker(sku):
    products = get_products()
    initial_len = len(products)
    updated = [p for p in products if p.get('sku').lower() != sku.lower() and p.get('id').lower() != sku.lower()]
    
    if len(updated) < initial_len:
        with open('data/products.json', 'w', encoding='utf-8') as f:
            json.dump(updated, f, ensure_ascii=False, indent=2)
        get_products.cache_clear()
        return jsonify({'success': True, 'message': f'Đã xóa sticker {sku}'})
    return jsonify({'success': False, 'message': 'Không tìm thấy sticker'}), 404

if __name__ == '__main__':
    # Initialize sample orders if empty
    if not os.path.exists(os.path.join(DATA_DIR, 'orders.json')):
        sample_orders = [
            {
                'order_code': 'SC-260825-8866',
                'customer_name': 'Nguyễn Hà My',
                'phone': '0912345678',
                'address': '24 Đường số 3, Cầu Giấy, Hà Nội',
                'note': 'Gói quà sinh nhật giúp mình kèm nơ hồng nhé ạ!',
                'items': [
                    {'sku': 'BOK-PST-002', 'name': 'Sổ Scrapbook Bìa Da Mềm Pastel Hologram', 'price': 220000, 'quantity': 1},
                    {'sku': 'STK-Y2K-001', 'name': 'Sticker 3D Hologram Y2K Sparkle Stars', 'price': 35000, 'quantity': 2},
                    {'sku': 'LAY-POL-001', 'name': 'Layout Khung Ảnh Polaroid Cài Giấy Cổ Điển', 'price': 45000, 'quantity': 1}
                ],
                'total_amount': 335000,
                'discount_amount': 50000,
                'final_amount': 285000,
                'status': 'Đang chuẩn bị tại Xưởng Thủ Công',
                'status_code': 'crafting',
                'created_at': '2026-08-25 14:20:00',
                'timeline': [
                    {'time': '14:20 25/08', 'title': 'Đã nhận đơn hàng', 'desc': 'Đơn hàng đã được xác nhận thanh toán.'},
                    {'time': '16:00 25/08', 'title': 'Đang gia công & đóng gói quà', 'desc': 'Xưởng đang dập nổi sticker 3D và chuẩn bị hộp bảo vệ.'}
                ]
            }
        ]
        save_json_data('orders.json', sample_orders)
        
    print('Starting MEMOUR Studio Flask Server on http://127.0.0.1:5000 ...')
    app.run(host='127.0.0.1', port=5000, debug=True)
