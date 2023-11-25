class CropField:
    def __init__(self, field_id):
        self.field_id = field_id
        self.crop_history = {}

    def add_crop(self, year, crop):
        if year in self.crop_history:
            print(f"Поле {self.field_id} вже має інформацію про вирощувану культуру в {year} році.")
        else:
            self.crop_history[year] = crop
            print(f"Культура {crop} вирощена на полі {self.field_id} у {year} році.")

    def display_crop_info(self):
        print(f"Інформація про вирощувані культури на полі {self.field_id}:")
        for year, crop in sorted(self.crop_history.items()):
            print(f"{year}: {crop}")


class Farm:
    def __init__(self, verbose=True):
        self.fields = {}
        self.verbose = verbose

    def add_field(self, field_id):
        if field_id not in self.fields:
            self.fields[field_id] = CropField(field_id)
            if self.verbose:
                print(f"Створено нове поле сільськогосподарського підприємства з ідентифікатором {field_id}.")
        else:
            if self.verbose:
                print(f"Поле з ідентифікатором {field_id} вже існує.")

    def choose_crop(self, field_id, year):
        if field_id in self.fields:
            current_field = self.fields[field_id]
            if year in current_field.crop_history:
                if self.verbose:
                    print(f"На полі {field_id} вже вирощена культура у {year} році.")
            else:
                available_crops = self.get_available_crops(field_id, year)
                if available_crops:
                    if self.verbose:
                        print(f"Доступні культури для вирощування на полі {field_id} у {year} році:")
                        for crop in available_crops:
                            print(crop)
                    chosen_crop = input("Виберіть культуру для вирощування: ")
                    current_field.add_crop(year, chosen_crop)
                else:
                    if self.verbose:
                        print("На жаль, немає доступних культур для вирощування на цьому полі.")
        else:
            if self.verbose:
                print(f"Поле з ідентифікатором {field_id} не існує.")

    def get_available_crops(self, field_id, year):
        if field_id in self.fields:
            current_field = self.fields[field_id]
            previous_year = year - 1 if year - 1 in current_field.crop_history else None
            if previous_year:
                previous_crop = current_field.crop_history[previous_year]
                if previous_crop == "Пшениця":
                    return ["Ячмінь", "Кукурудза", "Гречка"]
            else:
                return ["Пшениця", "Ячмінь", "Кукурудза", "Гречка"]
        return []

    def edit_crop_info(self, field_id, year, new_crop):
        if field_id in self.fields:
            current_field = self.fields[field_id]
            if year in current_field.crop_history:
                current_field.crop_history[year] = new_crop
                if self.verbose:
                    print(f"Інформацію про вирощувану культуру на полі {field_id} у {year} році відредаговано.")
            else:
                if self.verbose:
                    print(f"На полі {field_id} не було вирощено культуру у {year} році.")
        else:
            if self.verbose:
                print(f"Поле з ідентифікатором {field_id} не існує.")

farm = Farm()

while True:
    print("\nМеню:")
    print("1. Додати поле")
    print("2. Вибрати культуру для поля на певний рік")
    print("3. Відредагувати інформацію про вирощену культуру")
    print("4. Вийти")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        field_id = input("Введіть ідентифікатор поля: ")
        farm.add_field(field_id)
    elif choice == "2":
        field_id = input("Введіть ідентифікатор поля: ")
        year = int(input("Введіть рік: "))
        farm.choose_crop(field_id, year)
    elif choice == "3":
        field_id = input("Введіть ідентифікатор поля: ")
        year = int(input("Введіть рік: "))
        new_crop = input("Введіть нову культуру: ")
        farm.edit_crop_info(field_id, year, new_crop)
    elif choice == "4":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
