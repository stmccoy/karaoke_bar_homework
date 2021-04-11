from classes.people.person import Person
from classes.songs.song import Song
from classes.rooms.non_party_rooms import Toilet
#inherits from person class 

class Punter(Person):

#init that extends parent class init and adds own attributes
    def __init__(self, fave_genre: str, fave_song: str, money: float, *args, **kwargs):        
        #function that facilitates extention of init from parent class
        super(Punter, self).__init__(*args, **kwargs)
        self.fave_genre = fave_genre
        self.fave_song = fave_song
        self.money = money
    
    def pay_fee(self, fee:int):
        self.money -= fee
    
    def request_song(self, karaoke_staff, song: Song, song_fee: int):
        if karaoke_staff.accept_song_request(self, song_fee):
            self.money -= song_fee 
            return True
        return False
    
    def change_room(self, room_from, room_to, bouncer):
        if bouncer.allow_in_room(room_to, self):
            room_from.current_punter_total -= 1
            room_to.current_punter_total += 1
        elif isinstance(room_to, Toilet):
            if room_to.gender != self.gender:
                return False
            elif room_to.capacity == room_to.current_punter_total:
                room_from.current_punter_total -= 1
                room_to.queue.append(self)
        else:
            room_from.current_punter_total -= 1
            room_to.queue.append(self)
    
    def go_home(self, room_in):
        room_in.current_punter_total -= 1


        
        
    