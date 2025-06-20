import time
from datetime import datetime

def guest_check_in():
    print("🤖 Welcome to Hotel Robotica!")

    name = input("Please enter your name: ")
    print(f"Hello {name}. Welcome to Hotel Robotica!")

    days = int(input("How many days will you be staying? "))
    budget = float(input("Please enter your budget in USD: "))
    
    has_coupon = input("Do you have a discount coupon? (yes/no): ").lower()
    discount = 0.0
    if has_coupon == "yes":
        discount = float(input("Enter discount percentage (e.g., 10 for 10%): ")) / 100

    room_number = 100 + int(time.time()) % 900  # simple room number logic

    checkin_time = datetime.now()

    guest_data = {
        "name": name,
        "days": days,
        "budget": budget,
        "room_number": room_number,
        "checkin_time": checkin_time,
        "discount": discount
    }

    print(f"\nRoom {room_number} assigned to {name}. Check-in time: {checkin_time.strftime('%Y-%m-%d %H:%M:%S')}")
    return guest_data

def guest_check_out(guest_data):
    print("\n🤖 Processing your checkout...")

    checkout_time = datetime.now()

    # Assuming flat $100 charge per day
    base_rate = 100
    total_cost = guest_data["days"] * base_rate

    # Apply discount if any
    if guest_data["discount"] > 0:
        total_cost = total_cost * (1 - guest_data["discount"])

    print("\n🧾 Generating Invoice...")
    print("-" * 40)
    print(f"Name         : {guest_data['name']}")
    print(f"Room Number  : {guest_data['room_number']}")
    print(f"Check-In     : {guest_data['checkin_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Check-Out    : {checkout_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Stay Duration: {guest_data['days']} day(s)")
    print(f"Room Rate    : $100 per day")
    if guest_data["discount"] > 0:
        print(f"Discount     : {int(guest_data['discount'] * 100)}%")
    print(f"Total Amount : ${total_cost:.2f}")
    print("-" * 40)

def main():
    guest_info = guest_check_in()

    input("\nPress ENTER to simulate checkout...")

    guest_check_out(guest_info)

if __name__ == "__main__":
    main()
