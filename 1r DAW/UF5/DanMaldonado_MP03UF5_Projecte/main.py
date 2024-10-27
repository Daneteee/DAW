from taskmanager import TaskManager  # type: ignore
from task import Task
from tascaprogramacio import TascaProgramacio  # type: ignore
from tasks import dades_tasques  # type: ignore
from datetime import datetime


def menu():
    menu = {
        1: "Afegir Tasca",
        2: "Eliminar Tasca",
        3: "Completar Tasca",
        4: "Llistar Tasques Usuari",
        5: "Llistar Tasques Prioritat",
        6: "Llistar tasques Data límit",
        7: "Llistar Tasques Pendents",
        8: "Llistar TOTES les Tasques",
        0: "Sortir"
    }
    print("\n MENU\n ============")
    for k in menu:
        print(k, menu[k])
    ok = False
    while not ok:
        op = int(input("Tria opcio: "))
        ok = op in menu.keys()

    return op


def afegir_tasca(gestor):
    print("Afegir Tasca")
    print("==============")

    descripcio = input("Descripció de la tasca: ")
    datalimit = input("Datalimit format dd/mm/YYYY hh:mm: ")
    datalimit = datetime.strptime(datalimit, "%d/%m/%Y %H:%M")
    usuari = input("Usauari: ")
    durada = int(input("Durada:"))
    prioritat = input("Prioritat Baixa/Mitja/Alta: ")
    tasca = Task(descripcio, datalimit, usuari, durada, prioritat)
    gestor.afegir_tasca(tasca)


def llistat_tasques(llista_tasques):
    print("Llistat tasques")
    print("ID\tDescripció\t\t\tData Límit\t\tUsuari\tDurada:hores\tPriotitat\tRealitzada ")
    print(
        "=====================================================================================================================")
    for i in range(len(llista_tasques)):
        print(i, llista_tasques[i])


def eliminar_tasca(gestor):
    llistat_tasques(gestor.tasques)
    i = int(input("Quina tasca vols eliminar ?"))
    tasca = gestor.retorna_tasca(i)
    gestor.eliminar_tasca(tasca)


def completar_tasca(gestor):
    llistat_tasques(gestor.tasques)
    i = int(input("Quina tasca vols completar ?"))
    tasca = gestor.retorna_tasca(i)
    gestor.marcar_completada(tasca)


def llistar_tasques_usuari(gestor):
    usuari = input("Quin usuari vols mostrar les tasques ?")
    llista_tasques = gestor.obtenir_tasques_per_usuari(usuari)
    llistat_tasques(llista_tasques)


def llistar_tasques_prioritat(gestor):
    prioritat = input("Quina prioritat vols mostrar les tasques ?")
    llista_tasques = gestor.obtenir_tasques_per_prioritat(prioritat)
    llistat_tasques(llista_tasques)


def llistar_tasques_datalimit(gestor):
    datalimit = input("Quina data límit vols fixar, (es mostraran les tasques anteriors) dd/mm/YYYY?")
    datalimit = datetime.strptime(datalimit, "%d/%m/%Y")

    llista_tasques = gestor.obtenir_tasques_per_datalimit(datalimit)
    llistat_tasques(llista_tasques)


def llistar_tasques_pendents(gestor):
    llista_tasques = gestor.obtenir_tasques_pendents()
    llistat_tasques(llista_tasques)


def llistar_totes_les_tasques(gestor):
    llista_tasques = gestor.tasques
    llistat_tasques(llista_tasques)


def importar_tasques(gestor):
    for d_tasca in dades_tasques:
        tasca = Task(d_tasca["descripcio"], d_tasca["datalimit"], d_tasca["usuari"], d_tasca["durada"],
                     d_tasca["prioritat"])
        gestor.afegir_tasca(tasca)


def main():
    gestor = TaskManager()
    importar_tasques(gestor)

    sortir = False
    while not sortir:
        op = menu()
        if op == 1:
            afegir_tasca(gestor)
        elif op == 2:
            eliminar_tasca(gestor)
        elif op == 3:
            completar_tasca(gestor)
        elif op == 4:
            llistar_tasques_usuari(gestor)
        elif op == 5:
            llistar_tasques_prioritat(gestor)
        elif op == 6:
            llistar_tasques_datalimit(gestor)
        elif op == 7:
            llistar_tasques_pendents(gestor)
        elif op == 8:
            llistar_totes_les_tasques(gestor)
        elif op == 0:
            sortir = True


if __name__ == "__main__":
    main()
