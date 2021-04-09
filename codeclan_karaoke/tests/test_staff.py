import unittest
from classes.staff import *

class TestBouncer(unittest.TestCase):

    def setUp(self):
        self.bouncer_1 = Bouncer("Paul", 40, "Male")

    def test_bouncer_has_name(self):
        self.assertEqual("Paul", self.bouncer_1.name)
    
    def test_bouncer_has_age(self):
        self.assertEqual(40, self.bouncer_1.age)
    
    def test_bouncer_has_gender(self):
        self.assertEqual("Male", self.bouncer_1.gender)

class TestBarStaff(unittest.TestCase):

    def setUp(self):
        self.bar_staff_1 = BarStaff("Kerry", 22, "Female")

    def test_bar_staff_has_name(self):
        self.assertEqual("Kerry", self.bar_staff_1.name)
    
    def test_bar_staff_has_age(self):
        self.assertEqual(22, self.bar_staff_1.age)
    
    def test_bar_staff_has_gender(self):
        self.assertEqual("Female", self.bar_staff_1.gender)

class TestCheckInStaff(unittest.TestCase):

    def setUp(self):
        self.check_in_staff_1 = CheckInStaff("Kirsty", 35, "Female")

    def test_check_in_staff_has_name(self):
        self.assertEqual("Kirsty", self.check_in_staff_1.name)
    
    def test_check_in_staff_has_age(self):
        self.assertEqual(35, self.check_in_staff_1.age)
    
    def test_check_in_staff_has_gender(self):
        self.assertEqual("Female", self.check_in_staff_1.gender)
    
    
    