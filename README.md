# 🏢 Employee Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-orange.svg)](https://sqlite.org/)

A comprehensive **Employee Management System** built with Flask and SQLAlchemy. Streamline your HR operations with employee tracking, attendance management, leave requests, and payroll processing.

## ✨ Features

### 🔐 Authentication & Authorization
- Secure login/logout system
- Role-based access control (Admin, Manager, Employee)
- Password hashing with werkzeug security
- Session management

### 👥 Employee Management
- Add, view, edit, and delete employees
- Employee profile with photo upload
- Search and filter employees
- Export employee data to CSV/PDF

### 🏢 Department Management
- Create and manage departments
- Assign employees to departments
- Department-wise reporting

### 📅 Attendance Tracking
- Daily check-in/check-out
- Attendance calendar view
- Monthly attendance reports
- Late arrival tracking

### 📋 Leave Management
- Apply for leave (Casual, Sick, Annual)
- Approve/reject leave requests
- Leave balance tracking
- Leave history

### 💰 Payroll Management
- Salary structure management
- Monthly payroll generation
- Download payslips
- Tax calculation (configurable)

### 📊 Dashboard & Analytics
- Real-time statistics
- Charts and graphs (via Chart.js)
- Employee distribution by department
- Attendance trends

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)
- Git (optional)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/employee-management-system.git
cd employee-management-system
