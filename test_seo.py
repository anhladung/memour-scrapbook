import json
import re
import unittest
from pathlib import Path

from app import app, get_blogs, get_products


class SeoSmokeTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.site_url = app.config['SITE_URL']

    def test_homepage_metadata(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('MEMOUR Studio', html)
        self.assertIn('Scrapbook', html)
        self.assertIn(f'<link rel="canonical" href="{self.site_url}/">', html)
        self.assertTrue('/favicon.ico' in html or 'favicon-512.png' in html)

        scripts = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL
        )
        graph = json.loads(scripts[0])['@graph']
        website = next(item for item in graph if item['@type'] == 'WebSite')
        self.assertEqual(website['name'], 'MEMOUR Studio')
        self.assertEqual(website['url'], f'{self.site_url}/')

    def test_production_domain_is_the_canonical_origin(self):
        """Prevent deployment aliases from leaking into indexable SEO URLs."""
        production_url = 'https://memourscrapbook.com'
        self.assertEqual(self.site_url, production_url)

        about_html = self.client.get('/about').get_data(as_text=True)
        self.assertIn(
            f'<link rel="canonical" href="{production_url}/about">',
            about_html,
        )
        self.assertNotIn('memourscrapbook.vercel.app', about_html)

        robots = self.client.get('/robots.txt').get_data(as_text=True)
        sitemap = self.client.get('/sitemap.xml').get_data(as_text=True)
        self.assertIn(f'Sitemap: {production_url}/sitemap.xml', robots)
        self.assertIn(f'<loc>{production_url}/about</loc>', sitemap)
        self.assertNotIn('memourscrapbook.vercel.app', robots + sitemap)

    def test_legacy_vercel_domain_redirects_to_canonical_domain(self):
        response = self.client.get(
            '/about?source=legacy',
            base_url='https://memourscrapbook.vercel.app',
        )
        self.assertEqual(response.status_code, 308)
        self.assertEqual(
            response.headers['Location'],
            'https://memourscrapbook.com/about?source=legacy',
        )

    def test_favicon_and_public_urls(self):
        for path in ('/favicon.ico', '/static/assets/favicon-512.png', '/static/assets/apple-touch-icon.png'):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                response.close()

        for path in ('/guide', '/guide/scrapbook-la-gi', '/guide/mau-luu-but-dep'):
            with self.subTest(path=path):
                html = self.client.get(path).get_data(as_text=True)
                self.assertIn(f'<link rel="canonical" href="{self.site_url}{path}">', html)

        sitemap = self.client.get('/sitemap.xml').get_data(as_text=True)
        self.assertIn(f'<loc>{self.site_url}/</loc>', sitemap)
        robots = self.client.get('/robots.txt').get_data(as_text=True)
        self.assertIn(f'Sitemap: {self.site_url}/sitemap.xml', robots)

    def test_new_guides_are_complete_and_reachable(self):
        blogs = get_blogs()
        slugs = {blog['slug'] for blog in blogs}
        skus = {product['sku'] for product in get_products()}
        self.assertGreaterEqual(len(blogs), 17)
        self.assertEqual(len(slugs), len(blogs))

        sitemap = self.client.get('/sitemap.xml').get_data(as_text=True)
        for blog in blogs:
            if not blog.get('content_file'):
                continue
            with self.subTest(slug=blog['slug']):
                self.assertTrue((Path(app.static_folder) / blog['cover_image'].removeprefix('/static/')).is_file())
                self.assertTrue(set(blog['related_skus']).issubset(skus))
                self.assertTrue(set(re.findall(r'href="/guide/([^"]+)"', blog['content'])).issubset(slugs))
                self.assertGreaterEqual(blog['content'].count('<h2>'), 3)
                self.assertGreaterEqual(len(blog['faqs']), 2)

                path = f"/guide/{blog['slug']}"
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                html = response.get_data(as_text=True)
                self.assertIn(f'<link rel="canonical" href="{self.site_url}{path}">', html)
                self.assertIn(f'<loc>{self.site_url}{path}</loc>', sitemap)
                scripts = re.findall(
                    r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL
                )
                for script in scripts:
                    json.loads(script)


if __name__ == '__main__':
    unittest.main()
