from abc import ABC,abstractmethod

class car(ABC):
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    @abstractmethod
    def printdetails(self):
        pass

    def accelerate(self):
        print("speed up")

    def break_applied(self):
        print("car stopped")

class hatchback(car):
    def printdetails(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)

    def sunroof(self):
        print("not having this feature")

class suv(car):
    def printdetails(self):
       print("brand:",self.brand)
       print("brand:",self.brand)
       print("year:",self.year)

    def sunroof(self):
        print("available")

car1=hatchback("maruti","alto","2022")

car1.printdetails()
car1.accelerate()
car1.sunroof()
ca2=suv("maruti","alto","2022")
ca2.printdetails()
ca2.accelerate()
ca2.sunroof()
    
                                   