menu = {
    'samosa': 15,
    'chai': 10,
    'sandwich': 30,
    'noodles': 50,
    'thali': 100,
    'juice': 25,
}

print("Welcome to my canteen. Please place your order")

order = {}

for item, price in menu.items():
    print(f"{item.capitalize()} : {price} Rs")

while True:
    item = input("Please enter the item you want to order").strip().lower()

    if item in menu:
        quantity = input("Enter the quantity of the item")
        if quantity.isdigit() and int(quantity)>0:
            quantity = int(quantity)
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
                print(f"Order of {item.capitalize()} is added to your cart with quantity {quantity}")
        else:
            print("Enter a valid quantity")

    cont = input("Do you want to order another item? (yes/no): ").strip().lower()
    if cont != 'yes':
        break

# Final Bill
print("\n----- Your Bill -----")
subtotal = 0
for item, qty in order.items():
    cost = menu[item] * qty
    print(f"{item.capitalize()} x {qty} = {cost} Rs")
    subtotal += cost

gst = round(subtotal * 0.05, 2)
total = subtotal + gst

print(f"\nSubtotal: {subtotal} Rs")
print(f"GST (5%): {gst} Rs")
print(f"Total: {total} Rs")
print("\nThank you for ordering from Smart Canteen!")