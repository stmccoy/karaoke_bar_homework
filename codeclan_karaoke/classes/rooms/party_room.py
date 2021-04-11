from classes.rooms.room import Room
#class inherits from room class

class PartyRoom(Room):
    #init that extends parent class init and adds own attributes
    def __init__(self, genre: str,*args, **kwargs):       
        #function that facilitates extention of init from parent class
        super(PartyRoom, self).__init__(*args, **kwargs)
        self.genre = genre
        self.song_playing = None

    def play_song(self, song_object, punter, karaoke_staff, song_fee):
        if punter.request_song(karaoke_staff, song_object, song_fee):
            self.song_playing = song_object



