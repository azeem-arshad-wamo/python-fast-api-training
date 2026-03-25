from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee, Manager, Secretary, SalesPerson, FactoryWorker, TemporaryEmployee
from productivity import ProductivitySystem

class PayrollSystem:
    def calculatePayroll(self, employees):
        print("Calculating Payroll")
        print("====================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculatePayroll()}")
            print("")


salary = SalaryEmployee(1, "Goose", 1400)
hourly = HourlyEmployee(2, "Ali", 21, 40)
commission = CommissionEmployee(3, "Sara", 1200, 499)

payroll = PayrollSystem()
payroll.calculatePayroll([salary, hourly, commission])

manager = Manager(1, "Mary Poppins", 3000)
secretary = Secretary(2, "John Smith", 1500)
sales_guy = SalesPerson(3, "Kevin Bacon", 1000, 250)
factory_worker = FactoryWorker(4, "Jane Doe", 40, 15)
temporary_secretary = TemporaryEmployee(5, "Robin Williams", 40, 9)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary
]

productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = PayrollSystem()
payroll_system.calculatePayroll(employees)