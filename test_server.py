import unittest
import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding="utf-8")

from app import app

class ScrapCraftTestSuite(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_routes_status_code(self):
        routes = [
            "/",
            "/about",
            "/products",
            "/product/STK-Y2K-001",
            "/inspirations",
            "/handbook",
            "/handbook/huong-dan-layering-sticker-3d-chieu-sau-scrapbook",
            "/contact",
            "/studio",
            "/cart",
            "/order-tracking"
        ]
        for route in routes:
            response = self.app.get(route)
            self.assertEqual(response.status_code, 200, f"Route {route} failed with status {response.status_code}")
            print(f"[PASS] Route {route} OK (Status 200)")

    def test_api_products(self):
        response = self.app.get("/api/products")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        print(f"[PASS] API /api/products OK ({len(data)} items)")

    def test_api_inspirations(self):
        response = self.app.get("/api/inspirations")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        print(f"[PASS] API /api/inspirations OK ({len(data)} inspirations)")

    def test_api_ai_suggest(self):
        payload = {"prompt": "kỷ niệm bạn thân đi đà lạt vintage"}
        response = self.app.post("/api/ai-suggest", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data.get("status"), "success")
        self.assertIn("ai_reasoning", data)
        self.assertIn("canvas_preset", data)
        self.assertGreater(len(data["canvas_preset"]["items"]), 0)
        print(f"[PASS] API /api/ai-suggest OK: {data['ai_reasoning']}")

    def test_api_order_create_and_query(self):
        order_payload = {
            "name": "Test User",
            "phone": "0999999999",
            "address": "Test Address HCM",
            "items": [{"sku": "STK-Y2K-001", "name": "Sticker Test", "price": 35000, "quantity": 2}],
            "total_amount": 70000,
            "discount_amount": 0,
            "final_amount": 70000
        }
        res_post = self.app.post("/api/orders", data=json.dumps(order_payload), content_type="application/json")
        self.assertEqual(res_post.status_code, 200)
        order_created = json.loads(res_post.data)
        self.assertEqual(order_created.get("status"), "success")
        order_code = order_created["order"]["order_code"]
        print(f"[PASS] API /api/orders POST OK (Created {order_code})")

        # Query back
        res_get = self.app.get(f"/api/orders?q={order_code}")
        self.assertEqual(res_get.status_code, 200)
        order_queried = json.loads(res_get.data)
        self.assertEqual(order_queried.get("status"), "success")
        self.assertEqual(len(order_queried["orders"]), 1)
        print(f"[PASS] API /api/orders GET OK (Found {order_code})")

if __name__ == "__main__":
    unittest.main()
