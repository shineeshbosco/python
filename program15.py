class private:
    def __init__(self):
        self.__salary=5000
    def salary(self):
        return self.__salary

obj=private()
print(obj.salary())        