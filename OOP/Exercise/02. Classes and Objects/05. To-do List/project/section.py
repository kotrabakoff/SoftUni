class Section():
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(task)
        return f"Task {task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"
    #
    # def clean_task(self):
    #     removed_counter = 0
    #     for task in self.tasks:
    #         if task.completed:
    #             self.tasks.remove(task)
    #             removed_counter += 1
    #     return f"Cleared {removed_counter} tasks"

    def clean_section(self):
        initial_size = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f"Cleared {initial_size - len(self.tasks)} tasks."

    def view_section(self):
        text_to_return = f"Section {self.name}:"
        for task in self.tasks:
            text_to_return += '\n' + task.details()
        return text_to_return

