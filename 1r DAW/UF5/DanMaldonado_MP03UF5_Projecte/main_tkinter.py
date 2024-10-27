from tkinter import *
import tkinter.messagebox as messagebox

from taskmanager import TaskManager
from task import Task
from datetime import datetime
from tasks import dades_tasques  # type: ignore


class App:

    def __init__(self, master):

        self.task_manager = TaskManager()
        self.import_tasks()

        self.master = master
        self.frame = None
        master.title("Gestor de tasques")
        master.minsize(width=1200, height=900)
        master.resizable(False, False)
        self.title_label = Label(self.master, text="Projecte UF5-Tkinter - Gestor de Tasques")
        self.title_label.pack(pady=10)

        # Creem el botó de llistar
        self.list_button = Button(self.master, text="Llistar TOTES les Tasques", width=25, height=2,
                                  command=self.list_all_tasks)
        self.list_button.pack(pady=10)

        # Creem el botó d'afegir tasca
        self.add_button = Button(self.master, text="+ Afegir tasca", width=25, height=2,
                                 command=self.manage_task, fg="green")
        self.sort_reversed = False

    # Importem les tasques al gestor de tasques
    def import_tasks(self):
        for d_tasca in dades_tasques:
            task = Task(
                d_tasca["descripcio"],
                d_tasca["datalimit"],
                d_tasca["usuari"],
                d_tasca["durada"],
                d_tasca["prioritat"])
            self.task_manager.afegir_tasca(task)

    # Llistem totes els tasques
    def list_all_tasks(self):
        # Eliminem el botó de llistar
        self.list_button.pack_forget()

        # Mostrem el botó d'afegir tasca
        self.add_button.pack(side=BOTTOM, pady=10)

        # Creem el frame
        self.frame = Frame(self.master)

        # button_data = [
        #     ("Descripció", 10, "descripcio", 0, 70),
        #     ("Data Limit", 7, "datalimit", 1, 20),
        #     ("Usuari", 5, "usuari", 2, 10),
        #     ("Durada (hores)", 12, "durada", 3, 10),
        #     ("Prioritat", 6, "prioritat", 4, 10)
        # ]
        #
        # for text, width, field, column, padx in button_data:
        #     button = Button(self.frame, text=text, width=width, height=1,
        #                     command=lambda field=field: self.sort_tasks(field))
        #     button.grid(column=column, row=0, padx=padx)
        #
        # # Creem el títol de les opcions
        # labels_data = ["D", "E", "C"]
        # for i, text in enumerate(labels_data):
        #     label = Label(self.frame, text=text)
        #     label.grid(column=i + 5, row=0, padx=10)

        # Creem els botons d'ordenació
        description_button = Button(self.frame, text="Descripció", width=10, height=1,
                                    command=lambda field="descripcio": self.sort_tasks(field))
        description_button.grid(column=0, row=0, padx=70)

        date_button = Button(self.frame, text="Data Limit", width=7, height=1,
                             command=lambda field="datalimit": self.sort_tasks(field))
        date_button.grid(column=1, row=0, padx=20)

        user_button = Button(self.frame, text="Usuari", width=5, height=1,
                             command=lambda field="usuari": self.sort_tasks(field))
        user_button.grid(column=2, row=0, padx=10)

        duration_button = Button(self.frame, text="Durada (hores)", width=12, height=1,
                                 command=lambda field="durada": self.sort_tasks(field))
        duration_button.grid(column=3, row=0, padx=10)

        priority_button = Button(self.frame, text="Prioritat", width=6, height=1,
                                 command=lambda field="prioritat": self.sort_tasks(field))
        priority_button.grid(column=4, row=0, padx=10)

        # Creem el títol de les opcions
        delete_label = Label(self.frame, text="D")
        delete_label.grid(column=5, row=0, padx=10)

        edit_label = Label(self.frame, text="E")
        edit_label.grid(column=6, row=0, padx=10)

        confirm_button = Label(self.frame, text="C")
        confirm_button.grid(column=7, row=0, padx=10)

        # Mostrem cada camp de les tasques
        c_y = 1
        for task in self.task_manager.tasques:
            c_x = 0
            descripcio_label = Label(self.frame, text=task.descripcio, fg="gray" if task.realitzat else "black")
            descripcio_label.grid(column=c_x, row=c_y, padx=10, pady=10)
            c_x += 1

            datalimit_label = Label(self.frame, text=task.datalimit.strftime("%d/%m/%Y %H:%M"), fg="gray" if task.realitzat else "black")
            datalimit_label.grid(column=c_x, row=c_y, padx=5, )
            c_x += 1

            usuari_label = Label(self.frame, text=task.usuari, fg="gray" if task.realitzat else "black")
            usuari_label.grid(column=c_x, row=c_y, padx=5)
            c_x += 1

            durada_label = Label(self.frame, text=task.durada, fg="gray" if task.realitzat else "black")
            durada_label.grid(column=c_x, row=c_y, padx=5)
            c_x += 1

            prioritat_label = Label(self.frame, text=task.prioritat, fg="gray" if task.realitzat else "black")
            prioritat_label.grid(column=c_x, row=c_y, padx=5)
            c_x += 1

            # Creem els botons que gestionan la tasca
            delete_button = Button(self.frame, text="💣", width=1, height=1,
                                   command=lambda task_param=task: self.delete_task(task_param))
            delete_button.grid(column=c_x, row=c_y, padx=5)
            c_x += 1

            edit_button = Button(self.frame, text="🪄", width=1, height=1,
                                 command=lambda current_task=task: self.manage_task(True, current_task))

            edit_button.grid(column=c_x, row=c_y, padx=5) if not task.realitzat else None
            c_x += 1

            confirm_button = Button(self.frame, text="✔︎", width=1, height=1,
                                    command=lambda task_param=task: self.complete_task(task_param))
            confirm_button.grid(column=c_x, row=c_y, padx=5) if not task.realitzat else None

            c_x += 1
            c_y += 1

        self.frame.pack()

    # Ordenanem les taques
    def sort_tasks(self, field):
        """Funció que ordena la llista de tasques del task_manager

        Args:
            field (str): El camp pel qual volem ordenar la llista.
        """
        priority_values = {"Alta": 1, "Mitjana": 2, "Baixa": 3}

        if field == "prioritat":
            # En cas que sigui per prioritat ordenem pel nombre corresponent a aquesta prioritat
            self.task_manager.tasques.sort(key=lambda task: priority_values.get(task.__dict__[field]))
        else:
            self.task_manager.tasques.sort(key=lambda task: task.__dict__[field])

        # Si l'ordre d'ordenació és invers, invertim la llista
        if self.sort_reversed:
            self.task_manager.tasques.reverse()

        self.refresh_frame()

        # Canviem l'ordre d'ordenació
        self.sort_reversed = not self.sort_reversed

    # Actualitzem el frame que mostra les tasques
    def refresh_frame(self):
        # Eliminem el frame i tornem a llistar les tasques
        self.frame.destroy()
        self.list_all_tasks()

    # Eliminem una tasca
    def delete_task(self, task):
        """Eliminem la tasca pasada per paràmetre.

        Args:
            task (obj): Objecte tasca a eliminar.
        """
        self.task_manager.eliminar_tasca(task)
        self.refresh_frame()

    # Completar una tasca
    def complete_task(self, task):
        """Marquem la tasca pasada per paràmetre com a completada.

        Args:
            task (obj): Obcjecte tasca a marcar com a completat.
        """
        self.task_manager.marcar_completada(task)
        self.refresh_frame()

    # Edició o creació d'una tasca
    def manage_task(self, is_editing=False, task=None):
        """Aquesta funció crea una tasca en cas que no estiguem editant una. Si la estem
        editant, li passem la tasca a editar com a paràmetre per accedir als seus camps.

        Args:
            is_editing (bool, optional): True si estem editant. Defaults to False.
            task (obj, optional): La tasca a editar en cas que estiguem editant. Defaults to None.
        """
        
        # Creem la nova finestra
        secondary = Tk()
        secondary.title("Editar Tasca" if is_editing else "Afegir Tasca")
        secondary.minsize(width=400, height=300)
        secondary.resizable(False, False)

        # Creem les etiquetes i les entrades corresponents per cada camp
        description_entry = Entry(secondary, width=30)
        Label(secondary, text="Descripció de la tasca").pack(pady=10)
        description_entry.pack()

        limitdate_entry = Entry(secondary, width=30)
        Label(secondary, text="Data límit (dd/mm/YYYY hh:mm)").pack(pady=10)
        limitdate_entry.pack()

        user_entry = Entry(secondary, width=30)
        Label(secondary, text="Usuari").pack(pady=5)
        user_entry.pack()

        duration_entry = Entry(secondary, width=30)
        Label(secondary, text="Durada (hores)").pack(pady=10)
        duration_entry.pack()

        priority_entry = Entry(secondary, width=30)
        Label(secondary, text="Prioritat (Alta/Mitjana/Baixa)").pack(pady=10)
        priority_entry.pack()

        # En cas que estiguem editant fiquem els valors anteriors als entries per poder modificar-los.
        if is_editing:
            description_entry.insert(0, task.descripcio)
            limitdate_entry.insert(0, task.datalimit.strftime("%d/%m/%Y %H:%M"))
            user_entry.insert(0, task.usuari)
            duration_entry.insert(0, task.durada)
            priority_entry.insert(0, task.prioritat)
            
            # Eliminem la tasca que estem editant per no duplicar-la més endevant.
            self.task_manager.eliminar_tasca(task)

        # Creem el botó que crida a guardar la tasca i li passem un diccionari amb cada camp de la tasca.
        # El text que es mostra canvia depenent de si l'editem o afegim.
        Button(secondary, text="Editar tasca" if is_editing else "Afegir tasca",
               command=lambda: self.save_task(
                   {
                       "descripcio": description_entry.get().capitalize(),
                       "datalimit": limitdate_entry.get(),
                       "usuari": user_entry.get().capitalize(),
                       "durada": duration_entry.get(),
                       "prioritat": priority_entry.get().capitalize()
                   },
                   secondary
               )).pack(pady=10)

        secondary.mainloop()

    def save_task(self, data, window):
        """Comprovem que les dades de la nova tasca siguin correctes i l'afegim al gestor.

        Args:
            data (dict): Diccionari amb les dades de la tasca
            window (obj): La finestra corresponent.
        """
        # Comprovem que totes les dades siguin correctes
        valid_data = True
        try:
            data["datalimit"] = datetime.strptime(data["datalimit"], "%d/%m/%Y %H:%M")
        except:
            self.show_error("ERROR: Format incorrecte. El format ha de ser dd/mm/aaaa hh:mm")
            valid_data = False

        try:
            data["durada"] = int(data["durada"])
        except ValueError:
            self.show_error("ERROR: La durada ha de ser un nombre enter")
            valid_data = False

        priorities = ["Alta", "Mitjana", "Baixa"]
        if data["prioritat"] not in priorities:
            self.show_error("ERROR: La prioritat ha de ser Alta, Mitjana o Baixa")
            valid_data = False

        # Si totes les dades són correctes afegik la tasca al gestor de tasques.
        if valid_data:
            task = Task(
                data["descripcio"],
                data["datalimit"],
                data["usuari"],
                data["durada"],
                data["prioritat"])
            self.task_manager.afegir_tasca(task)
            self.refresh_frame()
        window.destroy()

    def show_error(self, text):
        """Mostrem un error a l'usuari.

        Args:
            text (str): Text de l'error
        """
        error_window = Tk()
        error_window.title("Error")
        error_window.minsize(width=300, height=100)
        error_window.resizable(False, False)
        Label(error_window, text="⛔ " + text, font=("Arial", 14, "bold"), pady=10, padx=10).pack(expand=True,
                                                                                                 fill="both")
        Button(error_window, text="Ok", command=error_window.destroy).pack(pady=10)
        error_window.mainloop()


def main():
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
