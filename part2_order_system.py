# Part 2 — Restaurant Menu & Order Management System
# using lists, dicts, and nested combinations

import copy

# ===================== PROVIDED DATA =====================

menu = {
    "Paneer Tikka":    {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":   {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":        {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken":  {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":       {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":     {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":     {"category": "Mains",     "price": 40.0,  "available": True},
    "Gulab Jamun":     {"category": "Desserts",  "price": 90.0,  "available": True},
    "Rasgulla":        {"category": "Desserts",  "price": 80.0,  "available": True},
    "Ice Cream":       {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":    {"stock": 10, "reorder_level": 3},
    "Chicken Wings":   {"stock": 8,  "reorder_level": 2},
    "Veg Soup":        {"stock": 15, "reorder_level": 5},
    "Butter Chicken":  {"stock": 12, "reorder_level": 4},
    "Dal Tadka":       {"stock": 20, "reorder_level": 5},
    "Veg Biryani":     {"stock": 6,  "reorder_level": 3},
    "Garlic Naan":     {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":     {"stock": 5,  "reorder_level": 2},
    "Rasgulla":        {"stock": 4,  "reorder_level": 3},
    "Ice Cream":       {"stock": 7,  "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],            "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],               "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],          "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],              "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],            "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],              "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],         "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],            "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],           "total": 270.0},
    ],
}


# ======================== TASK 1 ========================
# Explore the Menu
# ========================================================

print("=" * 50)
print("TASK 1 — Explore the Menu")
print("=" * 50)

# 1. Print menu grouped by category
# first collect unique categories in the order they appear
categories = []
for item_name in menu:
    cat = menu[item_name]["category"]
    if cat not in categories:
        categories.append(cat)

for cat in categories:
    print(f"\n===== {cat} =====")
    for item_name in menu:
        info = menu[item_name]
        if info["category"] == cat:
            # show availability tag
            tag = "Available" if info["available"] else "Unavailable"
            print(f"  {item_name:<18} ₹{info['price']:.2f}   [{tag}]")

# 2. Compute and print summary stats
total_items = len(menu)
available_count = 0
for item_name in menu:
    if menu[item_name]["available"]:
        available_count += 1

print(f"\nTotal items on the menu: {total_items}")
print(f"Total available items:   {available_count}")

# most expensive item — go through each item to find max price
most_expensive_name = None
highest_price = 0
for item_name in menu:
    if menu[item_name]["price"] > highest_price:
        highest_price = menu[item_name]["price"]
        most_expensive_name = item_name

print(f"Most expensive item:     {most_expensive_name} (₹{highest_price:.2f})")

# items priced under 150
print("Items under ₹150:")
for item_name in menu:
    price = menu[item_name]["price"]
    if price < 150:
        print(f"  - {item_name}: ₹{price:.2f}")


# ======================== TASK 2 ========================
# Cart Operations
# ========================================================

print("\n" + "=" * 50)
print("TASK 2 — Cart Operations")
print("=" * 50)

cart = []  # list of dicts: {"item": ..., "quantity": ..., "price": ...}


def add_to_cart(item_name, qty):
    """Add an item to the cart. Handles validation and duplicate merging."""
    # check if item exists in menu
    if item_name not in menu:
        print(f"  >> '{item_name}' does not exist in the menu.")
        return

    # check availability
    if not menu[item_name]["available"]:
        print(f"  >> '{item_name}' is currently unavailable.")
        return

    # if already in cart, just bump the quantity
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] += qty
            print(f"  >> Updated '{item_name}' quantity to {entry['quantity']}.")
            return

    # otherwise add new entry
    new_entry = {
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"],
    }
    cart.append(new_entry)
    print(f"  >> Added '{item_name}' x{qty} to cart.")


def remove_from_cart(item_name):
    """Remove an item from cart by name."""
    for i in range(len(cart)):
        if cart[i]["item"] == item_name:
            cart.pop(i)
            print(f"  >> Removed '{item_name}' from cart.")
            return
    print(f"  >> '{item_name}' is not in the cart.")


def update_quantity(item_name, new_qty):
    """Update quantity for an existing cart item."""
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_qty
            print(f"  >> Updated '{item_name}' quantity to {new_qty}.")
            return
    print(f"  >> '{item_name}' is not in the cart, cannot update.")


def print_cart():
    """Quick helper to show current cart state."""
    if len(cart) == 0:
        print("  [Cart is empty]")
    else:
        for entry in cart:
            print(f"  {entry['item']} x{entry['quantity']}  ₹{entry['price']:.2f}")
    print()


# 4. Simulate the required sequence and print cart after each step

print("\nStep: Add Paneer Tikka x2")
add_to_cart("Paneer Tikka", 2)
print_cart()

print("Step: Add Gulab Jamun x1")
add_to_cart("Gulab Jamun", 1)
print_cart()

print("Step: Add Paneer Tikka x1 (should merge)")
add_to_cart("Paneer Tikka", 1)
print_cart()

print("Step: Add Mystery Burger (does not exist)")
add_to_cart("Mystery Burger", 1)
print_cart()

print("Step: Add Chicken Wings (unavailable)")
add_to_cart("Chicken Wings", 1)
print_cart()

print("Step: Remove Gulab Jamun")
remove_from_cart("Gulab Jamun")
print_cart()

# 5. Final order summary
print("========== Order Summary ==========")
subtotal = 0
for entry in cart:
    line_total = entry["quantity"] * entry["price"]
    subtotal += line_total
    print(f"  {entry['item']:<18} x{entry['quantity']}   ₹{line_total:.2f}")

print("  " + "-" * 36)
gst = subtotal * 0.05  # 5% GST
total_payable = subtotal + gst
print(f"  Subtotal:             ₹{subtotal:.2f}")
print(f"  GST (5%):             ₹{gst:.2f}")
print(f"  Total Payable:        ₹{total_payable:.2f}")
print("=" * 38)


# ======================== TASK 3 ========================
# Inventory Tracker with Deep Copy
# ========================================================

print("\n" + "=" * 50)
print("TASK 3 — Inventory Tracker with Deep Copy")
print("=" * 50)

# 1. Deep copy inventory before any changes
inventory_backup = copy.deepcopy(inventory)

# demonstrate that backup is independent
# manually change one stock value
inventory["Paneer Tikka"]["stock"] = 999
print("\nAfter setting Paneer Tikka stock to 999 in inventory:")
print(f"  inventory  -> Paneer Tikka stock = {inventory['Paneer Tikka']['stock']}")
print(f"  backup     -> Paneer Tikka stock = {inventory_backup['Paneer Tikka']['stock']}")
print("  (backup is unaffected — deep copy works!)")

# restore inventory back to original before continuing
inventory = copy.deepcopy(inventory_backup)
print("  Restored inventory from backup.\n")

# 2. Simulate order fulfilment — deduct quantities from final cart
print("Deducting cart items from inventory:")
for entry in cart:
    name = entry["item"]
    qty_needed = entry["quantity"]
    current_stock = inventory[name]["stock"]

    if current_stock >= qty_needed:
        inventory[name]["stock"] -= qty_needed
        print(f"  {name}: deducted {qty_needed}, remaining stock = {inventory[name]['stock']}")
    else:
        # not enough stock — deduct only what is available
        print(f"  WARNING: {name} — only {current_stock} in stock, needed {qty_needed}. Deducting {current_stock}.")
        inventory[name]["stock"] = 0

# 3. Reorder alerts
print("\nReorder Alerts:")
for item_name in inventory:
    stock = inventory[item_name]["stock"]
    reorder = inventory[item_name]["reorder_level"]
    if stock <= reorder:
        print(f"  ⚠ Reorder Alert: {item_name} — Only {stock} unit(s) left (reorder level: {reorder})")

# 4. Print both to prove deep copy protected original
print("\nFinal inventory vs backup:")
print(f"  {'Item':<18} {'Current Stock':>14} {'Backup Stock':>14}")
print("  " + "-" * 48)
for item_name in inventory:
    curr = inventory[item_name]["stock"]
    orig = inventory_backup[item_name]["stock"]
    marker = " *" if curr != orig else ""
    print(f"  {item_name:<18} {curr:>14} {orig:>14}{marker}")
print("  (* = changed from original)")


# ======================== TASK 4 ========================
# Daily Sales Log Analysis
# ========================================================

print("\n" + "=" * 50)
print("TASK 4 — Daily Sales Log Analysis")
print("=" * 50)

# 1. Total revenue per day
print("\nRevenue per day:")
revenue_per_day = {}
for date in sales_log:
    day_total = 0
    for order in sales_log[date]:
        day_total += order["total"]
    revenue_per_day[date] = day_total
    print(f"  {date}: ₹{day_total:.2f}")

# 2. Best-selling day (highest revenue)
best_day = None
best_revenue = 0
for date in revenue_per_day:
    if revenue_per_day[date] > best_revenue:
        best_revenue = revenue_per_day[date]
        best_day = date
print(f"\nBest-selling day: {best_day} with ₹{best_revenue:.2f}")

# 3. Most ordered item across all days
# count how many individual orders each item appears in
item_order_count = {}
for date in sales_log:
    for order in sales_log[date]:
        for item_name in order["items"]:
            if item_name in item_order_count:
                item_order_count[item_name] += 1
            else:
                item_order_count[item_name] = 1

most_ordered = None
max_count = 0
for item_name in item_order_count:
    if item_order_count[item_name] > max_count:
        max_count = item_order_count[item_name]
        most_ordered = item_name
print(f"Most ordered item: {most_ordered} (appeared in {max_count} orders)")

# 4. Add a new day and reprint stats
new_day_orders = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]
sales_log["2025-01-05"] = new_day_orders
print("\n--- After adding 2025-01-05 ---")

# recalculate revenue per day
revenue_per_day = {}
for date in sales_log:
    day_total = 0
    for order in sales_log[date]:
        day_total += order["total"]
    revenue_per_day[date] = day_total

print("\nUpdated revenue per day:")
for date in revenue_per_day:
    print(f"  {date}: ₹{revenue_per_day[date]:.2f}")

# recalculate best-selling day
best_day = None
best_revenue = 0
for date in revenue_per_day:
    if revenue_per_day[date] > best_revenue:
        best_revenue = revenue_per_day[date]
        best_day = date
print(f"\nBest-selling day: {best_day} with ₹{best_revenue:.2f}")

# recalculate most ordered item
item_order_count = {}
for date in sales_log:
    for order in sales_log[date]:
        for item_name in order["items"]:
            if item_name in item_order_count:
                item_order_count[item_name] += 1
            else:
                item_order_count[item_name] = 1

most_ordered = None
max_count = 0
for item_name in item_order_count:
    if item_order_count[item_name] > max_count:
        max_count = item_order_count[item_name]
        most_ordered = item_name
print(f"Most ordered item: {most_ordered} (appeared in {max_count} orders)")

# 5. Numbered list of all orders using enumerate
print("\nAll orders (numbered):")
all_orders = []
for date in sales_log:
    for order in sales_log[date]:
        all_orders.append((date, order))

for idx, (date, order) in enumerate(all_orders, start=1):
    items_str = ", ".join(order["items"])
    print(f"  {idx}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")

print("\n--- Done ---")
