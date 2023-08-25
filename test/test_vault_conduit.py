import unittest
from app.VaultConduit import VaultConduit


class VaultConduitTest(unittest.TestCase):
    def test_vault_conduit(self):
        vault_conn = VaultConduit()
        assert isinstance(vault_conn, VaultConduit)


    def test_vault_get(self):
        vault_conn = VaultConduit()
        vault_get = vault_conn.vault_conduit_query()
        self.assertEqual(vault_get, isinstance())
