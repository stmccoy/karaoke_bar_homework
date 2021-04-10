class Room:

    def __init__(self, queue: list, staff: list, capacity: int, current_punter_total: int, song_playing= None):
        self.queue = queue
        self.staff = staff
        self.capacity = capacity
        self.current_punter_total = current_punter_total
