from fitxaInformacio import FitxaInformacio


class FitxaClient(FitxaInformacio):
    def __init__(self, client):
        super().__init__(client)
