class Bicycle:
    def move(self):
        return "Cycling."
    
class Car:
    def move(self):
        return "Driving.."

class Plane:
    def move(self):
        return "Flying...!"
    
class Boat:
    def move(self):
        return "Sailing...!"
    


for vehicle in [Bicycle(), Car(), Plane(), Boat()]:
    print(vehicle.move())

