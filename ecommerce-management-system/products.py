from data import products


def show_products():
    print("\nAvailable Products\n")

    for product in products:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ₹{product['price']} | "
            f"Stock: {product['stock']}"
        )


def search_product(search_name):
    found = False

    for product in products:
        if search_name.lower() in product["name"].lower():
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ₹{product['price']} | "
                f"Stock: {product['stock']}"
            )

            found = True

    if not found:
        print("\nProduct not found.")