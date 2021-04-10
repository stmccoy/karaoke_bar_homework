import unittest
from classes.rooms.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.room_1 = Room([], [], 30, 20)

    def test_room_has_queue(self):

        self.assertEqual(0, len(self.room_1.queue))
    
    def test_room_has_staff(self):

        self.assertEqual(0, len(self.room_1.staff))
    
    def test_room_has_capacity(self):

        self.assertEqual(30, self.room_1.capacity)