class TaskManager:

    def __init__(self) -> None:
        self.tasques = []

    def afegir_tasca(self, tasca):
        self.tasques.append(tasca)

    def eliminar_tasca(self, tasca):
        self.tasques.remove(tasca)

    def marcar_completada(self,tasca):
        tasca.marcar_completada()

    def obtenir_tasques_per_usuari(self, usuari):
        return [tasca for tasca in self.tasques if tasca.usuari == usuari]
    
    def obtenir_tasques_per_prioritat(self, prioritat):
        return [tasca for tasca in self.tasques if tasca.prioritat == prioritat]
    
    def obtenir_tasques_per_datalimit(self, datalimit):
        return [tasca for tasca in self.tasques if tasca.datalimit < datalimit]
    
    def obtenir_tasques_pendents(self):
        return [tasca for tasca in self.tasques if not tasca.realitzat]
    
    
    def retorna_tasca(self, i):
        return self.tasques[i]
    

