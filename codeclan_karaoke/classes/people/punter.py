from classes.people.person import Person
from classes.songs.song import Song
#inherits from person class 

class Punter(Person):

#init that extends parent class init and adds own attributes
    def __init__(self, fave_genre: str, fave_song: str, money: float, honesty: int, *args, **kwargs):
        
        #function that facilitates extention of init from parent class
        super(Punter, self).__init__(*args, **kwargs)

        self.fave_genre = fave_genre
        self.fave_song = fave_song
        self.money = money
        self.honesty = honesty
    
    def pay_fee(self, fee:int):
        self.money -= fee
    
    def request_song(self, karaoke_staff, song: Song, song_fee: int):
        if karaoke_staff.accept_song_request(self, song_fee):
            self.money -= song_fee 
            return True
        return False
        
        
    