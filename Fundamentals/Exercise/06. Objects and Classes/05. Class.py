class Class:
    students = []
    grades = []
    __students_count = 22
    def __init__(self, name):
        self.name = name

    def add_student(self, name, grade: float):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return f"{(sum(self.grades) / len(self.grades)):.2f}"

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {(sum(self.grades) / len(self.grades)):.2f}"

# Example:

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
print(a_class.get_average_grade())
a_class.add_student("Amy", 3.50)
print(a_class)

