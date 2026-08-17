from cart import cart


def view_cart():

    if not cart:
        print("\nCart is empty.")
        return

    try:
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

    except KeyError as error:
        print(f"Cart data is missing the key: {error}")

    else:
        print("------------------------------")
        print(f"Grand Total: ₹{grand_total}")


def checkout():

    if not cart:
        print("\nCart is empty.")
        return

    try:
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

    except KeyError as error:
        print(f"Cart data is missing the key: {error}")
        return

    else:
        print("------------------------------")
        print(f"Grand Total: ₹{grand_total}")

        confirm = input(
            "Confirm order? (y/n): "
        ).strip().lower()

        if confirm == "y":
            print("\nOrder placed successfully!")
            print(f"Total amount: ₹{grand_total}")

            cart.clear()

        elif confirm == "n":
            print("Checkout cancelled.")

        else:
            print("Invalid choice. Please enter y or n.")