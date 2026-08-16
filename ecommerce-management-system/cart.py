from data import products

cart = []


def add_to_cart(product_name, product_count):
    for product in products:

        if product_name.lower() in product["name"].lower():

            if product_count > product["stock"]:
                print(
                    f"Only {product['stock']} units of "
                    f"{product['name']} are available."
                )
                return

            total_price = product["price"] * product_count

            cart.append(
                {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": product_count,
                    "total": total_price,
                }
            )

            print(
                f"Added {product_count} x {product['name']} "
                f"==> ₹{total_price}"
            )

            return

    print("Product not found")


def remove_from_cart():
    if not cart:
        print("\nCart is empty.")
        return

    print("\n========== CART ==========")

    for item in cart:
        print(
            f"Name: {item['name']} | "
            f"Qty: {item['quantity']} | "
            f"Price: ₹{item['price']} | "
            f"Total Price: ₹{item['total']}"
        )

    rm_name = input("\nEnter product name to remove from cart: ").strip()

    for item in cart:
        if rm_name.lower() == item["name"].lower():
            cart.remove(item)
            print(f"{item['name']} removed from cart.")
            return

    print("Product not found in cart.")
        


    
