import uuid
class Employee:
    employee_id=""
    name=""
    family=""
    salary=[]
    department=""
    
    def avgsal(self):
        total=0
        for i in range(len(self.salary)):
            total += self.salary[i]
        print("avgSal",total/len(self.salary))
    def printEmp(self):
        print(self.name,self.family,self.salary,self.department,self.employee_id)
    def __init__(self,name,family,salary,department,employee_id):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        self.employee_id = employee_id

class FulltimeEmployee(Employee):
    def __init__(self,name,family,salary,department):
        super().__init__(name,family,salary,department,uuid.uuid1())
    def printFTEmp(self):
        print(self.name,self.employee_id)


emp1 = FulltimeEmployee("John","Doughles",[1000,800,900],"HW")
emp1.printFTEmp()
emp1.printEmp()
emp1.avgsal()
emp2 = Employee("Sarah","Johnson",[1000],"SW",uuid.uuid1())
emp2.printEmp()
emp2.avgsal()