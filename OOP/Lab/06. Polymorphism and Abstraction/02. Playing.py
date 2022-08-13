def start_playing(instrument):
    return instrument.play()


class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))
