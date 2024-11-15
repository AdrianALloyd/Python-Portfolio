import tkinter as tk
from tkinter import ttk
from tkinter import *

#Creates the application window
root = tk.Tk()
root.title('Weather')
root.geometry('400x200+50+50')
root.resizable(False, False)
# creates main window

#Sets a theme for the application
style = ttk.Style()
style.theme_use("clam")

#Example weather data
weather_data = { 
    "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
    "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, 
    "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
    "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
    "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} 
    } 

#Function to change data based on the selected dropdown option
def change_label(*args):
    selected= selected_option.get()

    temp = weather_data[selected]["temperature"]
    conditions = weather_data[selected]["conditions"]
    wind = weather_data[selected]["wind_speed"]
    humid = weather_data[selected]["humidity"]
    #Puts the selected weather data on the screen
    weather_display.config(text = f"The weather for {selected} is:\nTemperature: {temp}\nConditions: {conditions}\nWind speed: {wind}\nHumidity: {humid}\n")
    weather_display.pack(pady=5)

selected_option = tk.StringVar(root)
selected_option.set("London")
selected_option.trace("w", change_label)

temp = weather_data[selected_option.get()]["temperature"]
conditions = weather_data[selected_option.get()]["conditions"]
wind = weather_data[selected_option.get()]["wind_speed"]
humid = weather_data[selected_option.get()]["humidity"]

#Putting user instructions on the screen 
instruction_label = tk.Label(root, text="Please select a city from the dropdown to view weather data")
instruction_label.pack(pady=5)

#Display default city information on screen
weather_display = tk.Label(root, text = f"The weather for {selected_option.get()} is:\nTemperature: {temp}\nConditions: {conditions}\nWind speed: {wind}\nHumidity: {humid}\n")
weather_display.pack(pady= 5)

#Creates the dropdown menu
dropdown = OptionMenu(root, selected_option, *weather_data.keys())
dropdown.pack(expand=True, pady= 5)



root.mainloop()
