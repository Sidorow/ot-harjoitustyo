import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate = Kassapaate()
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0
        
    def test_luokan_alustus_toimii(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        
    def test_kateisosto_ei_toimi_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        osto = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(str(osto), "230")
    
    def test_kateisosto_ei_toimi_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
        osto = self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(str(osto), "390")
        
    def test_kateisosto_toimii_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassapaate.edulliset), "1")
        osto = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(osto), "10")
        
    def test_kateisosto_toimii_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
        osto = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(str(osto), "50")
        
        
    def test_korttiosto_toimii_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(osto), "True")
        self.assertEqual(str(self.kassapaate.edulliset), "2")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_korttiosto_ei_toimi_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.4")
        self.assertEqual(str(self.kassapaate.edulliset), "4")
        osto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(osto), "False")
        self.assertEqual(str(self.kassapaate.edulliset), "4")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        
    def test_korttiosto_toimii_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(osto), "True")
        self.assertEqual(str(self.kassapaate.maukkaat), "2")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        
    def test_korttiosto_ei_toimi_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")
        self.assertEqual(str(self.kassapaate.maukkaat), "2")
        osto = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(osto), "False")
        self.assertEqual(str(self.kassapaate.maukkaat), "2")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        
    def test_kortille_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "101000")
        
    def test_kortille_lataus_ei_toimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-10)
        osto = self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-10)
        self.assertEqual(str(osto), "False")
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        
        
        