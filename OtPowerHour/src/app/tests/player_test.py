import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Matti")
        
    def test_drinks_are_added(self):
        self.assertEqual(str(self.player.get_stats()), "Juomia juotu: 0")
        self.player.add_drink()
        self.assertEqual(str(self.player.get_stats()), "Juomia juotu: 1")