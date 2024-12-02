from abc import ABC, abstractmethod


class vehicle(ABC):

    @abstractmethod
    def engine_condition(self):
        pass


class specs(vehicle):
    def __init__(self, vehicle_type, color, engine_state):
        self.type = vehicle_type#$
        self.color = color#$
        self.engine = engine_state #$

    def engine_condition(self):# $
        if self.engine is True:
            print('engine started')
        else:
            print('engine stopped')


# multi level ineritance
class car(specs):
    wheels = 4#

    def __init__(self, gears, vehicle_type, color, engine_state):
        self.gears = gears#$
        super().__init__(vehicle_type, color, engine_state)

    # instancemethod
    def details(self):# $
        # self.engine_condition()
        print(f"This car has {self.gears} gears in {self.color} color with {self.type} type {self.wheels}")

    @classmethod
    def get_wheel_details(cls):# $
        print(f"this car has {cls.wheels} wheels")

    @staticmethod
    def get_info():# $
        print("this is car class")


# hierarical inheritance
class bike(car):
    wheels = 2  # class variable

    def __init__(self, gears, vehicle_type, color, engine_state):
        self.gears = gears
        super().__init__(vehicle_type, color, engine_state)

    # instancemethod
    def details(self):
        print(f"This bike has {self.gears} gears in {self.color} color with {self.type} type")

    @classmethod
    def get_wheel_details(cls):
        print(f"this bike has {cls.wheels} wheels")

    @staticmethod
    def get_info():
        print("this is bike class")


# polymorphism
def transport(obj):
    obj.get_info()
    obj.get_wheel_details()
    obj.details()
    obj.engine_condition()


#encapsulation
car_obj = car(6, "diesel", "black", True)
bike_obj = bike(5, "petrol", "white", False)
transport(car_obj)
transport(bike_obj)

# print(dir(car))
# print(dir(car_obj))


