import requests


def search_rides(source, destination, rideDate, jwt_token):
    print("Tool called: search_rides")
    print("Source:", source)
    print("Destination:", destination)
    print("Date:", rideDate)

    response = requests.get(
        "http://localhost:8080/api/rides/search",
        params={
            "source": source,
            "destination": destination,
            "rideDate": rideDate,
        },
        headers={
            "Authorization": f"Bearer {jwt_token}"
        },
        timeout=15,
    )

    print("Spring Boot status:", response.status_code)
    response.raise_for_status()

    return response.json()





def my_rides():

    print("My rides tool called!")

    response = requests.get(
        "http://localhost:8080/api/rides/myrides",
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)
    print("Spring Boot calling my rides api")

    return response.json()


def my_ride_find_by_id(ride_id):

    print("My ride find by id tool called!")

    response = requests.get(
        f"http://localhost:8080/api/rides/{ride_id}",
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)

    return response.json()


def my_bookings():

    print("My bookings tool called!")

    response = requests.get(
        "http://localhost:8080/api/bookings/mybookings",
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)

    return response.json()


def my_cars():

    print("My cars tool called!")

    response = requests.get(
        "http://localhost:8080/api/cars/mycars",
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)

    return response.json()


def register_car(carName,carNumber,carModel,carColor,carCapacity):

    print("Tool called!")
    print("Car Name:", carName)
    print("Car Number:", carNumber)
    print("Car Model:", carModel)
    print("Car Color:", carColor)
    print("Car Capacity:", carCapacity)

    response = requests.post(
        "http://localhost:8080/api/cars",
        json={
            "carName": carName,
            "carNumber": carNumber,
            "carModel": carModel,
            "carColor": carColor,
            "capacity": carCapacity
        },
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)
    print("Spring Boot calling register car api")

    return response.json()


def create_ride(carId, source, destination, rideDate, rideTime, price):

    print("Tool called: create_ride")
    print("Car ID:", carId)
    print("Source:", source)
    print("Destination:", destination)
    print("Date:", rideDate)
    print("Time:", rideTime)
    print("Price:", price)

    response = requests.post(
        f"http://localhost:8080/api/rides/cars/{carId}",
        json={
            "source": source,
            "destination": destination,
            "rideDate": rideDate,
            "rideTime": rideTime,
            "price": price
        },
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)

    return response.json()



def book_ride(ride_id):

    print("Tool called: book_ride")
    print("Ride ID:", ride_id)

    response = requests.post(
        f"http://localhost:8080/api/bookings/rides/{ride_id}",
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)
    print("Spring Boot calling book ride api")

    return response.json()

def cancel_booking(booking_id):

    print("Tool called: cancel_booking")
    print("Booking ID:", booking_id)

    response = requests.patch(
        f"http://localhost:8080/api/bookings/{booking_id}/cancel",
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)
    print("Spring Boot calling cancel booking api")

    return response.json()

def cancel_ride(ride_id):

    print("Tool called: cancel_ride")
    print("Ride ID:", ride_id)

    response = requests.patch(
        f"http://localhost:8080/api/rides/{ride_id}/cancel",
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)
    print("Spring Boot calling cancel ride api")

    return response.json()


def updated_ride(ride_id, source, destination, rideDate, rideTime, price):

    print("Tool called: updated_ride")
    print("Ride ID:", ride_id)
    print("Source:", source)
    print("Destination:", destination)
    print("Date:", rideDate)
    print("Time:", rideTime)
    print("Price:", price)

    response = requests.put(
        f"http://localhost:8080/api/rides/{ride_id}",
        json={
            "source": source,
            "destination": destination,
            "rideDate": rideDate,
            "rideTime": rideTime,
            "price": price
        },
        headers={
            "Authorization": f"Bearer {JWT_TOKEN}"
        }
    )

    print("Spring Boot status:", response.status_code)

    return response.json()