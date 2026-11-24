from data import products

cart = []


def add_to_cart(product_name, product_count):

    if not product_name:
        print("Product name cannot be empty.")
        return

    if product_count <= 0:
        print("Product count must be greater than zero.")
        return

    try:
        for product in products:

            if product_name.lower() == product["name"].lower():

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
                    f"Added {product_count} x "
                    f"{product['name']} ==> ₹{total_price}"
                )

                return

        print("Product not found.")

    except KeyError as error:
        print(f"Product data is missing the key: {error}")