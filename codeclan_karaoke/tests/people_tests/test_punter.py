import unittest
from classes.people.punter import Punter

class TestPunter(unittest.TestCase):

    def setUp(self):

        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
    
    def test_punter_has_name(self):
        self.assertEqual("Beverly", self.punter_1.name)
    
    def test_punter_has_age(self):
        self.assertEqual(50, self.punter_1.age)
    
    def test_punter_has_gender(self):
        self.assertEqual("Female", self.punter_1.gender)
    
    def test_punter_has_fave_genre(self):
        self.assertEqual("Pop", self.punter_1.fave_genre)
    
    def test_punter_has_fave_song(self):
        self.assertEqual("Hit Me Baby One More Time", self.punter_1.fave_song)
    
    def test_punter_has_money(self):
        self.assertEqual(60, self.punter_1.money)
    
    def test_punter_has_honesty(self):
        self.assertEqual(2, self.punter_1.honesty)
