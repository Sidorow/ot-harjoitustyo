import unittest
from app.gameservice import Service

class TestService(unittest.TestCase):
    def setUp(self):
        self.app = Service()
    
    def test_players_are_added(self):
        app = Service()
        app.add_players("Matti")
        for player in app.players:
            self.assertEqual(str(player), "Matti")
        
    def test_check_players_false(self):
        app = Service()
        app.add_players("Matti")
        self.assertEqual(str(app.check_players()), "False")
        
    def test_check_players_true(self):
        app = Service()
        app.add_players("Matti")
        app.add_players("Paavo")
        app.add_players("Kalervo")
        self.assertEqual(str(app.check_players()), "True")
        
    def test_target(self):
        app = Service()
        app.add_players("Matti")
        self.assertEqual(str(app.target()), "Matti")
        
    def test_drink_select_1_player(self):
        app = Service()
        app.add_players("Matti")
        self.assertEqual(str(app.drink_select()), "Pelaaja Matti ottaa juoman")
        
    def test_drink_select_2_player(self):
        app = Service()
        app.add_players("Matti")
        app.add_players("Matti")
        app.add_players("Matti")
        app.add_players("Matti")
        app.add_players("Matti")
        app.add_players("Matti")
        self.assertEqual(str(app.drink_select()), "Pelaajat Matti, Matti, ottavat juoman")
    
    def test_correct_curse_spread(self):
        app = Service()
        app.spread_curse_times()
        self.assertEqual(str(app.curse_times), "[55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]")
        