class Motors:

    def __init__ (self, make, model, size_of_wheels, color, engine_type, engine_size):
        self.make = make
        self.model = model
        self.size_of_wheels = size_of_wheels
        self.color = color
        self.engine_type = engine_type
        self.engine_size = engine_size
    

class Car:

    def __init__ (self, doors, color, make, model, engine_type, engine_size):
        self.doors = doors
        self.color = color
        self.make = make
        self.model = model
        self.engine_type = engine_type
        self.engine_size = engine_size


motor1 = Motors("HONDA", "R1", "8.5in x 17in", "Black", "V-Twin", "1000cc")

car1 = Car("4Doors", "RED", "Tesla", "X", "AC Induction", "28in x 26in")