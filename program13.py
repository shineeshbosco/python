class dog:
    def __init__(self,name):
        self.name=name
    def displayname(self):
        print(f"dog name is :",{self.name})

class lab(dog):
    def sound(self):
        print("labrodar woofs")
class guide(lab,dog):
    def sound():
        print("guide")
dog1=dog('lab')
print(dog1.name)
dog1.displayname()

lab1=lab('labrodar')
lab1.displayname()
print(lab1.name)


1.single
2.multible
3.multi level