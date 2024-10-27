# Crea una classe anomenada QuizBrain, en l’arxiu quiz_brain.py. Fes el constructor on incialitzes els atributs
# question_number a 0 i question_list a una llista de preguntes que li passarem per paràmetre (question_bank).

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Fes el mètode next_question a la classe QuizBrain per poder accedir a la pregunta. Aquest mètode ha d’accedir a
    # la question_number, que té l'índex de la pregunta actual, i ha de mostrar el “text” de la pregunta per la qual
    # volem demanar una resposta, després demanarà l’usuari que introdueixi una resposta per la pregunta formulada,
    # finalment incrementa l’atribut question_number. Aquest mètode retorna la resposta de l’usuari.
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return user_answer

    # Fes un mètode a la classe QuizBrain anomenat still_have_question() que retornarà un booleà true si encara hi ha
    # preguntes per mostrar i false si ja ha mostrat totes les preguntes.
    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    # Afegeix l’atribut score a la classe QuizBrain i el mètode check_answer(), cada vegada que encerti una pregunta s
    # core s’incrementarà i mostrarà missatge corresponent. Paràmetre, la resposta de l’usuari
    def check_answer(self, answer):
        answers = {"True": ["T", "TRUE", "S", "SI", "YES"], "False": ["F", "FALSE", "N", "NO"]}

        answer = "True" if answer.upper() in answers["True"] else "False"

        if answer == self.question_list[self.question_number - 1].answer:
            self.score += 1
            print("Molt bé! Resposta correcta!!")
            print(f"Punts: {self.score}/{self.question_number}")
        else:
            print("Resposta incorrecta... :(")
            print(f"Punts: {self.score}/{self.question_number}")

    # Finalment: Informa del resultat a l'usuari. Fes el mètode final_result a la classe QuizBrain
    def final_result(self):
        print(f"Has acabat! Has obtingut {self.score}/{self.question_number} punts!")
