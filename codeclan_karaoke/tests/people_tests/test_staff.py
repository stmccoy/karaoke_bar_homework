import unittest
from classes.people.staff import *
from classes.people.punter import Punter
from classes.rooms.party_room import PartyRoom

class TestBouncer(unittest.TestCase):

    def setUp(self):
        self.bouncer_1 = Bouncer("Paul", 40, "Male")
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
        self.punter_2 = Punter("Rock", "We Will Rock You", 2, 2, "Darren", 17, "Male")

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
    

class TestKaraokeStaff(unittest.TestCase):

    def setUp(self):
        self.karaoke_staff_1 = KaraokeStaff("Kerry", 22, "Female")

    def test_karaoke_staff_has_name(self):
        self.assertEqual("Kerry", self.karaoke_staff_1.name)
    
    def test_karaoke_staff_has_age(self):
        self.assertEqual(22, self.karaoke_staff_1.age)
    
    def test_karaoke_staff_has_gender(self):
        self.assertEqual("Female", self.karaoke_staff_1.gender)

class TestCheckInStaff(unittest.TestCase):

    def setUp(self):
        self.check_in_staff_1 = CheckInStaff("Kirsty", 35, "Female")
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
        self.punter_2 = Punter("Rock", "We Will Rock You", 2, 2, "Darren", 17, "Male")

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
    

    
    
    
    