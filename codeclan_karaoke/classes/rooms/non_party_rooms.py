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
    
    def admit_punter(self, punter_object, bouncer_object, check_in_staff_object, entrance_fee: int, party_rooms_list: list):
        #bouncer object method for checking punter age, returns boolean
        if not bouncer_object.check_id(punter_object):
            return bouncer_object.check_id(punter_object)
        else:
            #check_in_staff method for checking customer can afford entrance fee to bar, returns boolean
            if not check_in_staff_object.take_entrance_fee(punter_object, entrance_fee):
                return check_in_staff_object.take_entrance_fee(punter_object, entrance_fee)
            #check_in_staff method that assigns customer to room but checks we have a room that matches customer's favourite genre
            elif check_in_staff_object.room_assign(punter_object, party_rooms_list) != False:
                check_in_staff_object.room_assign(punter_object, party_rooms_list)
            #returning false means we have no room that matches customers favourite genre so customer should try another bar
            else:
                return False
            

                
            




