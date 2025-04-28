# utils/file_handler.py

import json
import os
import csv
from employee import Employee

DATABASE_FILE = 'database.json'
CSV_FILE = 'employees.csv'

def load_data():
    if not os.path.exists(DATABASE_FILE):
        return []

    with open(DATABASE_FILE, 'r') as f:
        try:
            data = json.load(f)
            return [Employee.from_dict(emp) for emp in data]
        except json.JSONDecodeError:
            return []

def save_data(employees):
    with open(DATABASE_FILE, 'w') as f:
        json.dump([emp.to_dict() for emp in employees], f, indent=4)

def export_to_csv(employees):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Employee ID", "Name", "Age", "Position", "Salary"])
        for emp in employees:
            writer.writerow([emp.emp_id, emp.name, emp.age, emp.position, emp.salary])
