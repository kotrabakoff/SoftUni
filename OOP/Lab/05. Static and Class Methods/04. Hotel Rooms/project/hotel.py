

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)


    # def take_room(self, room_number, people):
    #     for room in self.rooms:
    #         if room.number == room_number:
    #             if room.capacity >= people:
    #                 room.is_taken = True
    #                 room.capacity -= room.guests
    #                 room.guests = people
    #                 self.guests += people

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)



    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def status(self):
        frees = [str(room.number) for room in self.rooms if not room.is_taken]
        takens = [str(room.number) for room in self.rooms if room.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(frees)}\n" \
               f"Taken rooms: {', '.join(takens)}"

