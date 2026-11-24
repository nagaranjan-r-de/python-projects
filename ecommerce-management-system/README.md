# 🛒 Python E-Commerce Management System

A simple **console-based E-Commerce Management System built with Python**.

This project is part of my **Python learning journey**, where I practice Python concepts by building small projects.

---

## 📌 Features

- 📦 View available products
- 🔍 Search products
- 🛒 Add products to cart
- 📋 View cart
- ❌ Remove products from cart
- 💰 Calculate product and cart totals
- 💳 Checkout and confirm orders
- 📊 Track product stock
- ⚠️ Exception handling
- 🧹 Clear cart after successful checkout

---

## 🧠 Concepts Learned

- Variables and Data Types
- Lists and Dictionaries
- Loops
- Conditional Statements
- Functions
- Modules
- User Input
- **Exception Handling**
- `try`
- `except`
- `else`
- `finally`
- `ValueError`
- `KeyError`

---

## ⚠️ Newly Learned: Exception Handling

I recently learned **Exception Handling in Python** and implemented it in this project.

It helps the program handle unexpected errors without crashing.

For example:

```python
try:
    product_count = int(
        input("Enter number of products to add: ")
    )
except ValueError:
    print("Please enter a valid number.")
```
---

## 🏗️ Project Structure

```text
ecommerce-management-system/
│
├── data.py          # Product data
├── products.py      # View and search products
├── cart.py          # Add and remove products from cart
├── checkout.py      # View cart and checkout
├── main.py          # Main program and menu
├── README.md        # Project documentation
│
└── venv/            # Python virtual environment