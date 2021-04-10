import unittest
from classes.rooms.party_room import PartyRoom

class TestPartyRoom(unittest.TestCase):

    def setUp(self):

        self.party_room_1 = PartyRoom("Rock", [], [], 30, 20)
    
    def test_party_room_has_genre(self):
        self.assertEqual("Rock", self.party_room_1.genre)

    def test_party_room_has_queue(self):

        self.assertEqual(0, len(self.party_room_1.queue))
    
    def test_party_room_has_staff(self):

        self.assertEqual(0, len(self.party_room_1.staff))
    
    def test_party_room_has_capacity(self):

        self.assertEqual(30, self.party_room_1.capacity)
    
