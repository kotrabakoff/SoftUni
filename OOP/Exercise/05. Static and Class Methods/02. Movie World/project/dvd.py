from project.month_mapper import month_mapper


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        separated = date.split(".")
        month = int(separated[1])
        year = int(separated[2])
        month_last = month_mapper[month]
        return cls(name, id, year, month_last, age_restriction)

    def __repr__(self):
        if self.is_rented:
            rented = "rented"
        else:
            rented = "not rented"

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented}"




