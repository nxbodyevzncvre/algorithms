import string
import secrets


def generate_password():
    combination = string.ascii_lowercase + string.digits

    length = int(input("Type the length of your password: "))
    symbols = input(
        "Wish you to add any symbols to your password?(type + if you want) ")
    uppercase = input(
        "Wish you add any upper case symbols to your password?(type + if you want) ")

    if symbols == "+":
        combination += string.punctuation
    else:
        combination += string.pu

    if uppercase == "+":
        combination += string.ascii_uppercase
    else:
        combination += string.ascii_lowercase

    combination_length = len(combination)

    new_password = ""

    for empty in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password


print(generate_password())
