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
        #karoake staff class method that confirms punter has enough money
        if karaoke_staff_object.accept_song_request(self, song_fee):
            self.money -= song_fee 
            return True
        return False
    
    def change_room(self, room__object_from, room_object_to, bouncer):
        #bouncer class method that checks amount of people in room to see if there is space
        if bouncer.allow_in_room(room_object_to, self):
            room__object_from.current_punter_total -= 1
            room_object_to.current_punter_total += 1
        elif isinstance(room_object_to, Toilet):
            #gender check for toilet class
            if room_object_to.gender != self.gender:
                return False
            #adds punter class to queue for room if room full
            elif room_object_to.capacity == room_object_to.current_punter_total:
                room__object_from.current_punter_total -= 1
                room_object_to.queue.append(self)
        else:
            #adds punter class to queue for room
            room__object_from.current_punter_total -= 1
            room_object_to.queue.append(self)
    
    def go_home(self, room_in_object):
        #subtacts 1 from the current punter total of room object
        room_in_object.current_punter_total -= 1
    
    def shout(self, room_in_object):
        if self.fave_song == room_in_object.song_playing:
            return "OMG I LOVE THIS SONG!!!"
        return "WOOP WOOP"


        
        
    