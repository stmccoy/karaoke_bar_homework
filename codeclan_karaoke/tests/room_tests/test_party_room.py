import unittest
from classes.rooms.party_room import PartyRoom
from classes.songs.song import Song
from classes.people.punter import Punter
from classes.people.staff import KaraokeStaff


class TestPartyRoom(unittest.TestCase):

    def setUp(self):
        self.party_room_1 = PartyRoom("Rock", [], [], 30, 20)
        self.song_1 = Song("Hit Me Baby One More Time", "Britney Spears", "Pop")
        self.punter_1 = Punter("Pop", "Hit Me Baby One More Time", 60, 2, "Beverly", 50, "Female")
        self.punter_2 = Punter("Pop", "Hit Me Baby One More Time", 1, 2, "Steve", 50, "Male")
        self.karaoke_staff_1 = KaraokeStaff("Kerry", 22, "Female")
        self.song_fee = 2
    
    def test_party_room_has_genre(self):
        self.assertEqual("Rock", self.party_room_1.genre)

    def test_party_room_has_queue(self):
        self.assertEqual(0, len(self.party_room_1.queue))
    
    def test_party_room_has_staff(self):
        self.assertEqual(0, len(self.party_room_1.staff))
    
    def test_party_room_has_capacity(self):
        self.assertEqual(30, self.party_room_1.capacity)
    
    def test_party_room_can_play_song(self):
        song = self.song_1
        punter = self.punter_1
        karaoke_staff = self.karaoke_staff_1
        song_fee = self.song_fee
        self.party_room_1.play_song(song, punter, karaoke_staff, song_fee)
        self.assertEqual(song, self.party_room_1.song_playing)
    
    def test_party_room_cannot_play_song(self):
        song = self.song_1
        punter = self.punter_2
        karaoke_staff = self.karaoke_staff_1
        song_fee = self.song_fee
        self.party_room_1.play_song(song, punter, karaoke_staff, song_fee)
        self.assertEqual(None, self.party_room_1.song_playing)
    
