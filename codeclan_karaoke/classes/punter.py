from classes.person import Person
#inherits from person class 

class Punter(Person):

#init that extends parent class init and adds own attributes
    def __init__(self, fave_genre: str, fave_song: str, money: float, honesty: int, *args, **kwargs):
        
        #function that facilitates extention of init from parent class
        super(Punter, self).__init__(*args, **kwargs)

        self.fave_genre = fave_genre
        self.fave_song = fave_song
        self.money = money
        self.honesty = honesty
    