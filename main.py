import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from datetime import date

from tool import (
    search_rides,
    my_rides,
    my_ride_find_by_id,
    my_bookings,
    my_cars,
    register_car,
    create_ride,
    book_ride,
    cancel_booking,
    cancel_ride,
    update_ride
)

from tool_definitions import (
    search_rides_tool,
    my_rides_tool,
    my_ride_find_by_id_tool,
    my_bookings_tool,
    my_cars_tool,
    register_car_tool,
    create_ride_tool,
    book_ride_tool,
    cancel_booking_tool,
    cancel_ride_tool,
    update_ride_tool
)



load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


today = date.today()

last_ride = None

chat = client.chats.create(
    model="gemini-3.5-flash-lite",

    config=types.GenerateContentConfig(

        tools=[
            search_rides_tool,
            my_rides_tool,
            my_ride_find_by_id_tool,
            my_bookings_tool,
            my_cars_tool,
            register_car_tool,
            create_ride_tool,
            book_ride_tool,
            cancel_booking_tool,
            cancel_ride_tool,
            update_ride_tool
        ],
        system_instruction=f"""
                You are a helpful carpooling assistant.

                Today's date is {today}.
                The user's latest selected ride is:{last_ride}

                When the user gives a date without a year:
                - Use the upcoming occurrence of that date.
                - Return dates in YYYY-MM-DD format.

                TOOL USAGE:
                - Use search_rides to search for available rides.
                - Use my_rides to retrieve the user's own rides.
                - Use my_ride_find_by_id to retrieve a specific ride.
                - Use my_bookings to retrieve the user's bookings.
                - Use my_cars to retrieve the user's registered cars.
                - Use register_car to register a new car.
                - Use create_ride to create a new ride.
                - Use book_ride to book a ride.
                - Use cancel_booking to cancel a booking.
                - Use cancel_ride to cancel a ride.

                RESPONSE FORMATTING:
                - Always explain tool results in clear, readable text.
                - Never return raw Python lists or raw JSON to the user.
                - For multiple rides, bookings, or cars, format each item separately.
                - Use bullet points for individual records.
                - Include relevant IDs, dates, times, prices, statuses, and other available details.
                - Format dates as DD MMM YYYY, for example 01 Nov 2026.
                - Format times in 12-hour format, for example 01:00 PM.
                - If the result is an empty list, say that no records were found.
                - Never invent missing information.
                - After receiving tool results, provide a final text answer to the user.

                RIDE CREATION RULES:
                - When the user wants to create a ride, first retrieve their registered cars using my_cars.
                - Never guess or invent a car ID. Use an ID returned by my_cars.
                - If the user has multiple cars, ask which car they want to use.
                - Collect all required ride details: source, destination, date, time, and price.
                - Convert the ride date to YYYY-MM-DD and time to HH:MM:SS.
                - Before calling create_ride, summarize the car and all ride details and ask the user for confirmation.
                - Only call create_ride after the user explicitly confirms the complete details.
                - If the user changes any detail, show the updated summary and ask for confirmation again.
                - If ride creation fails, explain the backend error without claiming success.
                - If ride creation succeeds, summarize the actual details returned by the backend.

                RIDE BOOKING RULES:
                - When a user wants to book a ride, use search_rides if the selected ride is not already available in the current conversation context.
                - Use only a real rideId returned by the backend.
                - Never invent or guess a rideId.
                - If multiple rides match, ask the user which onethey want to book.
                - Show the selected ride's actual details returned by the backend.
                - Ask the user to explicitly confirm the booking.
                - Call book_ride only after explicit confirmation.
                - If the user changes the selected ride, show the updated details and ask for confirmation again.
                - If booking fails, explain the actual backend error.
                - If booking succeeds, summarize the actual booking response returned by the backend.
                - Never claim a booking succeeded without a successful backend response.
                - Never retry a failed booking blindly.

                CANCELLATION RULES:
                - When a user wants to cancel a booking, use my_bookings to retrieve their current bookings.
                - Show the actual booking details returned by the backend. 
                - Ask the user to explicitly confirm the cancellation.
                - Call cancel_booking only after explicit confirmation.
                - If cancellation fails, explain the actual backend error.
                - If cancellation succeeds, summarize the actual cancellation response returned by the backend.
                - Never claim a cancellation succeeded without a successful backend response.
                - Never retry a failed cancellation blindly.
                - When a user wants to cancel a ride, use my_rides to retrieve their current rides.
                - Show the actual ride details returned by the backend.
                - Ask the user to explicitly confirm the cancellation.
                - Call cancel_ride only after explicit confirmation.    
                """
    )
)



while True:

    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    

    # Send the user's message to Gemini
    response = chat.send_message(
        message=user_message
    )

    # Continue until Gemini returns a normal text answer
    while True:

        # Find whether Gemini requested a tool
        function_call = None

        for part in response.candidates[0].content.parts:

            if part.function_call:
                function_call = part.function_call
                break

        # If no tool was requested, display Gemini's answer
        if function_call is None:

            print("\nAI:")
            print(response.text)
            break

        print("\nTool requested:", function_call.name)

        # Execute the requested Python function
        if function_call.name == "search_rides":

            source = function_call.args["source"]
            destination = function_call.args["destination"]
            rideDate = function_call.args["rideDate"]

            result = search_rides(
                source,
                destination,
                rideDate
            )
            if result:
                last_ride = result[0]
                print("Remembered ride:", last_ride["rideId"])


        elif function_call.name == "register_car":

            carName = function_call.args["carName"]
            carNumber = function_call.args["carNumber"]
            carModel = function_call.args["carModel"]
            carColor = function_call.args["carColor"]
            carCapacity = function_call.args["carCapacity"]

            result = register_car(carName,carNumber,carModel,carColor,carCapacity)

        elif function_call.name == "my_rides":

            result = my_rides()

        elif function_call.name == "my_ride_find_by_id":

            rideId = function_call.args["rideId"]

            result = my_ride_find_by_id(rideId)

        elif function_call.name == "my_bookings":

            result = my_bookings()

        elif function_call.name == "my_cars":

            result = my_cars()

        elif function_call.name == "create_ride":

            source = function_call.args["source"]
            destination = function_call.args["destination"]
            rideDate = function_call.args["rideDate"]
            rideTime = function_call.args["rideTime"]
            price = function_call.args["price"]
            carId = function_call.args["carId"]

            result = create_ride(
                carId,
                source,
                destination,
                rideDate,
                rideTime,
                price
            )

        elif function_call.name == "book_ride":

            ride_id = function_call.args["rideId"]

            result = book_ride(ride_id) 

        elif function_call.name == "cancel_booking":

            booking_id = function_call.args["bookingId"]

            result = cancel_booking(booking_id)

        elif function_call.name == "cancel_ride":

            ride_id = function_call.args["rideId"]

            result = cancel_ride(ride_id)

        elif function_call.name == "update_ride":  
             
            ride_id = function_call.args["rideId"]
            source = function_call.args.get("source")
            destination = function_call.args.get("destination")
            rideDate = function_call.args.get("rideDate")
            rideTime = function_call.args.get("rideTime")
            price = function_call.args.get("price")

            result = update_ride(
                ride_id,
                source,
                destination,
                rideDate,
                rideTime,
                price
            )

        else:

            result = {
                "error": f"Unknown tool: {function_call.name}"
            }

        print("\nTool result:")
        print(result)

        # Send the tool result back to Gemini
        tool_response = types.Part.from_function_response(
            name=function_call.name,
            response={
                "result": result
            }
        )

        response = chat.send_message(
            message=tool_response
        )