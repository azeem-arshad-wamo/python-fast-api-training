import os
os.system('clear')

# We are writing an example where we will have different employee salary processings
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    @abstractmethod
    def calculatePayroll(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, id, name, weeklySalary):
        super().__init__(id, name)
        self.weeklySalary = weeklySalary

    def calculatePayroll(self):
        return self.weeklySalary
    
class HourlyEmployee(Employee):
    def __init__(self, id, name, hoursWorked, hourlyRate):
        super().__init__(id, name)
        self.hoursWorked = hoursWorked
        self.hourlyRate = hourlyRate

    def calculatePayroll(self):
        return self.hourlyRate * self.hoursWorked

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weeklySalary, commission):
        super().__init__(id, name, weeklySalary)
        self.commission = commission

    def calculatePayroll(self):
        fixed = super().calculatePayroll()
        return fixed + self.commission

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} screams and yells for {hours} hours.")

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing office paperwork.")

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours on the phone.")

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"{self.name} manufactures gadgets for {hours} hours.")

# ...

class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hourly_rate)
