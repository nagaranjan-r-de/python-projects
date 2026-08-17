# 🚌 Python Bus / Train Ticket Booking System

A simple **console-based Bus / Train Ticket Booking System built with Python**.

This project is part of my **Python learning journey**, where I practice Python concepts by building small projects.

---

## 📌 Features

- 🚌 View available buses and trains
- 🔍 Search buses/trains by source and destination
- 💺 View available seats
- 🎫 Book a ticket
- ❌ Cancel a ticket
- 📋 View booking details
- 📊 View all bookings
- 💰 Calculate ticket price
- ⚠️ Validate user input
- 💾 Save bookings to a file
- 📂 Read vehicle data from a file

---

## 🧠 Concepts Learned

- Variables and Data Types
- Lists and Dictionaries
- Loops
- Conditional Statements
- Functions
- Modules
- User Input
- Exception Handling
- **File Handling**
- Reading data from files
- Writing data to files
- `open()`
- `read()`
- `write()`
- `with open()`

---

## 📂 Currently Learning: File Handling

I am currently learning **File Handling in Python** and applying it to this project.

File Handling allows the program to **read data from files and save data to files**.

For example, reading vehicle data:

```python
with open("data/vehicles.txt", "r") as file:
    data = file.read()
    print(data)
 ```

 ---

## 🏗️ Project Structure

```text
bus-train-booking/
│
├── data/
│   ├── vehicles.txt      # Bus and train data
│   └── bookings.txt      # Saved booking data
│
├── vehicles.py           # View and search buses/trains
├── bookings.py           # Booking and cancellation
├── utils.py              # Validation and utility functions
├── main.py               # Main program and menu
├── README.md             # Project documentation
│
└── venv/                 # Python virtual environment
```
