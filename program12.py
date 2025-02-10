class Animals: 
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print("eating")
    def play(self):
        print("play")
    def sleep(self):
        print("sleep")
animal=Animals("lion",10)
print(animal.name)
print(animal.age)
animal2=Animals("tiger",5)
print(animal2.name)
print(animal2.age)                    

