import uuid
class Employee:
    employee_id=""
    name=""
    family=""
    salary=[]
    department=""
    #computes average salary of an employee
    def avgsal(self):
        total=0
        for i in range(len(self.salary)):
            total += self.salary[i]
        print("avgSal",total/len(self.salary))
    #prints the employee object attribute values
    def printEmp(self):
        print(self.name,self.family,self.salary,self.department,self.employee_id)
    #constructor to initialize the attributes of employee class
    def __init__(self,name,family,salary,department,employee_id):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        self.employee_id = employee_id

#child class of Employee
class FulltimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        #calls the constructor of parent class, Employee
        super().__init__(name,family,salary,department,uuid.uuid1())
    #prints few attribute values declared in its parent class
    def printFTEmp(self):
        print(self.name,self.employee_id)

#child class object
emp1 = FulltimeEmployee("John","Doughles",[1000,800,900],"HW")
emp1.printFTEmp()
emp1.printEmp()
emp1.avgsal()
#parent class object
emp2 = Employee("Sarah","Johnson",[1000],"SW",uuid.uuid1())
emp2.printEmp()
emp2.avgsal()