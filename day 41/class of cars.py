# Day 41
# Class Of Cars

class Cars:
    def __init__(self,car_model, color, year, transmission, electric):
        self.car_model = car_model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_car(self):
        return (f"car_model = {self.car_model}\n"
                f"Color = {self.color}\n"
                f"Year = {self.year}\n"
                f"Transmission = {self.transmission}\n"
                f"Electric = {self.electric}")

class BMW(Cars):
    def __init__(self,car_model, color, year, transmission, electric):
        Cars.__init__(self,car_model, color, year, transmission, electric)

class TESLA(Cars):
    def __init__(self, car_model, color, year, transmission, electric):
        Cars.__init__(self, car_model, color, year, transmission, electric)

class FORD(Cars):
    def __init__(self, car_model, color, year, transmission, electric):
        Cars.__init__(self, car_model, color, year, transmission, electric)



bmw1 = BMW("x6", "silver", 2018, "Auto", False)
tesla1 = TESLA("S", "beige", 2017, "Auto", True)
ford1 = FORD("Focus", "White", 2020, "Auto", False)

print(bmw1.print_car(),"\n")
print(tesla1.print_car(),"\n")
print(ford1.print_car())
