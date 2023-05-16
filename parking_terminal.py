class ParkingLot:
    def __init__(self):
        self.spots = [[None] * 20, [None] * 20]  # Initialize parking spots

    def park_vehicle(self, vehicle):
        # Find the first empty parking spot and park the vehicle there
        for i in range(2):
            for j in range(20):
                if not self.spots[i][j]:
                    self.spots[i][j] = vehicle
                    return ("A" if i == 0 else "B", j+1)  # Return the parking spot as a tuple
        return None  # Return None if the parking lot is full

    def get_parking_spot(self, vehicle_number):
        # Find the parking spot where the vehicle with the given number is parked
        for i in range(2):
            for j in range(20):
                if self.spots[i][j] and self.spots[i][j].vehicle_number == vehicle_number:
                    return ("A" if i == 0 else "B", j+1)  # Return the parking spot as a tuple
        return None  # Return None if the vehicle is not parked in the parking lot

class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

class ParkingTerminal:
    def __init__(self):
        self.parking_lot = ParkingLot()  # Initialize a ParkingLot object

    def is_vehicle_parked(self, vehicle_number):
        spot = self.parking_lot.get_parking_spot(vehicle_number)
        return spot is not None

    def park_vehicle(self, vehicle_number):
        if self.is_vehicle_parked(vehicle_number):
            print(f"Vehicle {vehicle_number} is already parked in the parking lot.")
        else:
            vehicle = Vehicle(vehicle_number)
            spot = self.parking_lot.park_vehicle(vehicle)
            if spot:
                print(f"Parking successful. Level: {spot[0]}, Spot: {spot[1]}")
            else:
                print("Parking lot is full.")

    def get_parking_spot(self, vehicle_number):
        spot = self.parking_lot.get_parking_spot(vehicle_number)
        if spot:
            print(f"Vehicle {vehicle_number} is parked at Level {spot[0]}, Spot {spot[1]}.")
        else:
            print(f"Vehicle {vehicle_number} is not parked in the parking lot.")

    def run(self):
        while True:
            print("Enter 1 to park a vehicle.")
            print("Enter 2 to retrieve parking spot of a vehicle.")
            print("Enter 3 to exit.")
            choice = input("Enter your choice: ")
            if choice == "1":
                vehicle_number = input("Enter vehicle number: ")
                self.park_vehicle(vehicle_number)
            elif choice == "2":
                vehicle_number = input("Enter vehicle number: ")
                self.get_parking_spot(vehicle_number)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")

def main():
    terminal = ParkingTerminal()
    terminal.run()

if __name__ == "__main__":
    main()

