import unittest
from classes.rooms.non_party_rooms import *

class TestToilet(unittest.TestCase):

    def setUp(self):

        self.toilet_1 = Toilet([], [], 30)

    def test_toilet_has_queue(self):

        self.assertEqual(0, len(self.toilet_1.queue))
    
    def test_toilet_has_staff(self):

        self.assertEqual(0, len(self.toilet_1.staff))
    
    def test_toilet_has_capacity(self):

        self.assertEqual(30, self.toilet_1.capacity)

class TestSmokingArea(unittest.TestCase):

    def setUp(self):

        self.smoking_area_1 = SmokingArea([], [], 30)

    def test_smoking_area_has_queue(self):

        self.assertEqual(0, len(self.smoking_area_1.queue))
    
    def test_smoking_area_has_staff(self):

        self.assertEqual(0, len(self.smoking_area_1.staff))
    
    def test_smoking_area_has_capacity(self):

        self.assertEqual(30, self.smoking_area_1.capacity)

class TestCheckInRoom(unittest.TestCase):

    def setUp(self):

        self.check_in_room_1 = CheckInRoom(5, [], [], 30)
    
    def test_check_in_room_has_fee(self):
        self.assertEqual(5, self.check_in_room_1.entrance_fee)

    def test_check_in_room_has_queue(self):

        self.assertEqual(0, len(self.check_in_room_1.queue))
    
    def test_check_in_room_has_staff(self):

        self.assertEqual(0, len(self.check_in_room_1.staff))
    
    def test_check_in_room_has_capacity(self):

        self.assertEqual(30, self.check_in_room_1.capacity)