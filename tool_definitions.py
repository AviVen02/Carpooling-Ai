from google.genai import types


search_rides_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="search_rides",
            description="Search for available carpool rides.",
            parameters={
                "type": "object",
                "properties": {
                    "source": {
                        "type": "string",
                        "description": "Starting location"
                    },
                    "destination": {
                        "type": "string",
                        "description": "Destination location"
                    },
                    "rideDate": {
                        "type": "string",
                        "description": "Ride date in YYYY-MM-DD format"
                    }
                },
                "required": [
                    "source",
                    "destination",
                    "rideDate"
                ]
            }
        )
    ]
)


my_rides_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="my_rides",
            description="Get all rides created by the currently logged-in user.",
            parameters={
                "type": "object",
                "properties": {}
            }
        )
    ]
)


my_ride_find_by_id_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="my_ride_find_by_id",
            description="Get details of a specific ride by its ride ID.",
            parameters={
                "type": "object",
                "properties": {
                    "rideId": {
                        "type": "integer",
                        "description": "The ID of the ride to retrieve."
                    }
                },
                "required": [
                    "rideId"
                ]
            }
        )
    ]
)


my_bookings_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="my_bookings",
            description="Get all bookings made by the currently logged-in user.",
            parameters={
                "type": "object",
                "properties": {}
            }
        )
    ]
)


my_cars_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="my_cars",
            description="Get all cars registered by the currently logged-in user.",
            parameters={
                "type": "object",
                "properties": {}
            }
        )
    ]
)

register_car_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="register_car",
            description="Register a new car for the currently logged-in user.",
            parameters={
                "type": "object",
                "properties": {
                    "carName": {
                        "type": "string",
                        "description": "Name of the car"
                    },
                    "carNumber": {
                        "type": "string",
                        "description": "Car number"
                    },
                    "carModel": {
                        "type": "string",
                        "description": "Model of the car"
                    },
                    "carColor": {
                        "type": "string",
                        "description": "Color of the car"
                    },
                    "carCapacity": {
                        "type": "integer",
                        "description": "Capacity of the car"
                    }
                },
                "required": [
                    "carName",
                    "carNumber",
                    "carModel",
                    "carColor",
                    "carCapacity"
                ]
            }
        )
    ]
)


create_ride_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="create_ride",
            description=(
                "Create a ride for the currently logged-in user "
                "using one of their registered cars. Call this tool "
                "only after the user confirms the ride details."
            ),
            parameters={
                "type": "object",
                "properties": {
                    "carId": {
                        "type": "integer",
                        "description": (
                            "ID of the user's registered car, "
                            "retrieved from my_cars"
                        )
                    },
                    "source": {
                        "type": "string",
                        "description": "Ride starting location"
                    },
                    "destination": {
                        "type": "string",
                        "description": "Ride destination"
                    },
                    "rideDate": {
                        "type": "string",
                        "description": "Ride date in YYYY-MM-DD format"
                    },
                    "rideTime": {
                        "type": "string",
                        "description": "Ride time in HH:MM:SS format"
                    },
                    "price": {
                        "type": "number",
                        "description": "Price of the ride; must be at least 1"
                    }
                },
                "required": [
                    "carId",
                    "source",
                    "destination",
                    "rideDate",
                    "rideTime",
                    "price"
                ]
            }
        )
    ]
)

book_ride_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="book_ride",
            description=(
                "Book a ride for the authenticated user. "
                "Use only a rideId returned by search_rides. "
                "Call this tool only after the user explicitly "
                "confirms the selected ride and booking details."
            ),
            parameters={
                "type": "object",
                "properties": {
                    "rideId": {
                        "type": "integer",
                        "description": (
                            "The ID of the ride to book, "
                            "retrieved from search_rides"
                        )
            }
        },
        "required": [
            "rideId"
        ]
    }
        )

    ]
)

cancel_booking_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="cancel_booking",
            description=(
                "Cancel a booking for the authenticated user. "
                "Use only a bookingId returned by my_bookings."
            ),
            parameters={
                "type": "object",
                "properties": {
                    "bookingId": {
                        "type": "integer",
                        "description": (
                            "The ID of the booking to cancel, "
                            "retrieved from my_bookings"
                        )
                    }
                },
                "required": [
                    "bookingId"
                ]
            }
        )
    ]
)  

cancel_ride_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="cancel_ride",
            description=(
                "Cancel a ride for the authenticated user. "
                "Use only a rideId returned by my_rides."
            ),
            parameters={
                "type": "object",
                "properties": {
                    "rideId": {
                        "type": "integer",
                        "description": (
                            "The ID of the ride to cancel, "
                            "retrieved from my_rides"
                        )
                    }
                },
                "required": [
                    "rideId"
                ]
            }
        )
    ]
)  

update_ride_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="update_ride",
            description=(
                "Update a ride for the authenticated user. "
                "Use only a rideId returned by my_rides."
            ),
            parameters={
                "type": "object",
                "properties": {
                    "rideId": {
                        "type": "integer",
                        "description": (
                            "The ID of the ride to update, "
                            "retrieved from my_rides"
                        )
                    },
                    "source": {
                        "type": "string",
                        "description": "Updated starting location"
                    },
                    "destination": {
                        "type": "string",
                        "description": "Updated destination"
                    },
                    "rideDate": {
                        "type": "string",
                        "description": "Updated ride date in YYYY-MM-DD format"
                    },
                    "rideTime": {
                        "type": "string",
                        "description": "Updated ride time in HH:MM:SS format"
                    },
                    "price": {
                        "type": "number",
                        "description": (
                            "Updated price of the ride; must be at least 1"
                        )
                    }
                },
                "required": [
                    "rideId",
                    "source",
                    "destination",
                    "rideDate",
                    "rideTime",
                    "price"
                ]
            }
        )
    ]    
)

