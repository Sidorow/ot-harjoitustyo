import unittest
from app.gameservice import Service

class TestService(unittest.TestCase):
    def setUp(self):
        self.app = Service()
    
    def test_players_are_added(self):
        app = Service()
        app.add_players("Matti")
        self.assertEqual(str(app.players), "['Matti']")