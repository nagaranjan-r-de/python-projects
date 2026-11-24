from vehicles import view_vehicles, search_vehicles
from bookings import view_available_seats, book_ticket, cancel_ticket, view_booking, view_all_bookings
from utils import calculate_ticket_price,get_valid_choice


def display_menu():
    print("\n========================================")
    print("       BUS / TRAIN BOOKING SYSTEM")
    print("========================================")
    print("1. View Available Buses/Trains")
    print("2. Search by Source and Destination")
    print("3. View Available Seats")
    print("4. Book a Ticket")
    print("5. Cancel a Ticket")
    print("6. View Booking Details")
    print("7. View All Bookings")
    print("8. Calculate Ticket Price")
    print("9. Exit")
    print("========================================")


def main():
    while True:
        display_menu()

        choice = int(input("Enter U'r choice: "))

        if choice == 1:
            vehicles = view_vehicles()
            for vehicle in vehicles:
                print(vehicle)

        elif choice == 2:
            search_vehicles()

        elif choice == 3:
            view_available_seats()

        elif choice == 4:
            book_ticket()

        elif choice == 5:
            cancel_ticket()

        elif choice == 6:
            view_booking()

        elif choice == 7:
            view_all_bookings()

        elif choice == 8:
            calculate_ticket_price()

        elif choice == 9:
            print("\nThank you for using the Bus/Train Booking System!")
            break

        else:
            get_valid_choice()

if __name__ == "__main__":
    main()