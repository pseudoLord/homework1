def corrector(string, width, symbol):
    if len(symbol) != 1:
        raise ValueError("Символ-заповнювач повинен бути лише одним символом.")
    if width < len(string):
        return string
    return string.center(width, symbol)

user_string = input("Введіть текст: ")
user_width = int(input("Введіть загальну ширину: "))
user_symbol = input("Введіть символ-заповнювач: ")

try:
    result = corrector(user_string, user_width, user_symbol)
    print("Відформатований текст:", result)
except ValueError as e:
    print("Помилка:", e)
