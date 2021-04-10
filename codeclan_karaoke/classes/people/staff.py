from classes.people.person import Person
from classes.people.punter import Punter
#all classes inherit from person class 

class Bouncer(Person):

    def check_id(self, punter: Punter):
        if punter.age >= 18:
            return "On you go mate"
        return "Sling your hook pal"

class KaraokeStaff(Person):

    pass

class CheckInStaff(Person):

    def take_entrance_fee(self, punter: Punter, entrance_fee: int):
        if (punter.money - entrance_fee) < 0:
            return "Not enough money, sorry"
        else:
            punter.pay_fee(entrance_fee)
            return "Thank You"
    
    def room_assign(self, punter: Punter, room_list: list):
        pass

        
