import tkinter as tk
from tkinter import font

# Dictionary of items with categories as keys
items = {
    "beverages": {
        "Coffee": {"price": 2.50, "quantity": 0},
        "Tea": {"price": 2.00, "quantity": 0},
        "Soda": {"price": 1.50, "quantity": 0}
    },
    "snacks": {
        "Chips": {"price": 1.00, "quantity": 0},
        "Cookies": {"price": 1.25, "quantity": 0},
        "Sandwich": {"price": 3.00, "quantity": 0}
    },
    "desserts": {
        "Cake": {"price": 3.50, "quantity": 0},
        "Ice Cream": {"price": 2.75, "quantity": 0},
        "Pie": {"price": 4.00, "quantity": 0}
    }
}

# Global dictionary to store quantity labels
quantity_labels = {}

# Increment function
def increment(item_type, item_name):
    items[item_type][item_name]["quantity"] += 1
    quantity_labels[item_type][item_name]["text"] = str(items[item_type][item_name]["quantity"])

# Decrement function
def decrement(item_type, item_name):
    if items[item_type][item_name]["quantity"] > 0:
        items[item_type][item_name]["quantity"] -= 1
        quantity_labels[item_type][item_name]["text"] = str(items[item_type][item_name]["quantity"])

# Checkout function
def checkout():
    total_amount = sum(item_info["price"] * item_info["quantity"] for item_type in items.values() for item_info in item_type.values())
    breakdown_window = tk.Toplevel(root)
    breakdown_window.title("Checkout")
    breakdown_window.geometry("500x400")
    breakdown_window.config(bg='lightblue')
    
    tk.Label(breakdown_window, text="Item", font=heading_font, bg='lightyellow').pack(pady=5)
    tk.Label(breakdown_window, text="Quantity", font=heading_font, bg='lightyellow').pack(pady=5)
    tk.Label(breakdown_window, text="Total Price", font=heading_font, bg='lightyellow').pack(pady=5)
    
    for item_type, item_dict in items.items():
        for item_name, item_info in item_dict.items():
            quantity = item_info["quantity"]
            if quantity > 0:
                tk.Label(breakdown_window, text=f"{item_name}: {quantity}", bg='lightgreen').pack(pady=5)
                tk.Label(breakdown_window, text=f"${item_info['price'] * quantity:.2f}", bg='lightgreen').pack(pady=5)
    
    tk.Label(breakdown_window, text=f"Total Amount: ${total_amount:.2f}", font=bold_font, bg='lightpink').pack(pady=10)

# Create tkinter window
root = tk.Tk()
root.title("Cafe Bill Management System")
root.geometry("600x400")
root.config(bg='lightgray')

# Fonts
heading_font = font.Font(family='Helvetica', size=12, weight='bold')
bold_font = font.Font(family='Helvetica', size=10, weight='bold')

# Function to open the menu page
def open_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Cafe Menu")
    menu_window.geometry("800x600")
    menu_window.config(bg='lightcyan')

    # Create frames for each category
    frames = {}
    for i, category in enumerate(items.keys()):
        frames[category] = tk.LabelFrame(menu_window, text=category.capitalize(), padx=10, pady=10, bg='lightblue', font=heading_font)
        frames[category].pack(side="left", padx=20, pady=20)

    # Populate frames with items and buttons
    for category, item_dict in items.items():
        frame = frames[category]
        for j, (item_name, item_info) in enumerate(item_dict.items()):
            label = tk.Label(frame, text=f"{item_name}: $ {item_info['price']}", bg='white')
            label.pack(pady=5)
            
            quantity_label = tk.Label(frame, text=str(item_info["quantity"]), bg='white')
            quantity_label.pack(pady=5)
            quantity_labels.setdefault(category, {})[item_name] = quantity_label
            
            increment_button = tk.Button(frame, text="+", command=lambda ctg=category, iname=item_name: increment(ctg, iname), bg='lightgreen', fg='black', font=bold_font)
            increment_button.pack(side="left", padx=5)
            
            decrement_button = tk.Button(frame, text="-", command=lambda ctg=category, iname=item_name: decrement(ctg, iname), bg='lightcoral', fg='black', font=bold_font)
            decrement_button.pack(side="left", padx=5)

    # Checkout button on the menu page
    checkout_button = tk.Button(menu_window, text="Checkout", command=checkout, bg='mediumslateblue', fg='white', font=bold_font)
    checkout_button.pack(pady=20)

# Button on the root window to open the menu page
open_menu_button = tk.Button(root, text="Open Menu", command=open_menu, bg='darkblue', fg='white', font=heading_font)
open_menu_button.pack(pady=50)

root.mainloop()
