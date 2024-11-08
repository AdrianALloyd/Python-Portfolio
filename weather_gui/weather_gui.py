import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Weather')
root.geometry('400x200+50+50')
root.resizable(False, False)
# creates main window


weather_data = { 
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, 
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} 
    } 
def change_label(*args):
    selected= selected_option.get()

    temp = weather_data[selected]["temperature"]
    conditions = weather_data[selected]["conditions"]
    wind = weather_data[selected]["wind_speed"]
    humid = weather_data[selected]["humidity"]

    weather_display.config(text = f"The weather for {selected} is:\nTemperature: {temp}\nConditions: {conditions}\nWind speed: {wind}\nHumidity: {humid}\n")
    weather_display.pack(pady=5)

selected_option = tk.StringVar(root)
selected_option.set("London")
selected_option.trace("w", change_label)

temp = weather_data[selected_option.get()]["temperature"]
conditions = weather_data[selected_option.get()]["conditions"]
wind = weather_data[selected_option.get()]["wind_speed"]
humid = weather_data[selected_option.get()]["humidity"]



instruction_label = tk.Label(root, text="Please select a city from the dropdown to view weather data")
instruction_label.pack(pady=5)


weather_display = tk.Label(root, text = f"The weather for {selected_option.get()} is:\nTemperature: {temp}\nConditions: {conditions}\nWind speed: {wind}\nHumidity: {humid}\n")
weather_display.pack(pady= 5)



dropdown = OptionMenu(root, selected_option, *weather_data.keys())
dropdown.pack(expand=True, pady= 5)








# def display(user_city):
#     city = user_city.title()
#     try:
#         temp = weather_data[city]["temperature"]
#         conditions = weather_data[city]["conditions"]
#         wind = weather_data[city]["wind_speed"]
#         humid = weather_data[city]["humidity"]
#         print(f"The weather for {city} is:\nTemperature: {temp}\nConditions: {conditions}\nWind speed: {wind}\nHumidity: {humid}\n")
#     except KeyError:
#         print("An error has occurred, data unavailable or misspelled")


# def list():
#     print("Cities:")
#     for x in weather_data:
#         print(x)


# list()
# user_city = input("Please enter the city name you want the forcast for:\n")

# display(user_city)

# while True:
#     com =input("Please enter a command, for a list of commands type 'help'\n")

#     match com:
#         case "help":
#             print("Available commands: \nlist - Gives a list of available cities \n'city name' - Displays the weather for the selected city \nexit - Exits the application")
#         case "list":
#             list()
#         case "exit":
#             break
#         case _:
#             display(com)

















root.mainloop()
