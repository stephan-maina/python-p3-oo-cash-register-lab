#!/usr/bin/env python3

from cash_register import CashRegister

# Create a CashRegister instance with a 10% discount
register = CashRegister(10)

# Add items to the cash register
register.add_item("Apple", 1.99)
register.add_item("Banana", 0.99, 3)
register.add_item("Orange", 2.49)

# Calculate and apply the discount
discounted_total = register.apply_discount()
if discounted_total is not None:
    print(f"Total after discount: ${discounted_total:.2f}")
else:
    print("No discount applied.")

# Void the last transaction
register.void_last_transaction()

# Display the final total and items
print(f"Final Total: ${register.total:.2f}")
print("Items:")
for item in register.items:
    print(f"{item['name']}: ${item['price']:.2f} x {item['quantity']}")

# Attempt to void another transaction (should have no effect)
register.void_last_transaction()

      
