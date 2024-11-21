import json
import os

class Meter:
    def __init__(self, id, type, initial_reading=0):
        self.id = id
        self.type = type
        self.reading = initial_reading

    def update_reading(self, new_reading):
        if new_reading < self.reading:
            raise ValueError("New reading must be greater than the current reading.")
        self.reading = new_reading

    def get_reading(self):
        return self.reading

class MeterManager:
    def __init__(self, filename='meters.json'):
        self.filename = filename
        self.meters = self.load_meters()

    def load_meters(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_meters(self):
        with open(self.filename, 'w') as file:
            json.dump(self.meters, file)

    def add_meter(self, meter):
        self.meters[meter.id] = {'type': meter.type, 'reading': meter.get_reading()}
        self.save_meters()

    def update_meter(self, meter_id, new_reading):
        if meter_id in self.meters:
            meter = Meter(meter_id, self.meters[meter_id]['type'], self.meters[meter_id]['reading'])
            meter.update_reading(new_reading)
            self.meters[meter_id]['reading'] = meter.get_reading()
            self.save_meters()
        else:
            raise KeyError(f"Meter with ID {meter_id} not found.")

    def get_meter_reading(self, meter_id):
        if meter_id in self.meters:
            return self.meters[meter_id]['reading']
        else:
            raise KeyError(f"Meter with ID {meter_id} not found.")

def main():
    manager = MeterManager()

    while True:
        print("\nВиберіть опцію:")
        print("1. Додати лічильник")
        print("2. Оновити показник лічильника")
        print("3. Отримати показник лічильника")
        print("4. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            id = input("Введіть ID лічильника: ")
            type = input("Введіть тип лічильника: ")
            initial_reading = int(input("Введіть початковий показник: "))
            meter = Meter(id, type, initial_reading)
            manager.add_meter(meter)
            print(f"Лічильник з ID {id} додано.")

        elif choice == '2':
            id = input("Введіть ID лічильника для оновлення: ")
            new_reading = int(input("Введіть новий показник: "))
            try:
                manager.update_meter(id, new_reading)
                print(f"Показник лічильника з ID {id} оновлено.")
            except KeyError as e:
                print(e)

        elif choice == '3':
            id = input("Введіть ID лічильника для отримання показника: ")
            try:
                reading = manager.get_meter_reading(id)
                print(f"Показник лічильника з ID {id}: {reading}")
            except KeyError as e:
                print(e)

        elif choice == '4':
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
