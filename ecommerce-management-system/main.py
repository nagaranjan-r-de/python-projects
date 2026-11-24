from products import show_products, search_product
from cart import add_to_cart, remove_from_cart
from checkout import view_cart, checkout


def main():
    while True:
        print("========================================")
        print("       PYTHON E-COMMERCE SYSTEM")
        print("========================================")

        print("\nWelcome to our store!")

        print("\n")

        print("1. View Products")
        print("2. Search Product")
        print("3. Add Product to Cart")
        print("4. View Cart")
        print("5. Remove Product from Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_products()

        elif choice == "2":
            search_name = input("Enter product to search : ").strip()
            try:    
                search_product(search_name)
            except Exception as error:
                print(f"Error while searching product: {error}")
            else:
                print("Searching name ...")


        elif choice == "3":
            product_name = input("Enter product to add to cart: ")
            try:
                product_count = int(input("Enter number of products to add: "))
                add_to_cart(product_name, product_count)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "4":
            try:
                view_cart()
            except Exception as error:
                print(f"Error while viewing cart: {error}")

        elif choice == "5":
            try:
                remove_from_cart()
            except Exception as error:
                print(f"Error while removing product: {error}")

        elif choice == "6":
            try:
                checkout()
            except Exception as error:
                print(f"Checkout error: {error}")


        elif choice == "7":
            print("\nThank you for using the E-Commerce Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
