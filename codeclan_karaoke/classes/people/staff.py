from classes.people.person import Person
from classes.people.punter import Punter
#all classes inherit from person class 

class Bouncer(Person):

    def check_id(self, punter: Punter):
        if punter.age >= 18:
            return True
        return False
    
    def allow_in_room(self, room, punter=None):
        if room.capacity == room.current_punter_total:
            return False
        # elif isinstance(room, Toilet):
        #     if punter.gender == room.gender:
        #         return True
        #     return False
        return True

class KaraokeStaff(Person):

    def accept_song_request(self, punter: Punter, song_fee: int):
        if punter.money - song_fee > 0:
            return True
        else:
            return False

class CheckInStaff(Person):

    def take_entrance_fee(self, punter: Punter, entrance_fee: int):
        if (punter.money - entrance_fee) < 0:
            return False
        else:
            punter.pay_fee(entrance_fee)
            return True
    
    def room_assign(self, punter: Punter, rooms_list: list):
        for room in rooms_list:
            if punter.fave_genre == room.genre:
                if room.current_punter_total == room.capacity:
                    room.queue.append(punter)
                else:
                    room.current_punter_total += 1
                    break
    
    

        
