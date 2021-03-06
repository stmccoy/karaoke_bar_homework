from classes.people.person import Person
from classes.rooms.non_party_rooms import Toilet 
#all classes inherit from person class 

class Bouncer(Person):

    def check_id(self, punter_object):
        #checks punter's age prior to entering club
        if punter_object.age >= 18:
            return True
        return False
    
    def allow_in_room(self, room, punter_object):
        #gender check for toilet class
        if isinstance(room, Toilet):
            if punter_object.gender == room.gender and room.capacity != room.current_punter_total:
                return True
            return False
        #returns false if room is full 
        elif room.capacity == room.current_punter_total:
            return False
        return True

class KaraokeStaff(Person):

    def accept_song_request(self, punter_object, song_fee: int):
        #checks punter can afford to make a song request
        if punter_object.money - song_fee > 0:
            return True
        else:
            return False

class CheckInStaff(Person):

    def take_entrance_fee(self, punter_object, entrance_fee: int):
        #checks punter can afford entrance fee
        if (punter_object.money - entrance_fee) < 0:
            return False
        else:
            punter_object.pay_fee(entrance_fee)
            return True
    
    def room_assign(self, punter_object, rooms_list: list):
        for room in rooms_list:
            #checks that punter is going into room with genre they like, basically asking the punter where they want to be.
            if punter_object.fave_genre == room.genre:
                if room.current_punter_total == room.capacity:
                    room.queue.append(punter_object)
                else:
                    room.current_punter_total += 1
                    break
        else:
            return False
    
    

        
