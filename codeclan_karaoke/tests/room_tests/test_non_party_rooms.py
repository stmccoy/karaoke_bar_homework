import unittest
from classes.rooms.non_party_rooms import *
from classes.people.staff import *
from classes.people.punter import Punter
from classes.rooms.party_room import PartyRoom

class TestToilet(unittest.TestCase):

    def setUp(self):
        self.toilet_1 = Toilet("Female", [], [], 5, 2)
        self.toilet_2 = Toilet("Male", [], [], 5, 2)

    def test_toilet_has_queue(self):
        self.assertEqual(0, len(self.toilet_1.queue))
    
    def test_toilet_has_staff(self):
        self.assertEqual(0, len(self.toilet_1.staff))
    
    def test_toilet_has_capacity(self):
        self.assertEqual(5, self.toilet_1.capacity)
    
    def test_toilet_has_current_punter_total(self):
        self.assertEqual(2, self.toilet_1.current_punter_total)
    
    def test_toilet_has_gender(self):
        self.assertEqual("Female", self.toilet_1.gender)

    def test_toilet_has_gender(self):
        self.assertEqual("Male", self.toilet_2.gender)
    
    def test_confirm_type(self):
        self.assertEqual(True, isinstance(self.toilet_1, Toilet))

class TestSmokingArea(unittest.TestCase):

    def setUp(self):
        self.smoking_area_1 = SmokingArea([], [], 15, 10)

    def test_smoking_area_has_queue(self):
        self.assertEqual(0, len(self.smoking_area_1.queue)) 

    def test_smoking_area_has_staff(self):
        self.assertEqual(0, len(self.smoking_area_1.staff)) 

    def test_smoking_area_has_capacity(self):
        self.assertEqual(15, self.smoking_area_1.capacity)
    
    def test_smoking_area_has_current_punter_total(self):
        self.assertEqual(10, self.smoking_area_1.current_punter_total)

class TestCheckInRoom(unittest.TestCase):

    def setUp(self):
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, "Beverly", 17, "Female")
        self.punter_2 = Punter("Rock", "American Idiot", 3, "Beverly", 20, "Female")
        self.punter_3 = Punter("RnB", "Tipsy", 3, "Craig", 20, "Male")
        self.check_in_staff_1 = CheckInStaff("Kirsty", 35, "Female")
        self.bouncer_1 = Bouncer("Paul", 40, "Male")
        self.check_in_room_1 = CheckInRoom(5, [self.punter_1, self.punter_2, self.punter_3], [self.check_in_staff_1, self.bouncer_1], 10, 5)
        self.party_room_1 = PartyRoom("Rock",[], [self.check_in_staff_1], 30, 10)
        self.party_room_2 = PartyRoom("Pop", [], [self.check_in_staff_1], 30, 10)
        self.party_room_3 = PartyRoom("RnB", [], [self.check_in_staff_1], 30, 30)
        
    
    def test_check_in_room_has_fee(self):
        self.assertEqual(5, self.check_in_room_1.entrance_fee)

    def test_check_in_room_has_queue(self):
        self.assertEqual(3, len(self.check_in_room_1.queue))
    
    def test_check_in_room_has_staff(self):
        self.assertEqual(2, len(self.check_in_room_1.staff))
    
    def test_check_in_room_has_capacity(self):
        self.assertEqual(10, self.check_in_room_1.capacity)
    
    def test_check_in_room_has_current_punter_total(self):
        self.assertEqual(5, self.check_in_room_1.current_punter_total)
    
    def test_admission_process_id_fail(self):
        entrance_fee = self.check_in_room_1.entrance_fee
        punter = self.check_in_room_1.queue[0]
        check_in_staff = self.check_in_room_1.staff[0]
        bouncer = self.check_in_room_1.staff[1]
        party_rooms_list = [self.party_room_1, self.party_room_2, self.party_room_3]
        self.assertEqual(False, self.check_in_room_1.admit_punter(punter, bouncer, check_in_staff, entrance_fee, party_rooms_list))
    
    def test_admission_process_entrance_fee_fail(self):
        punter = self.check_in_room_1.queue[1]
        check_in_staff = self.check_in_room_1.staff[0]
        bouncer = self.check_in_room_1.staff[1]
        entrance_fee = self.check_in_room_1.entrance_fee
        party_rooms_list = [self.party_room_1, self.party_room_2, self.party_room_3]
        self.assertEqual(False, self.check_in_room_1.admit_punter(punter, bouncer, check_in_staff, entrance_fee, party_rooms_list))
    
    def test_admission_process_no_favourite_genre_match_between_punter_and_rooms(self):
        punter = self.check_in_room_1.queue[0]
        check_in_staff = self.check_in_room_1.staff[0]
        bouncer = self.check_in_room_1.staff[1]
        entrance_fee = self.check_in_room_1.entrance_fee
        party_rooms_list = [self.party_room_1, self.party_room_3]
        self.assertEqual(False, self.check_in_room_1.admit_punter(punter, bouncer, check_in_staff, entrance_fee, party_rooms_list))

    def test_admission_process_sucess(self):
        punter = self.check_in_room_1.queue[2]
        check_in_staff = self.check_in_room_1.staff[0]
        bouncer = self.check_in_room_1.staff[1]
        entrance_fee = self.check_in_room_1.entrance_fee
        party_rooms_list = [self.party_room_1, self.party_room_2, self.party_room_3]
        self.check_in_room_1.admit_punter(punter, bouncer, check_in_staff, entrance_fee, party_rooms_list)
        self.assertEqual(0, len(party_rooms_list[2].queue))


