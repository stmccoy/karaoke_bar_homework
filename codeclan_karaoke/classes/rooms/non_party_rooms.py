# from classes.people.staff import *
# from classes.people.punter import Punter
from classes.rooms.room import Room
#classes inherit from room class

class Toilet(Room):
    #init that extends parent class init and adds own attributes
    def __init__(self, gender, *args, **kwargs):       
        #function that facilitates extention of init from parent class
        super(Toilet, self).__init__(*args, **kwargs)
        self.gender = gender

class SmokingArea(Room):
    pass

class CheckInRoom(Room):
    #init that extends parent class init and adds own attributes
    def __init__(self, entrance_fee :int, *args, **kwargs):       
        #function that facilitates extention of init from parent class
        super(CheckInRoom, self).__init__(*args, **kwargs)
        self.entrance_fee = entrance_fee
    
    def admit_punter(self, punter, bouncer, check_in_staff, entrance_fee: int, party_rooms_list: list):
        if not bouncer.check_id(punter):
            return bouncer.check_id(punter)
        else:
            if not check_in_staff.take_entrance_fee(punter, entrance_fee):
                return check_in_staff.take_entrance_fee(punter, entrance_fee)
            else:
                check_in_staff.room_assign(punter, party_rooms_list)




