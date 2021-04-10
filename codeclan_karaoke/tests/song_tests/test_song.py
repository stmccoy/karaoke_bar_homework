import unittest
from classes.songs.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("We Will Rock You", "Queen", "Rock")
    
    def test_song_has_title(self):
        self.assertEqual("We Will Rock You", self.song_1.title)
    
    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song_1.artist)
    
    def test_song_has_genre(self):
        self.assertEqual("Rock", self.song_1.genre)