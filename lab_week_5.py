class Vehicle:
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = max_range
        self.seats = seats
        
    def move(self, speed):
        print(f"The vehicle is moving at {speed} km/h")
class Car(Vehicle):
    def __init__(self, colour, weight, max_speed, form_factor,  **kwargs):
        super().__init__(colour, weight, max_speed,  **kwargs)
        self.form_factor = form_factor

    def specification(self):
        print(f"Colour: {self.colour}")
        print(f"Weight: {self.weight} kg")
        print(f"Max speed: {self.max_speed} km/h")
        print(f"Form factor: {self.form_factor}")
        
    def move(self, speed):
        print(f"The car is driving at {speed} km/h")
        
class Electric(Car):
    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, max_range=None, seats=None):
        super().__init__(colour, weight, max_speed, form_factor,max_range=max_range, seats=seats)
        self.battery_capacity = battery_capacity
    def move(self, speed):
        print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range}")
        
        
class Petrol(Car):
    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, max_range=None, seats=None):
        super().__init__(colour, weight, max_speed, form_factor, max_range=max_range, seats=seats)
        self.fuel_capacity = fuel_capacity
    def move(self, speed):
        print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range}")
        
        
# New Plane class
class Plane(Vehicle):
    """ This class is a subclass of the Vehicle class, having one new argument wingspan"""
    def __init__(self, colour, weight, max_speed, wingspan,**kwargs):
        super().__init__(colour, weight, max_speed , **kwargs)
        self.wingspan = wingspan

    def move(self, speed):
        print(f"The plane is flying at {speed} km/h")
# Propeller plane subclass
class Propeller(Plane):
    """ This class is a subclass of the Plane class, having one new argument propeller_diameter"""
    def __init__(self, colour, weight, max_speed, wingspan, propeller_diameter):
        super().__init__(colour, weight, max_speed, wingspan)
        self.propeller_diameter = propeller_diameter

    def move(self, speed):
        print(f"The propeller plane is flying at {speed} km/h")

# Jet plane subclass
class Jet(Plane):
    """ This class is a subclass of the Plane class, having one new argument engine_thrust"""
    def __init__(self, colour, weight, max_speed, wingspan, engine_thrust):
        super().__init__(colour, weight, max_speed, wingspan)
        self.engine_thrust = engine_thrust

    def move(self, speed):
        print(f"The jet is flying at {speed} km/h")
 
        
# Multiple Inheritance 
class FlyingCar(Car, Plane):
    """ This class is a subclass of the Car and Plane classes"""
    def __init__(self, colour, weight, max_speed, form_factor, wingspan, **kwargs):
        # we need to add the wingspan to the keyword arguments so that following the MRO, the Plane class gets all the keyword arguments it needs
        super().__init__(colour, weight, max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)
    def move(self, speed):        
        print(f"The flying car is driving or flying at {speed} km/h")
class Animal:
    def move(self, speed):
        print(f"The animal is walking at {speed} km/h.")
      
def main():
    # object of electric car 
    # electric_car = Electric("green", 1200, 200, "Hatchback", 100, 200)
    # electric_car.move(100)
    
    
    # object of petrol car
    petrol_car = Petrol("red", 1500, 250, "SUV", 50, 100)
    petrol_car.move(150)
    
    # object of generic vehicle
    generic_vehicle = Vehicle("red", 1000, 200)
    generic_vehicle.move(100)
    
    # object of generic car
    generic_car = Car("red", 1000, 200, "SUV")
    generic_car.move(100)
    generic_car.specification()
    
    # object of generic electric car
    generic_car1 = Electric("red", 1000, 200, "SUV", 100, max_range=500, seats=5)
    generic_car1.move(100)
    print(generic_car1.seats)
    
    
    prop = Propeller("white", 5000, 600, 30, 3)
    prop.move(550)
    print("Propeller Diameter:", prop.propeller_diameter)

    # object of jet
    jet = Jet("grey", 10000, 900, 40, 20000)
    jet.move(850)
    print("Engine Thrust:", jet.engine_thrust)
    
    
    
    # multiple inheritance
    # object of flying car
    generic_flying_car = FlyingCar("red", 1000, 200, "SUV", 30, seats=5)
    generic_flying_car.move(100)
    print(generic_flying_car.seats, generic_flying_car.wingspan,
    generic_flying_car.form_factor)


    # object of flying car with more clarity
    generic_flying_car_2 = FlyingCar(colour="red", weight=1000, max_speed=200,
    form_factor="SUV", wingspan=30, seats=5)
    generic_flying_car_2.move(100)
    
    
    
    print('\n\n\n')
    vehicle = Vehicle("red", 1000, 150)
    car = Car("blue", 1200, 180, "Sedan")
    plane = Plane("white", 5000, 600, 25)
    flying_car = FlyingCar("silver", 1300, 200, "Hybrid", 15)
    animal = Animal()

    
    movable_objects = [vehicle, car, plane, flying_car, animal]

    # all classes have some implementation of move()
    # Calling move() on each object - this is polymorphism
    for obj in movable_objects:
        obj.move(20)


if __name__ == "__main__":
    main()
