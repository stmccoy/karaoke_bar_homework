import unittest
from classes.people.punter import Punter
from classes.songs.song import Song
from classes.people.staff import *
from classes.rooms.party_room import PartyRoom

class TestPunter(unittest.TestCase):

    def setUp(self):
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, "Beverly", 50, "Female")
        self.punter_2 = Punter("Pop", "Hit Me Baby One More Time", 1, "Steve", 50, "Male")
        self.song_1 = Song("Hit Me Baby One More Time", "Britney Spears", "Pop")
        self.karaoke_staff_1 = KaraokeStaff("Kerry", 22, "Female")
        self.bouncer_1 = Bouncer("Paul", 40, "Male")
        self.party_room_1 = PartyRoom("Rock",[], [], 30, 10)
        self.party_room_2 = PartyRoom("Pop", [], [], 30, 10)
        self.party_room_3 = PartyRoom("RnB", [], [], 30, 30)
        self.toilet_1 = Toilet("Female", [], [], 5, 2)
        self.toilet_2 = Toilet("Male", [], [], 5, 2)
        self.toilet_3 = Toilet("Male", [], [], 5, 5)

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
    
    def test_punter_change_room_success_toilet(self):
        room_1 = self.party_room_1
        female_toilet = self.toilet_1
        bouncer = self.bouncer_1
        female_punter = self.punter_1
        female_punter.change_room(room_1, female_toilet, bouncer)
        self.assertEqual(9, room_1.current_punter_total)
        self.assertEqual(3, female_toilet.current_punter_total)
    
    def test_punter_change_room_fail(self):
        room_1 = self.party_room_1
        room_2 = self.party_room_3
        bouncer = self.bouncer_1
        self.punter_1.change_room(room_1, room_2, bouncer)
        self.assertEqual(9, room_1.current_punter_total)
        self.assertEqual(30, room_2.current_punter_total)
        self.assertEqual(1, len(room_2.queue))
    
    def test_punter_change_room_gender_fail_toilet(self):
        room_1 = self.party_room_1
        male_toilet = self.toilet_2
        bouncer = self.bouncer_1
        female_punter = self.punter_1
        female_punter.change_room(room_1, male_toilet, bouncer)
        self.assertEqual(10, room_1.current_punter_total)
        self.assertEqual(2, male_toilet.current_punter_total)
    
    def test_punter_change_room_capacity_fail_toilet(self):
        room_1 = self.party_room_1
        full_toilet = self.toilet_3
        bouncer = self.bouncer_1
        male_punter = self.punter_2
        male_punter.change_room(room_1, full_toilet, bouncer)
        self.assertEqual(9, room_1.current_punter_total)
        self.assertEqual(5, full_toilet.current_punter_total)
        self.assertEqual(1, len(full_toilet.queue))
    
    def test_punter_go_home(self):
        room = self.party_room_1
        self.punter_1.go_home(room)
        self.assertEqual(9, room.current_punter_total)
    
    def test_punter_favourite_song_shout(self):
        room = self.party_room_1
        room.song_playing = "Hit Me Baby One More Time"
        self.assertEqual("OMG I LOVE THIS SONG!!!", self.punter_1.shout(room))
    
    def test_punter_not_favourite_song_shout(self):
        room = self.party_room_1
        room.song_playing = "Gotta Get Thru This"
        self.assertEqual("WOOP WOOP", self.punter_1.shout(room))


