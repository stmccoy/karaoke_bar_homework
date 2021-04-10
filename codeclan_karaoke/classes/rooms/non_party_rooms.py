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

