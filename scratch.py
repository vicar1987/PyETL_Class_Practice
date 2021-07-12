class Car
    wheels = 4
    def __init__(self, color, brand, power_type, price, max_speed, max_power):
        self.color = color
        self.brand = brand
        self.power_type = power_type
        self.seat = 5
        self.price = price
        self.speed = 0
        self.__max_speed = max_speed
        self.__max_power = max_power



class ElecrtricCar(Car)

    def __init__(self, color, brand, power_type, price, max_speed, max_power):
        super().__init__(color, brand, power_type, price, max_speed, max_power)
        self.gps = __gps

    @property
    def