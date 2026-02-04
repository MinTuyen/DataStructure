
class Employee:
    "Employee"
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.identifier=kwargs.get("identifier")
        self.salary=kwargs.get("salary")
        self.info_list = list(kwargs.values())

    def cal_salary(self):
        return 0

    def __str__(self):
        return self.__class__.__name__ + "\n" + ",".join(map(str,self.info_list))



############################################################
############################################################
############################################################
class PermanentEmployee(Employee):
    "Permanent Employee"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._benefits=kwargs.get("benefits")
    @property
    def benefits (self):
        return self._benefits
    @benefits.setter
    def benefits (self,type):
        if isinstance(type, list):
            self._benefits = type
        else:
            raise ValueError("Invalid list, please try again!")

    def cal_salary(self):
        if "health_insurance" in self._benefits and "retirement" in self.benefits:
            return float(self.salary * 0.7)
        elif "health_insurance" in self._benefits:
            return float(self.salary * 0.9)
        elif "retirement" in self._benefits:
            return float(self.salary * 0.8)
        else:
            return float(self.salary)


    def __str__(self):
        return self.__class__.__name__ + "\n" +",".join(map(str,self.info_list))



############################################################
############################################################
############################################################
class Manager(Employee):
    "Manager"
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
    
        self._bonus =kwargs.get("bonus")
    @property
    def bonus (self):
        return self._bonus
    @bonus.setter
    def bonus(self, new_bonus):
        if new_bonus > 0 and isinstance(new_bonus,float):
            self._bonus = new_bonus
        else:
            raise ValueError("Invalid bonus, please try again!")
    
    def cal_salary(self):
        return float((self._bonus) + (self.salary))
    def __str__(self):
        return self.__class__.__name__ + "\n" +",".join(map(str,self.info_list))




############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    "Temporary Employee"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._hours =kwargs.get("hours")

    @property
    def hours (self):
        return self.hours
    @ hours.setter
    def hours(self, new_hours):
        if new_hours > 0 and isinstance(new_hours,int):
            self._hours = new_hours
        else:
            raise ValueError("Invalid hours, please try again!")
    def cal_salary(self):
        return float(self.salary * self._hours)



    def __str__(self):
        return self.__class__.__name__ + "\n" +",".join(map(str,self.info_list))



############################################################
############################################################
############################################################
class Consultant(TemporaryEmployee):
    "Consultant"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._travel = kwargs.get("travel")

    @property
    def travel (self):
        return self._travel
    @travel.setter
    def travel(self, new_travel_hour):
        if new_travel_hour > 0 and isinstance(new_travel_hour,int):
            self._travel = new_travel_hour
        else:
            raise ValueError("Invalid travel hours, please try again!")

    def cal_salary(self):
        return float(self._travel * 1000 + self.salary * self._hours)
    def __str__(self):
        return self.__class__.__name__ + "\n" +",".join(map(str,self.info_list))



############################################################
############################################################
############################################################
class ConsultantManager(Consultant, Manager):
    "Consultant Manager"
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)


    def cal_salary(self):
        return float((self._hours)*self.salary + self._travel*1000 +self._bonus)

    def __str__(self):
        return self.__class__.__name__ + "\n" +",".join(map(str,self.info_list))


############################################################
############################################################
############################################################

def main():
    ''' ##### DRIVER CODE #####
        ##### Do not change. '''

    # create employees
    chris = Employee(name="Chris", identifier="UT1")
    emma = PermanentEmployee(name="Emma", identifier="UT2", salary=100000, benefits=["health_insurance"])
    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    charlotte = Manager(name="Charlotte", identifier="UT5", salary=1000000, bonus=100000)
    matt = ConsultantManager(name="Matt", identifier="UT6", salary=1000, hours=40, travel=4, bonus=10000)

    # print employees
    print(chris, "\n")
    print(emma, "\n")
    print(sam, "\n")
    print(john, "\n")
    print(charlotte, "\n")
    print(matt, "\n")

    # calculate and print salaries
    print("Check Salaries")
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]
    print("Emma's Salary is:", emma.cal_salary())
    print("Sam's Salary is:", sam.cal_salary())
    print("John's Salary is:", john.cal_salary())
    print("Charlotte's Salary is:", charlotte.cal_salary())
    print("Matt's Salary is:",  matt.cal_salary())

if __name__ == "__main__":
    main()
