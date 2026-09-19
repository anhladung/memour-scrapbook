import os
import sys
import json
import unittest
from app import app, get_products

class TestScrapbookApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_routes_status_200_or_redirect(self):
        routes = [
            ('/', 200),
            ('/about', 200),
            ('/products', 200),
            ('/product/STK-001', 200),
            ('/product/LAY-001', 200),
            ('/product/LAY-002', 200),
            ('/product/LAY-003', 200),
            ('/product/SCR-001', 200),
            ('/inspiration', 200),
            ('/inspiration/insp_001', 302),
            ('/guide', 200),
            ('/guide/mau-luu-but-dep', 200),
            ('/mau-luu-but-dep', 200),
            ('/contact', 200),
            ('/studio', 200),
            ('/cart', 200),
            ('/orders', 200),
            ('/order-tracking', 200),
            ('/api/products', 200),
            ('/api/blogs', 200)
        ]
        for route, expected_status in routes:
            res = self.app.get(route)
            self.assertEqual(res.status_code, expected_status, f"Route {route} returned status {res.status_code} (expected {expected_status})")

    def test_announcement_bar_removed(self):
        res = self.app.get('/')
        content = res.data.decode('utf-8')
        self.assertNotIn('MÃ ƯU ĐÃI: GENZ10', content, "Announcement bar should be removed from header")

    def test_patterns_files_exist(self):
        patterns = [
            'pat_kraft.svg', 'pat_grid.svg', 'pat_dotgrid.svg', 'pat_botanical.svg',
            'pat_vintage_news.svg', 'pat_gingham_pink.svg', 'pat_black_card.svg', 'pat_parchment.svg'
        ]
        for pat in patterns:
            path = os.path.join('static', 'assets', 'patterns', pat)
            self.assertTrue(os.path.exists(path), f"Pattern file {path} must exist")

    def test_ai_suggest_endpoint(self):
        payload = {
            'prompt': 'kỷ yếu thanh xuân bạn thân vintage đà lạt',
            'mood': 'vintage'
        }
        res = self.app.post('/api/ai-suggest', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data.get('status'), 'success')
        self.assertIn('ai_reasoning', data)
        self.assertIn('book', data)
        self.assertGreaterEqual(len(data.get('layouts', [])), 1)
        self.assertGreaterEqual(len(data.get('stickers', [])), 1)
    def test_memour_branding(self):
        res = self.app.get('/')
        content = res.data.decode('utf-8')
        self.assertIn('MEMOUR', content)
        self.assertIn('Every memory has a story', content)
        print("MEMOUR Branding Test: SUCCESS")

if __name__ == '__main__':
    unittest.main()
