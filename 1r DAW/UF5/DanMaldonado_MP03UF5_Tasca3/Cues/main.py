from task import Task
from taskmanager import TaskManager
from menu import Menu



def main():
    functions = ["Afegir tasca", "Executar totes les tasques", "Executar una sola tasca", "Imprimir totes les tasques"]
    menu = Menu(functions)
    taskmanager = TaskManager()
    leave = False

    while not leave:
        menu.print_menu()
        choice = menu.get_choice()
        if choice == 1:
            task_name = input("Introdueix el nom de la tasca: ")
            task = Task(task_name)
            taskmanager.add_task(task)
        elif choice == 2:
            taskmanager.execute_all()
        elif choice == 3:
            taskmanager.execute_oldest()
        elif choice == 4:
            taskmanager.print_tasks()
        else:
            print("Sortint...!")
            leave = True


if __name__ == "__main__":
    main()
