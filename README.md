# 🍽️ SHUBH Restaurant Management System

## 📌 Project Overview

The **SHUBH Restaurant Management System** is a console-based Python application developed to automate and manage restaurant operations efficiently. The system allows administrators, customers, and staff members to perform various restaurant-related tasks such as menu management, order processing, cart management, billing, table management, and sales reporting.

This project demonstrates the practical implementation of Python concepts such as file handling, JSON data storage, modular programming, exception handling, and object-oriented design principles.

---

## 🚀 Features

### 👨‍💼 Administrator Module

* Create and manage staff accounts
* View restaurant menu
* Add new food items
* Update existing food items
* Delete food items
* View customer orders
* Delete orders
* View sales reports

### 🧑‍🍳 Staff Module

* View all orders
* Search orders by Order ID, Token Number, or Table Number
* View due payments
* View active tables

### 🧑 Customer Module

* Create customer account
* Sign in securely
* View menu
* Add food items to cart
* Update cart items
* Place Dine-In or Take-Away orders
* Generate bills and make payments

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)
* File Handling
* Modular Programming
* Exception Handling
* UUID Module
* Datetime Module
* Getpass / Maskpass

---

## 📂 Project Structure


SHUBHrestro/
│
├── main.py
├── modules.py
├── auth.py
│
├── AdminPanel/
│   └── admin.py
│
├── CustomerPanel/
│   └── customer.py
│
├── StaffPanel/
│   └── staff.py
│
└── Database/
    ├── menu.json
    ├── cart.json
    ├── orders.json
    ├── tables.json
    └── users.json


## 📸 Sample Functionalities

* User Authentication
* Menu Management
* Cart Management
* Order Placement
* Billing System
* Table Management
* Sales Report Generation


## 🔐 Authentication

The system provides secure login functionality for:

* Administrator
* Staff
* Customer

Passwords are masked during input using the `maskpass` package.

---

## 📈 Future Enhancements

* Database integration using MySQL or MongoDB
* GUI development using Tkinter or PyQt
* Online payment gateway integration
* Email/SMS notifications
* Inventory management system
* Web-based version using Django or Flask

---

## 👨‍💻 Author

**Shubhendra Singh**

Aspiring Java & Python Developer

---

## ⭐ Acknowledgements

This project was developed for learning and demonstrating Python programming concepts in a real-world application.
