# Fes una funció per sumar els dígits d’un nombre sencer positiu utilitzant recursivitat.
def sum_digits(n):
    assert 0 <= n == int(n), 'Ha de ser un nombre enter'
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


# Calcula la potència n d’un nombre sencer positiu utilitzant recursivitat.
def power_of(base, exp):
    assert 0 <= base == int(base) and 0 <= exp == int(exp), 'Ha de ser un nombre enter'
    if exp == 0:
        return 1
    return base * power_of(base, exp - 1)


# Fes una funció recursiva per girar un string
def reverse_string(string):
    assert isinstance(string, str), "Ha de ser de tipus string."
    if len(string) == 1:
        return string
    return reverse_string(string[1::]) + string[0]


# Passa un nombre sencer positiu a binari utilitzant recursivitat
def int_to_binary(n):
    assert 0 <= n == int(n), 'Ha de ser un nombre enter'
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return f"{int_to_binary(n // 2)}{n % 2}"


# Fes la funció de comprovació de palíndrom utilitzant recursivitat
def is_palindrome(string):
    assert isinstance(string, str), "Ha de ser de tipus string."
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


# Fes una funció per comptar totes les aparicions d’un caràcter específic en un string
def char_count(string, char, index=0):
    assert isinstance(char, str) and isinstance(string, str), "1r i 2n paràmetres han de ser de tipus string."
    if index >= len(string):
        return 0
    else:
        return (1 if char == string[index] else 0) + char_count(string, char, index + 1)


# def char_count(string, char, index=0, c=0):
#     assert isinstance(char, str) and isinstance(string, str), "1r i 2n paràmetres han de ser de tipus string."
#     if index >= len(string):
#         return c
#     else:
#         return char_count(string, char, index + 1, c + (1 if char == string[index] else 0))

# Fes una funció per sumar tots els elements d’una llista recursivament.
def sum_list(list_):
    assert all(isinstance(i, int) for i in list_), "Tots els elements han de ser de tipus enter."
    if len(list_) == 0:
        return 0
    return list_[0] + sum_list(list_[1:])


print(is_palindrome("aaaa"))