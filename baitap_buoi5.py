from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Lương phải là số dương !")

    def display_info(self):
        tong_luong = self.calculate_salary()
        print(f"ID: {self.id}, Tên: {self.name}, Lương thực nhận: {tong_luong}")
        
    @abstractmethod
    def calculate_salary(self):
        pass

class developer(Employee):
    def __init__(self, id, name, salary, programming_language, overtime_hour):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
        self.overtime_hour = overtime_hour

    def calculate_salary(self):
        return self.get_salary() + (self.overtime_hour * 200)

class Manager(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.get_salary() + self.bonus
    

dev_1 = developer(1, "Tân", 500000, "Python", 50)
mng_1 = Manager(1, "Tân", 900000, 500)

dev_1.display_info()
mng_1.display_info()

dev_1.set_salary(700)

dev_1.display_info()


    