from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def check_value(self, value, iter):
        for val in iter:
            if val.name == value:
                return val
        return

    def check_type(self, value, iter):
        for val in iter:
            if val.race_type == value:
                return val
        return

    def check_reversed(self, value, iter):
        for val in reversed(iter):
            if val.__class__.__name__ == value:
                if not val.is_taken:
                    return val
                return
        return

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type == "Appaloosa" or horse_type == "Thoroughbred":
            horse = self.check_value(horse_name, self.horses)
            if horse:
                raise Exception(f"Horse {horse_name} has been already added!")
            if horse_type == "Appaloosa":
                horse = Appaloosa(horse_name, horse_speed)
            elif horse_type == "Thoroughbred":
                horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        jockey = self.check_value(jockey_name, self.jockeys)
        if jockey in self.jockeys:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        horserace = self.check_type(race_type, self.horse_races)
        if horserace:
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):
        horse = self.check_reversed(horse_type, self.horses)
        jockey = self.check_value(jockey_name, self.jockeys)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.has_horse:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = horse
        jockey.has_horse = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        horserace = self.check_type(race_type, self.horse_races)
        jockey = self.check_value(jockey_name, self.jockeys)
        if not horserace:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.has_horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        for horserace in self.horse_races:
            if jockey in horserace.jockeys:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horserace.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        horserace = self.check_type(race_type, self.horse_races)
        if not horserace:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horserace.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        current_fastest = 0
        for jockey in horserace.jockeys:
            if jockey.horse.speed > current_fastest:
                winner = jockey
                current_fastest = jockey.horse.speed
        return f"The winner of the {race_type} race, with a speed of {current_fastest}km/h is {winner.name}! Winner's horse: {winner.horse.name}."






