import json
import os
import sys
import types
import unittest

from app import app


class _Promise:
    def __init__(self, value):
        self.value = value


class _Result(dict):
    def to_py(self):
        return dict(self)


class _Statement:
    def __init__(self, database, sql):
        self.database = database
        self.sql = sql
        self.params = ()

    def bind(self, *params):
        self.params = params
        return self

    def run(self):
        if self.sql.startswith('INSERT'):
            self.database.rows.append(json.loads(self.params[2]))
            return _Promise(_Result(success=True, results=[]))

        query = self.params[0].strip('%').lower()
        phone = self.params[1].strip('%')
        rows = [
            {'payload': json.dumps(order, ensure_ascii=False)}
            for order in self.database.rows
            if query in order['order_code'].lower() or phone in order['phone']
        ]
        return _Promise(_Result(success=True, results=rows))


class _Database:
    def __init__(self):
        self.rows = []

    def prepare(self, sql):
        return _Statement(self, sql)


class CloudflareMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pyodide = types.ModuleType('pyodide')
        ffi = types.ModuleType('pyodide.ffi')
        ffi.run_sync = lambda promise: promise.value
        pyodide.ffi = ffi
        sys.modules.setdefault('pyodide', pyodide)
        sys.modules.setdefault('pyodide.ffi', ffi)

    def setUp(self):
        self.client = app.test_client()
        self.database = _Database()
        self.worker_env = types.SimpleNamespace(DB=self.database)

    def test_static_directory_and_google_analytics_are_preserved(self):
        self.assertTrue(app.static_folder.endswith(os.path.join('public', 'static')))
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('G-EH7LKGCKHH', response.get_data(as_text=True))

    def test_orders_use_d1_inside_cloudflare(self):
        environment = {'workers.env': self.worker_env}
        created = self.client.post(
            '/api/orders',
            json={'name': 'Cloudflare Test', 'phone': '0900000000', 'items': []},
            environ_overrides=environment,
        )
        self.assertEqual(created.status_code, 200)
        order_code = created.get_json()['order']['order_code']

        found = self.client.get(
            f'/api/orders?q={order_code}',
            environ_overrides=environment,
        )
        self.assertEqual(found.status_code, 200)
        self.assertEqual(found.get_json()['orders'][0]['phone'], '0900000000')

    def test_orders_fail_clearly_when_d1_binding_is_missing(self):
        response = self.client.get(
            '/api/orders?q=SC-',
            environ_overrides={'workers.env': types.SimpleNamespace()},
        )
        self.assertEqual(response.status_code, 503)


if __name__ == '__main__':
    unittest.main()
