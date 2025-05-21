import re


def validate_phone():
    phone = input("Введіть номер телефону у форматі +380XXXXXXXXX: ")
    pattern = r"^\+380\d{9}$"

    if re.match(pattern, phone):
        print(" Номер телефону правильний.")
    else:
        print(" Невірний формат номера телефону. Спробуйте ще раз.")


validate_phone()
