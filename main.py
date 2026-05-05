# Railway Reservation System
# main.py

# Total number of seats
total_seats = 50

# Dictionary to store bookings
# Format: booking_id : {name, age, seat_no}
bookings = {}

# List to track available seats
available_seats = list(range(1, total_seats + 1))

# Booking ID counter
booking_counter = 1001


def check_availability():
    print("\n--- Available Seats ---")
    print("Total Available Seats:", len(available_seats))
    print("Seat Numbers:", available_seats)


def book_ticket():
    global booking_counter

    if len(available_seats) == 0:
        print("\nSorry! No seats available.")
        return

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

    # Assign first available seat
    seat_no = available_seats.pop(0)

    booking_id = "B" + str(booking_counter)
    booking_counter += 1

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat_no": seat_no
    }

    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat_no)


def view_ticket():
    booking_id = input("Enter Booking ID: ")

    if booking_id in bookings:
        print("\n--- Ticket Details ---")
        print("Booking ID:", booking_id)
        print("Name:", bookings[booking_id]["name"])
        print("Age:", bookings[booking_id]["age"])
        print("Seat Number:", bookings[booking_id]["seat_no"])
    else:
        print("\nBooking not found!")


def cancel_ticket():
    booking_id = input("Enter Booking ID to cancel: ")

    if booking_id in bookings:
        seat_no = bookings[booking_id]["seat_no"]

        # Return seat back
        available_seats.append(seat_no)
        available_seats.sort()

        del bookings[booking_id]

        print("\nTicket Cancelled Successfully!")
        print("Seat", seat_no, "is now available again.")
    else:
        print("\nInvalid Booking ID!")


def menu():
    while True:
        print("\n========== Railway Reservation System ==========")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_availability()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            view_ticket()

        elif choice == "4":
            cancel_ticket()

        elif choice == "5":
            print("\nThank you for using Railway Reservation System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Run program
menu()
