# employee.py

class Employee:
    def __init__(self, emp_id, name, age, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "position": self.position,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            emp_id=data['emp_id'],
            name=data['name'],
            age=data['age'],
            position=data['position'],
            salary=data['salary']
        )
