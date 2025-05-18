import datetime

def birthday_weekdays():
    day = int(input("Введіть день народження (1–31): "))
    month = int(input("Введіть місяць народження (1–12): "))

    print(f"\nDate: {day:02d}.{month:02d}\n")

    current_year = datetime.datetime.now().year

    for year in range(current_year, current_year + 20):
        try:
            birthday = datetime.date(year, month, day)
            day_name = birthday.strftime("%A")
            print(f"{birthday.strftime('%d.%m.%Y')} — {day_name}")
        except ValueError:
            print(f"{day:02d}.{month:02d}.{year} — Неприпустима дата")


birthday_weekdays()
