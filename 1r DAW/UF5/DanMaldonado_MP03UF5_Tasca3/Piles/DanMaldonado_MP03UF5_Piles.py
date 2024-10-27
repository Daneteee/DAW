from stack import Stack

def check_parenthesis(string):
    parenthesis_stack = Stack()
    for character in string:
        if character == "(":
            parenthesis_stack.push(character)
        elif character == ")" and not parenthesis_stack.is_empty():
            parenthesis_stack.pop()

    return parenthesis_stack.is_empty()


def reverse_string(string):
    reversed_stack = Stack()
    reversed_string = ""
    for character in string:
        reversed_stack.push(character)

    while not reversed_stack.is_empty():
        reversed_string += reversed_stack.pop()

    return reversed_string


def reverse_sentence(sentence):
    reversed_sentence = ""
    current_word = ""

    for character in sentence:
        if character != " ":
            current_word += character
        else:
            reversed_word = reverse_string(current_word)
            reversed_sentence += reversed_word + " "
            current_word = ""

    if current_word != "":
        reversed_word = reverse_string(current_word)
        reversed_sentence += reversed_word

    return reversed_sentence


def postfix_expression(expression):
    stack = Stack()
    for character in expression:
        if type(character) is int:
            stack.push(character)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = eval(f"{operand2}{character}{operand1}")
            print(f"{operand1} {character} {operand2} = {result}")
            stack.push(result)
