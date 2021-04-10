from classes.rooms.room import Room
from classes.songs.song import Song
#class inherits from room class

class PartyRoom(Room):
    #init that extends parent class init and adds own attributes
    def __init__(self, genre: str,*args, **kwargs):       
        #function that facilitates extention of init from parent class
        super(PartyRoom, self).__init__(*args, **kwargs)
        self.genre = genre
        self.song_list = [
            Song("Gotta Get Thru This", "Daniel Beddingfield", "Pop"),
            Song("Hit Me Baby One More Time", "Britney Spears", "Pop"),
            Song("What I Go To School For", "Busted", "Pop"),
            Song("Tragedy", "Steps", "Pop"),
            Song("Deeper Shade Of Blue", "Steps", "Pop"),
            Song("American Idiot", "Green Day", "Rock"),
            Song("The Pretender", "Foo Fighters", "Rock"),
            Song("Welcome To The Black Parade", "My Chemical Romance", "Rock"),
            Song("Supermassive Black Hole", "Muse", "Rock"),
            Song("The Anthem", "Good Charlotte", "Rock"),
            Song("Yeah", "Usher", "RnB"),
            Song("Tispy", "J-Kwon", "RnB"),
            Song("I've Got A Feeling", "Black Eyed Peas", "RnB"),
            Song("Rehab", "Rihanna", "RnB"),
            Song("Single Ladies", "Beyonce", "RnB")
        ]
        self.song_playing = None

    def play_song(self, song, punter, karaoke_staff, song_fee):
        if punter.request_song(karaoke_staff, song, song_fee):
            self.song_playing = song



