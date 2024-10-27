from queue_ import Queue_


class TaskManager:
    def __init__(self):
        self.tasks_queue = Queue_()

    def add_task(self, task):
        # Afegim la tasca a la cua de tasques
        self.tasks_queue.enqueue(task)
        print(f"Tasca {task.name} afegida.")

    def execute_all(self):
        # Executem totes les tasques de la cua
        while not self.tasks_queue.is_empty():
            task = self.tasks_queue.dequeue()
            task.execute()

    def execute_oldest(self):
        # Executem la tasca més antiga de la cua
        if not self.tasks_queue.is_empty():
            oldest_task = self.tasks_queue.dequeue()
            oldest_task.execute()

    def print_tasks(self):
        # Imprimim les tasques de la cua
        self.tasks_queue.traverse_forward()
