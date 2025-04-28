# manager.py

from employee import Employee
from utils.file_handler import load_data, save_data

class EmployeeManager:
    def __init__(self):
        self.employees = load_data()

    def _generate_id(self):
        if not self.employees:
            return "EMP001"
        last_id = max(int(emp.emp_id[3:]) for emp in self.employees)
        return f"EMP{str(last_id + 1).zfill(3)}"

    def add_employee(self, name, age, position, salary):
        emp_id = self._generate_id()
        employee = Employee(emp_id, name, age, position, salary)
        self.employees.append(employee)
        save_data(self.employees)

    def remove_employee(self, emp_id):
        self.employees = [e for e in self.employees if e.emp_id != emp_id]
        save_data(self.employees)

    def update_employee(self, emp_id, **kwargs):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.name = kwargs.get('name', employee.name)
                employee.age = kwargs.get('age', employee.age)
                employee.position = kwargs.get('position', employee.position)
                employee.salary = kwargs.get('salary', employee.salary)
                save_data(self.employees)
                return
