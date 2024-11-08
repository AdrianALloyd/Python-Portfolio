


weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} } 
#welcome message

#user input, ask for city of forecast wanted

#get the weather data (hardcoded)

#display weather data, current temp, weather conditions eg sunny and rainy, windspeed, humidity

#data validation, make sure the user enters a valid city

#thank you message for using the application



print("Welcome to 4cast")

def display(user_city):
    city = user_city.title()
    try:
        temp = weather_data[city]["temperature"]
        conditions = weather_data[city]["conditions"]
        wind = weather_data[city]["wind_speed"]
        humid = weather_data[city]["humidity"]
        print(f"The weather for {city} is:\nTemperature: {temp}\nConditions: {conditions}\nWind speed: {wind}\nHumidity: {humid}\n")
    except KeyError:
        print("An error has occurred, data unavailable or misspelled")


def list():
    print("Cities:")
    for x in weather_data:
        print(x)


list()
user_city = input("Please enter the city name you want the forcast for:\n")

display(user_city)

while True:
    com =input("Please enter a command, for a list of commands type 'help'\n")

    match com:
        case "help":
            print("Available commands: \nlist - Gives a list of available cities \n'city name' - Displays the weather for the selected city \nexit - Exits the application")
        case "list":
            list()
        case "exit":
            break
        case _:
            display(com)


print("Thank you for using 4cast")
