from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display the list of available taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    """Taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
                current_taxi.start_fare()
            else:
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()
