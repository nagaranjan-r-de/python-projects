def view_vehicles():
    vehicles = []
    with open("data/vehicle.txt","r") as file:
        for line in file:
            data = line.strip().split(",")
            vehicle = {
                "id": int(data[0]),
                "name": data[1],
                "type": data[2],
                "source": data[3],
                "destination": data[4],
                "price": float(data[5]),
                "seats": int(data[6])
            }
            print("\n")

            vehicles.append(vehicle)

    return vehicles

def search_vehicles():
    print("naga")