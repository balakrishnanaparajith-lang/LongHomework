class Hotel:
    def __init__(self):
        self.rooms = {
            101: "Empty",
            102: "Empty",
            103: "Empty",
            104: "Empty",
            105: "Empty"
        }

        self.guests = {}
    def show_available_rooms(self):
        print("\n--- Available Rooms ---")
        for room, status in self.rooms.items():
            if status == "Empty":
                print(f"Room {room} is available")
        print()

    def book_room(self):
        name = input("Enter guest name: ")
        room = int(input("Enter room number to book: "))
        days = int(input("Enter number of days: "))

        if room not in self.rooms:
            print("Invalid room number\n")
            return

        if self.rooms[room] == "Empty":
            self.rooms[room] = "Booked"
            self.guests[name] = {"room": room, "days": days}
            print(f"{name} booked room {room} for {days} days\n")
        else:
            print(f"Room {room} is already booked\n")

    def cancel_booking(self):
        name = input("Enter guest name to cancel booking: ")

        if name in self.guests:
            room = self.guests[name]["room"]
            self.rooms[room] = "Empty"
            del self.guests[name]
            print(f"Booking cancelled for {name}\n")
        else:
            print("Guest not found\n")

    def show_unique_guests(self):
        print("\n--- Unique Guests ---")
        for guest in self.guests.keys():
            print(guest)
        print()

    def calculate_bill(self):
        name = input("Enter guest name: ")

        if name in self.guests:
            days = self.guests[name]["days"]
            price_per_day = 200
            total = days * price_per_day
            print(f"Total bill for {name} is {total} AED\n")
        else:
            print("Guest not found\n")


hotel = Hotel()
while True:
    print("1. Show available rooms")
    print("2. Book room")
    print("3. Cancel booking")
    print("4. Show unique guests")
    print("5. Calculate bill")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        hotel.show_available_rooms()
    elif choice == "2":
        hotel.book_room()
    elif choice == "3":
        hotel.cancel_booking()
    elif choice == "4":
        hotel.show_unique_guests()
    elif choice == "5":
        hotel.calculate_bill()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")

