class Task:
    def __init__(self, description, limit_date, user, duration, priority, completed):
        self.description = description
        self.limit_date = limit_date
        self.user = user
        self.duration = duration
        self.priority = priority
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def update_limit_date(self, new_limit_date):
        self.limit_date = new_limit_date

    def update_user(self, new_user):
        self.user = new_user

    def update_duration(self, new_duration):
        self.duration = new_duration

    def __str__(self):
        return f"""Tasca: {self.description}
    Data límit: {self.limit_date}
    Usuari assignat: {self.user}
    Durada estimada: {self.duration}
    Prioritat: {self.priority}
    Completada: {self.completed}"""
