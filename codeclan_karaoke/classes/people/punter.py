from classes.people.person import Person
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
    
    def request_song(self, karaoke_staff_object, song_object, song_fee: int):
        if karaoke_staff_object.accept_song_request(self, song_fee):
            self.money -= song_fee 
            return True
        return False
    
    def change_room(self, room__object_from, room_object_to, bouncer):
        if bouncer.allow_in_room(room_object_to, self):
            room__object_from.current_punter_total -= 1
            room_object_to.current_punter_total += 1
        elif isinstance(room_object_to, Toilet):
            if room_object_to.gender != self.gender:
                return False
            elif room_object_to.capacity == room_object_to.current_punter_total:
                room__object_from.current_punter_total -= 1
                room_object_to.queue.append(self)
        else:
            room__object_from.current_punter_total -= 1
            room_object_to.queue.append(self)
    
    def go_home(self, room_in_object):
        room_in_object.current_punter_total -= 1
    
    def shout(self, room_in_object):
        if self.fave_song == room_in_object.song_playing:
            return "OMG I LOVE THIS SONG!!!"
        return "WOOP WOOP"


        
        
    