class Motors:

    def __init__ (self, make, model, size_of_wheels, color, engine_type, engine_size):
        self.make = make
        self.model = model
        self.size_of_wheels = size_of_wheels
        self.color = color
        self.engine_type = engine_type
        self.engine_size = engine_size

    def __str__(self):
        return f'Motor object\nMake: {self.make}\nModel: {self.model}\nSize of wheels: {self.size_of_wheels}\nColor: {self.color}\nEngine type: {self.engine_type}\nEngine size: {self.engine_size}'    

class Car:

    def __init__ (self, doors, color, make, model, engine_type, engine_size):
        self.doors = doors
        self.color = color
        self.make = make
        self.model = model
        self.engine_type = engine_type
        self.engine_size = engine_size
    
    def __str__(self):
        return f'Car object\nNumber of doors: {self.doors}\nMake: {self.make}\nModel: {self.model}\nColor: {self.color}\nEngine type: {self.engine_type}\nEngine size: {self.engine_size}' 


car1 = Car(4, 'black', 'Toyota', 'Corolla', 'Air-breathing', '150cc')
motor1 = Motors('Honda', 'R1', '14in', 'Black', 'Air-breathing','150cc')

print(car1)
print(motor1)