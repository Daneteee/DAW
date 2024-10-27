class Task:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(self.name + " se está executant.")
