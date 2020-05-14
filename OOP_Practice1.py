#author: Tyler Elenberger
#created: 10/27/2019

class Employee():
    def __init__(self,employee,number):
        self.employee = employee
        self.number = number
        
class ProductionWorker(Employee):
    def __init__(self,employee,number,shift,pay):
        Employee.__init__(self,employee,number)
        self.shift = shift
        self.pay = pay
        
    def display_values(self,*args):
        print("############################")
        print("Employee name: ",self.employee)
        print("\n")
        print("Employee number: ",self.number)
        print("\n")
        print("Employee shift number: ",self.shift)
        print("\n")
        print("Employee hourly pay rate",self.pay)
    
class ShiftSupervisor(Employee):

    def __init__(self,employee,number,shift,pay):
        Employee.__init__(self,employee,number)
        self.annual = annual
        
    def check_bonus(self):
        bonus = 3000
        if (int(annual) <= 48000):
            print("\n")
            print("Supervisor has received a bonus of :",bonus)
        else:
            print("\n")
            print("Supervisor didn't receive their bonus")
            
employee = input("Enter the employee's name: ")
number = input("Enter employee number: ")
shift = input("Enter employee shift number: ")
pay = input("Enter employee's hourly pay rate: ")
annual = int(pay) * 40 * 48

productionObject = ProductionWorker(employee,number,shift,pay)
productionObject.display_values()

supervisorObject = ShiftSupervisor(employee,number,shift,pay)
print('\n')
print(annual)
supervisorObject.check_bonus()
