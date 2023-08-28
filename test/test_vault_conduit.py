import unittest
from app.VaultConduit import VaultConduit


class VaultConduitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vault_conn = VaultConduit()

    def test_vault_conduit_constructor(self):
        assert isinstance(self.vault_conn, VaultConduit)

    def test_vault_get(self):
        expected = {'hush_hush': 'test'}
        vault_get = self.vault_conn.get_secret()
        assert isinstance(vault_get, dict)
        self.assertEqual(vault_get, expected)