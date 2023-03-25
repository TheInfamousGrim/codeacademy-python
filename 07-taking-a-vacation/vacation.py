def answer():
    return 42


# Get the total cost of the hotel after x nights

def hotel_cost(nights):
    return 140 * nights

# Get the cost of the flight depending on the city

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "Not Valid"

# Work out the total car cost
    
def rental_car_cost(days):
    total_car_cost = days * 40
    if days >= 7:
        total_car_cost -= 50
    elif days >= 3:
        total_car_cost -= 20
    return total_car_cost

# Find the total cost for the trip
def trip_cost(city, days, spending_money):
    total = rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
    return total

print(trip_cost("Los Angeles", 5, 600))

