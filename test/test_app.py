import unittest
from app import create_app


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.update({
            "TESTING": True
        })

        self.client = self.app.test_client()

    def test_health_check_ok(self):
        res = self.client.get('/health-check')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Ok', res.data)
