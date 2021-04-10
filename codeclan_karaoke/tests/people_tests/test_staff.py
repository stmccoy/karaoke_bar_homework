import unittest
from classes.people.staff import *
from classes.people.punter import Punter
from classes.rooms.party_room import PartyRoom
from classes.songs.song import Song

class TestBouncer(unittest.TestCase):

    def setUp(self):
        self.bouncer_1 = Bouncer("Paul", 40, "Male")
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
        self.punter_2 = Punter("Rock", "We Will Rock You", 2, 2, "Darren", 17, "Male")
        self.party_room_1 = PartyRoom("Rock",[], [], 30, 10)
        self.party_room_2 = PartyRoom("RnB", [], [], 30, 30)

    def test_bouncer_has_name(self):
        self.assertEqual("Paul", self.bouncer_1.name)
    
    def test_bouncer_has_age(self):
        self.assertEqual(40, self.bouncer_1.age)
    
    def test_bouncer_has_gender(self):
        self.assertEqual("Male", self.bouncer_1.gender)
    
    def test_bouncer_checks_id_and_admits(self):
        self.assertEqual("On you go mate", self.bouncer_1.check_id(self.punter_1))
    
    def test_bouncer_checks_id_and_rejects(self):
        self.assertEqual("Sling your hook pal", self.bouncer_1.check_id(self.punter_2))
    
    def test_bouncer_allow_room_change(self):
        room = self.party_room_1
        self.assertEqual(True, self.bouncer_1.allow_in_room(room))
    
    def test_bouncer_reject_room_change(self):
        room = self.party_room_2
        self.assertEqual(False, self.bouncer_1.allow_in_room(room))
    

class TestKaraokeStaff(unittest.TestCase):

    def setUp(self):
        self.karaoke_staff_1 = KaraokeStaff("Kerry", 22, "Female")
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
        self.punter_2 = Punter("Pop", "Hit Me Baby One More Time", 1, 2, "Steve", 50, "Male")
        self.song_fee = 2

    def test_karaoke_staff_has_name(self):
        self.assertEqual("Kerry", self.karaoke_staff_1.name)
    
    def test_karaoke_staff_has_age(self):
        self.assertEqual(22, self.karaoke_staff_1.age)
    
    def test_karaoke_staff_has_gender(self):
        self.assertEqual("Female", self.karaoke_staff_1.gender)
    
    def test_karaoke_staff_take_song_request(self):
        punter = self.punter_1
        song_fee = self.song_fee      

        self.assertEqual(True, self.karaoke_staff_1.accept_song_request(punter, song_fee))
    
    def test_karaoke_staff_refuse_song_request(self):
        punter = self.punter_2 
        song_fee = self.song_fee      

        self.assertEqual(False, self.karaoke_staff_1.accept_song_request(punter, song_fee))
        

class TestCheckInStaff(unittest.TestCase):

    def setUp(self):
        self.check_in_staff_1 = CheckInStaff("Kirsty", 35, "Female")
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
        self.punter_2 = Punter("Rock", "We Will Rock You", 2, 2, "Darren", 17, "Male")
        self.punter_3 = Punter("RnB", "Tipsy", 30, 2, "Karl", 35, "Male")
        self.party_room_1 = PartyRoom("Rock",[], [self.check_in_staff_1], 30, 10)
        self.party_room_2 = PartyRoom("Pop", [], [self.check_in_staff_1], 30, 10)
        self.party_room_3 = PartyRoom("RnB", [], [self.check_in_staff_1], 30, 30)
        self.party_rooms_list = [self.party_room_1, self.party_room_2, self.party_room_3]

    def test_check_in_staff_has_name(self):
        self.assertEqual("Kirsty", self.check_in_staff_1.name)
    
    def test_check_in_staff_has_age(self):
        self.assertEqual(35, self.check_in_staff_1.age)
    
    def test_check_in_staff_has_gender(self):
        self.assertEqual("Female", self.check_in_staff_1.gender)
    
    def test_pay_entrance_fee_not_enough_money(self):
        self.assertEqual("Not enough money, sorry", self.check_in_staff_1.take_entrance_fee(self.punter_2, 5))
    
    def test_pay_entrance_fee_enough_money(self):
        self.assertEqual("Thank You", self.check_in_staff_1.take_entrance_fee(self.punter_1, 5))
        self.assertEqual(55, self.punter_1.money)
    
    def test_admission_to_room_success(self):
        self.check_in_staff_1.room_assign(self.punter_1, self.party_rooms_list)
        self.assertEqual(11, self.party_room_2.current_punter_total)
    
    def test_admission_to_room_full(self):
        self.check_in_staff_1.room_assign(self.punter_3, self.party_rooms_list)
        self.assertEqual(30, self.party_room_3.current_punter_total)
        self.assertEqual(1, len(self.party_room_3.queue))
    

    
    
    
    