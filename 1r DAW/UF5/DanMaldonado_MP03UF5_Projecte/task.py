"""
Tasca: representa una tasca que es pot gestionar dins d'un sistema de gestió de tasques. 
Atributs:
descripcio: Una cadena que conté la descripció de la tasca.
datalimit: Un objecte datetime que indica la data límit per completar la tasca.
usuari: Una cadena que indica l'usuari o assignat a la tasca.
durada: Un enter que indica la durada estimada de la tasca, pot ser en hores o en alguna altra unitat de temps.
prioritat: Un enter o un valor enumerat que indica la prioritat de la tasca (per exemple, baixa, mitjana, alta).
realitzat: Un booleà que indica si la tasca ha estat completada o no.

__init__(self, descripcio, datalimit, usuari, durada, prioritat): Constructor de la classe. Inicialitza els atributs de la tasca amb els valors proporcionats.
marcar_completada(self): Un mètode que marca la tasca com a completada, establint el valor de l'atribut realitzat com a True.
actualitzar_datalimit(self, nou_datalimit): Un mètode per actualitzar la data límit de la tasca amb un nou valor.
actualitzar_usuari(self, nou_usuari): Un mètode per actualitzar l'usuari assignat a la tasca amb un nou valor.
actualitzar_prioritat(self, nova_prioritat): Un mètode per actualitzar la prioritat de la tasca amb un nou valor.
__str__(self): Un mètode que retorna una cadena amb la informació detallada de la tasca, incloent-hi la descripció, la data límit, l'usuari assignat, la durada estimada, la prioritat i l'estat de completada.

"""
from datetime import date

# data = datetime.now()
# print(data.strftime("%Y-%m-%dT%H:%M"))


class Task:

    def __init__(self, descripcio, datalimit, usuari, durada, prioritat="Baixa") -> None:
        self.descripcio = descripcio
        self.datalimit = datalimit
        self.usuari = usuari
        self.durada = durada
        self.prioritat = prioritat
        self.realitzat = False

    def marcar_completada(self):
        self.realitzat = True

    def actualitzar_data_limit(self, nova_data):
        self.datalimit = nova_data

    def actualitzar_usuari(self, nou_usuari):
        self.usuari = nou_usuari

    def actualitzar_prioritat(self, nova_prioritat):
        self.prioritat = nova_prioritat

    def __str__(self) -> str:

        

        descripcio = self.descripcio[0:28:] if len(self.descripcio)>=28 else self.descripcio+" "*(28-len(self.descripcio))
        prioritat = self.prioritat if len(self.prioritat)==7 else self.prioritat+" "*(7-len(self.prioritat))
        return f"\t{descripcio} \t{self.datalimit.strftime('%Y-%m-%d %H:%M')}\t {self.usuari[0:5:]} \t {self.durada} hores\t {prioritat}\t {'Si' if self.realitzat else 'No'}"
        
# prova
# data = date(2024,4,5)
# tasca = Tasca("Repas",data, "Pilar", 10)
# print(tasca)
# tasca.realitzat = True
# print(tasca)
