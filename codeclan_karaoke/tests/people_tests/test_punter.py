import unittest
from classes.people.punter import Punter
from classes.songs.song import Song
from classes.people.staff import *
from classes.rooms.party_room import PartyRoom

class TestPunter(unittest.TestCase):

    def setUp(self):
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
        self.punter_2 = Punter("Pop", "Hit Me Baby One More Time", 1, 2, "Steve", 50, "Male")
        self.song_1 = Song("Hit Me Baby One More Time", "Britney Spears", "Pop")
        self.karaoke_staff_1 = KaraokeStaff("Kerry", 22, "Female")
        self.bouncer_1 = Bouncer("Paul", 40, "Male")
        self.party_room_1 = PartyRoom("Rock",[], [], 30, 10)
        self.party_room_2 = PartyRoom("Pop", [], [], 30, 10)
        self.party_room_3 = PartyRoom("RnB", [], [], 30, 30)

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
    
    def test_punter_pay_fee(self):
        self.punter_1.pay_fee(5)
        self.assertEqual(55, self.punter_1.money)
    
    def test_punter_request_song_success(self):
        self.punter_1.request_song(self.karaoke_staff_1, self.song_1, 2)
        self.assertEqual(58, self.punter_1.money)
    
    def test_punter_request_song_fail(self):
        self.punter_1.request_song(self.karaoke_staff_1, self.song_1, 2)
        self.assertEqual(1, self.punter_2.money)
    
    def test_punter_change_room_success(self):
        room_1 = self.party_room_1
        room_2 = self.party_room_2
        bouncer = self.bouncer_1
        self.punter_1.change_room(room_1, room_2, bouncer)
        self.assertEqual(9, room_1.current_punter_total)
        self.assertEqual(11, room_2.current_punter_total)
    
    def test_punter_change_room_fail(self):
        room_1 = self.party_room_1
        room_2 = self.party_room_3
        bouncer = self.bouncer_1
        self.punter_1.change_room(room_1, room_2, bouncer)
        self.assertEqual(9, room_1.current_punter_total)
        self.assertEqual(30, room_2.current_punter_total)
        self.assertEqual(1, len(room_2.queue))
    
    def test_punter_go_home(self):
        room = self.party_room_1
        self.punter_1.go_home(room)
        self.assertEqual(9, room.current_punter_total)


