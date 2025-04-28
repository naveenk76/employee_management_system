from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use a strong secret key!

# File where employee data will be stored
EMPLOYEE_DATA_FILE = 'employees.json'

# In-memory user store (replace this with a database in real applications)
users = {}

# Load employees from JSON file or initialize as an empty list
def load_employees():
    if os.path.exists(EMPLOYEE_DATA_FILE):
        with open(EMPLOYEE_DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return []

# Save employees to JSON file
def save_employees(employees):
    with open(EMPLOYEE_DATA_FILE, 'w') as f:
        json.dump(employees, f)

# Home Route
@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        search_query = request.args.get('search', '').strip().lower()  # Get search query
        employees = load_employees()
        filtered_employees = []

        if search_query:
            # Filter employees based on ID or Name
            filtered_employees = [
                emp for emp in employees
                if str(emp['emp_id']).startswith(search_query) or search_query in emp['name'].lower()
            ]
        else:
            filtered_employees = employees  # If no search query, show all employees

        return render_template('home.html', employees=filtered_employees)

    return redirect(url_for('login'))

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not username or not password or not confirm_password:
            flash("Please fill out all fields.")
            return redirect(url_for('register'))

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for('register'))

        if len(password) < 6:
            flash("Password must be at least 6 characters long.")
            return redirect(url_for('register'))

        # Store the user in the in-memory 'users' dictionary
        if username in users:
            flash("Username already taken. Please choose a different username.")
            return redirect(url_for('register'))

        users[username] = {'password': password, 'role': 'user'}  # Default role is user
        flash("Registration successful! Please log in.")
        return redirect(url_for('login'))

    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        # Check if the username exists and the password matches
        if username in users and users[username]['password'] == password:
            session['username'] = username
            flash("Login successful!")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.")
            return redirect(url_for('login'))

    return render_template('login.html')

# Admin Dashboard Route
@app.route('/admin')
def admin_dashboard():
    if 'username' not in session or users[session['username']]['role'] != 'admin':
        flash("Access denied!")
        return redirect(url_for('home'))

    return render_template('admin_dashboard.html')

# Manage Users Route
@app.route('/admin/manage_users')
def manage_users():
    if 'username' not in session or users[session['username']]['role'] != 'admin':
        flash("Access denied!")
        return redirect(url_for('home'))

    return render_template('manage_users.html', users=users)

# Edit User Route
@app.route('/admin/edit_user/<username>', methods=['GET', 'POST'])
def edit_user(username):
    if 'username' not in session or users[session['username']]['role'] != 'admin':
        flash("Access denied!")
        return redirect(url_for('home'))

    if username not in users:
        flash("User not found!")
        return redirect(url_for('manage_users'))

    if request.method == 'POST':
        new_role = request.form['role']
        users[username]['role'] = new_role  # Update the user's role
        flash(f"User '{username}' updated successfully!")
        return redirect(url_for('manage_users'))

    return render_template('edit_user.html', username=username, role=users[username]['role'])

# Add Employee Route
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        position = request.form['position']
        salary = float(request.form['salary'])

        # Load existing employees and add a new one
        employees = load_employees()

        # Add new employee with unique ID
        emp_id = len(employees) + 1  # Simple ID generation
        employees.append({'emp_id': emp_id, 'name': name, 'age': age, 'position': position, 'salary': salary})

        # Save updated employee list
        save_employees(employees)

        flash("Employee added successfully!")
        return redirect(url_for('home'))

    return render_template('add_employee.html')

# Update Employee Route
@app.route('/update/<int:emp_id>', methods=['GET', 'POST'])
def update_employee(emp_id):
    employees = load_employees()
    emp = next((emp for emp in employees if emp['emp_id'] == emp_id), None)
    if not emp:
        flash("Employee not found.")
        return redirect(url_for('home'))

    if request.method == 'POST':
        emp['name'] = request.form['name']
        emp['age'] = int(request.form['age'])
        emp['position'] = request.form['position']
        emp['salary'] = float(request.form['salary'])

        # Save updated employee list
        save_employees(employees)

        flash("Employee updated successfully!")
        return redirect(url_for('home'))

    return render_template('update_employee.html', employee=emp)

# Delete Employee Route
@app.route('/delete/<int:emp_id>', methods=['GET'])
def delete_employee(emp_id):
    employees = load_employees()
    employees = [emp for emp in employees if emp['emp_id'] != emp_id]

    # Save updated employee list
    save_employees(employees)

    flash("Employee deleted successfully!")
    return redirect(url_for('home'))

# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
