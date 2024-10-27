import sys
import random
from data import *
from question_model import Question
from quiz_brain import QuizBrain

menu = ["Question_data", "Science", "Geography", "History", "General", "Random_Facts"]


def generar_question_bank(q_d):
    q_d = [Question(q["text"], q["answer"]) for q in q_d]
    return q_d


def print_menu(menu):
    """Mostra les entrades de la tupla "menu" afegint el nombre
    corresponent i l'entrada "SORTIR" al final."""
    mida = len(menu)
    print("\nBancs\n--------------------")
    for i in range(len(menu)):
        print(f"{i + 1}. {str(menu[i])}")
    print(f"{mida + 1}. SORTIR")


def main():
    # Verifica que haya 1 solo argumento o que el segundo sea -T
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "-T"):
        question_bank = generar_question_bank(random.choice(question_banks))

        if len(sys.argv) == 2:
            if sys.argv[1] == "-T":
                sortir = False
                while not sortir:
                    print_menu(menu)

                    eleccio = None
                    while eleccio not in range(1, len(question_banks) + 1):
                        try:
                            eleccio = int(input("Selecciona un banc: "))
                        except ValueError:
                            print("ERROR: Entrada invàlida.")

                    question_bank = generar_question_bank(question_banks[eleccio - 1])
                    sortir = True
            else:
                print("ERROR: Argument invàlid.")

        joc = QuizBrain(question_bank)

        while joc.still_have_questions():
            resposta = joc.next_question()
            joc.check_answer(resposta)

        joc.final_result()
    else:
        print("ERROR: Arguments invàlids.")


if __name__ == '__main__':
    main()
