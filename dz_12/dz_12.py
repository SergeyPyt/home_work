class Human:
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def full_name(self):
        return f"Полное имя : {self.name} {self.surname}"

    def get_age(self):
        return f"Возраст: {self.birth_year}"


hum_1 = Human("Bob", "Carter", 18)

print(hum_1.full_name(), hum_1.get_age(), sep="\n")
