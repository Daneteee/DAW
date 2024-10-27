from datetime import datetime


class Command:

    # Es genera un identificador únic per a cada instància de la classe. Aquest identificador es genera concatenant el
    # prefix "c_" amb la data i l'hora actuals en un format específic. El format de data i hora utilitzat és
    # %y%m%d%H%M%S%f, que representa l'any, mes, dia, hora, minut, segon i microsegon.
    def __init__(self):
        self._id = "c_" + datetime.now().strftime("%y%m%d%H%M%S%f")
