class Car:
     def move(self):
        return "driving"
     
class Boat:
    def move(self):
        return "sailing"
    
class Airplane:
    def move(self):
        return "flying"
    
# in action
for vehicle in [Car(), Boat(), Airplane()]:
    print(vehicle.move())

# Output:
# driving
# sailing
# flying

