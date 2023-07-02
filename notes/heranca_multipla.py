class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("O carro está ligado.")

    def stop(self):
        print("O carro está desligado.")


class Electric:
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def charge(self):
        print("O carro elétrico está sendo carregado.")


class HybridCar(Car, Electric):
    def __init__(self, brand, battery_level, fuel_level):
        super().__init__(brand)
        super().__init__(battery_level)
        self.fuel_level = fuel_level

    def drive(self):
        print("O carro híbrido está em movimento.")

    def show_fuel_level(self):
        print(f"O nível de combustível do carro híbrido é {self.fuel_level}%.")


hybrid_car = HybridCar("Toyota", 80, 50)
hybrid_car.start()  # Output: O carro está ligado.
hybrid_car.charge()  # Output: O carro elétrico está sendo carregado.
hybrid_car.drive()  # Output: O carro híbrido está em movimento.
hybrid_car.show_fuel_level()  # Output: O nível de combustível do carro híbrido é 50%.
hybrid_car.stop()  # Output: O carro está desligado.
