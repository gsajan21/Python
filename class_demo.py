class Employee:
    # class variable
    company = "Sajan Gurung"
    
    def __inti__(self):
        print("")
    
    def __iniSt__(self, name, dept, salary):
        # instance variable
        self.name = name
        self.dept = dept
        self.salary = salary
        
    # instance method
    def show(self):
        print("Employee: ", self.name, self.dept, self.salary, Employee.company)
      
    # instance method
    def change_salary(self, new_salary):
        # modify salary or single instance variable
        self.salary = new_salary
    
    # class method
    @classmethod
    def change_name(cls, new_company):
        # modify class variable
        cls.company = new_company
    

emp1 = Employee("Sajan", "IT", 2345)
    
emp1.show()