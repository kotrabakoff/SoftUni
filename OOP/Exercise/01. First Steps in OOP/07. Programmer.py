class Programmer():
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills


    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if new_language != self.language and skills_needed <= self.skills:
            old_language = self.language
            self.language = new_language
            return F"{self.name} switched from {old_language} to {new_language}"
        elif new_language == self.language and skills_needed <= self.skills:
            return f"{self.name} already knows {self.language}"
        elif skills_needed > self.skills:
            return f"{self.name} needs {skills_needed - self.skills} more skills"

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
