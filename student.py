class Student:
    __slots__ = ["name","tasks"]
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def to_string(self):
        return f"Student Name: {self.name}<br>Topic Covered: {self.tasks}"