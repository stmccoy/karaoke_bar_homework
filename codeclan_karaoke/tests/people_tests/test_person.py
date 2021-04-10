import unittest
from classes.people.person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person_1 = Person("Fred", 20, "Male")
        self.person_2 = Person("Holly", 40, "Female")
    
    def test_person_has_name(self):
        self.assertEqual("Fred", self.person_1.name)
    
    def test_person_has_name(self):
        self.assertEqual("Holly", self.person_2.name)
    
    def test_person_has_age(self):
        self.assertEqual(20, self.person_1.age)
    
    def test_person_has_age(self):
        self.assertEqual(40, self.person_2.age)
    
    def test_person_has_gender(self):
        self.assertEqual("Female", self.person_2.gender)