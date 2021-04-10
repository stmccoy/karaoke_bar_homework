from classes.people.staff import *
from classes.people.punter import Punter
from classes.rooms.room import Room
#classes inherit from room class

class Toilet(Room):
    pass

class SmokingArea(Room):
    pass

class CheckInRoom(Room):
    #init that extends parent class init and adds own attributes
    def __init__(self, entrance_fee :int, *args, **kwargs):
        
        #function that facilitates extention of init from parent class
        super(CheckInRoom, self).__init__(*args, **kwargs)
    
        self.entrance_fee = entrance_fee
    
    def admit_punter(self, punter: Punter, bouncer: Bouncer, check_in_staff : CheckInStaff, entrance_fee: int, party_rooms_list: list):
        if bouncer.check_id(punter) == "Sling your hook pal":
            return bouncer.check_id(punter)
        else:
            if check_in_staff.take_entrance_fee(punter, entrance_fee) == "Not enough money, sorry":
                return check_in_staff.take_entrance_fee(punter, entrance_fee)
            else:
                check_in_staff.room_assign(punter, party_rooms_list)




