# Python Assignment — Part 2: Data Structures

## Restaurant Menu & Order Management System

This project is a Restaurant Order Management System built using Python's core data structures — lists, dictionaries, and nested combinations of both.

## What It Does

The script (`part2_order_system.py`) works through four main tasks:

### Task 1 — Explore the Menu
- Prints the full menu grouped by category (Starters, Mains, Desserts)
- Shows total item count, available items, the most expensive item, and items under ₹150

### Task 2 — Cart Operations
- Simulates adding, removing, and updating items in a shopping cart
- Handles edge cases like unavailable items, missing items, and duplicate additions
- Prints a final order summary with subtotal, 5% GST, and total payable

### Task 3 — Inventory Tracker with Deep Copy
- Creates a deep copy of the inventory to protect the original data
- Deducts stock based on the cart from Task 2
- Prints reorder alerts when stock falls at or below the reorder level
- Compares final inventory with the backup to prove deep copy worked

### Task 4 — Daily Sales Log Analysis
- Calculates and prints revenue per day
- Finds the best-selling day and most ordered item
- Adds a new day's data and recalculates all stats
- Prints a numbered list of all orders using `enumerate`

## How to Run

```bash
python3 part2_order_system.py
```

## Requirements

- Python 3.x
- No external libraries needed (only uses `copy` from stdlib)
