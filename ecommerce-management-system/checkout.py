from cart import cart

def view_cart():
    if not cart:
        print("\nCart is empty.")
        return

    print("\n========== YOUR CART ==========")

    grand_total = 0

    for item in cart:
        print(
            f"Name: {item['name']} | "
            f"Qty: {item['quantity']} | "
            f"Price: ₹{item['price']} | "
            f"Total Price: ₹{item['total']}"
        )

        grand_total += item["total"]

    print("------------------------------")
    print(f"Grand Total: ₹{grand_total}")


def checkout():

    if not cart:
        print("\nCart is empty.")
        return

    print("\n========== CHECKOUT ==========")

    grand_total = 0

    for item in cart:
        print(
            f"Name: {item['name']} | "
            f"Qty: {item['quantity']} | "
            f"Price: ₹{item['price']} | "
            f"Total Price: ₹{item['total']}"
        )

        grand_total += item["total"]

    print("------------------------------")
    print(f"Grand Total: ₹{grand_total}")

    confirm = input("Confirm order? (y/n): ").lower()

    if confirm != "y":
        print("Checkout cancelled.")
        return

    print("\nOrder placed successfully!")
    print(f"Total amount: ₹{grand_total}")

    cart.clear()