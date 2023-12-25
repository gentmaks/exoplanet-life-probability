"""
Name: Gent Maksutaj
Date: 12/08/2023
Description: This program creates a GUI that allows the user to input the attributes of a planet
and then sends a request to the API to get a list of planets that are similar to the user's input.
The program then displays a bar graph of the planets that are recommended and a 3D scatter plot
of the planets that are recommended and Earth.
Class: CS
"""
import tkinter as tk
from functools import partial
from request import RequestWorlds, RequestPlanetsValues
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import randint

def main():
    root = tk.Tk()
    earth_data = RequestWorlds("earth").get_worlds()
    root.title("Tkinter Slider Example")

    """
    Description: Function that is called when the slider is changed, prints the value of the slider.
    Parameters: value - the value of the slider
    Return: None
    """
    def on_slider_change(value):
        print("Slider value:", value)

    """
    Description: Function that calculates the probability of life on a planet based on the difference 
    between the planet's attributes and Earth's attributes.
    Parameters: planet_attributes - a dictionary of the planet's attributes
                earth_attributes - a dictionary of Earth's attributes
    Return: percentage_score - the probability of life on the planet as a percentage
    """
    def calculate_life_probability(planet_attributes, earth_attributes):
        # Define weights for each attribute
        weights = {
        'mass': 1,
        'radius': 1,
        'temperature': 2,
        'semi_major_axis': 2,
        'period': 1,
        'distance_light_year': 2
        }
        # Calculate the difference between each attribute of the planet and Earth
        for key in weights.keys():
            if planet_attributes[key] is None:
                planet_attributes[key] = earth_attributes[key]
        differences = {key: abs(planet_attributes[key] - earth_attributes[key]) for key in weights.keys()}

        # Normalize the differences
        normalized_differences = {key: diff / weights[key] for key, diff in differences.items()}

        # Calculate the total difference score
        total_difference = sum(normalized_differences.values())

        # Calculate the probability score (inverse of the total difference)
        probability_score = 5 / (1 + total_difference)

        # Ensure the probability score is within the valid range (0 to 5)
        probability_score = max(0, min(1, probability_score))
        probability_score = probability_score * 0.7

        # Convert the probability score to a percentage in the range of 1 to 100
        percentage_score = probability_score * 100
        return percentage_score

    """
    Description: Function that ignores the slider and sets its value to 0.
    Parameters: slider - the slider to ignore
    Return: None
    """
    def ignore_slider(slider):
        slider.set(0)  # Set the value to 0 to "ignore" it
        slider.configure(state=tk.DISABLED)  # Disable the slider

    """
    Description: Function that records the responses of the sliders and sends a request to the API.
    Parameters: slider_values - a list of the values of the sliders
    Return: None
    """
    def record_response(slider_values):
        recorded_response = slider_values
        query = {}
        for i in range(len(slider_name)):
            query[slider_name[i][0]] = recorded_response[i]
            
        query["range"] = recorded_response[-1]
        response_planet_recommendations = RequestPlanetsValues("earth").get_planets_values(query)
        visualize_response(response_planet_recommendations, earth_data)
        display_bar_graph(response_planet_recommendations, earth_data)

    """
    Description: Function that displays a bar graph of the planets that are recommended.
    Parameters: response_planet_recommendations - a list of the planets that are recommended
                earth_data - a dictionary of Earth's attributes
    Return: None
    """
    def display_bar_graph(response_planet_recommendations, earth_data):
        # base the bar graph on the probability score
        for planet in response_planet_recommendations:
            planet["probability_score"] = calculate_life_probability(planet, earth_data[0])
        # remove earth from the list of planets
        response_planet_recommendations = [planet for planet in response_planet_recommendations if planet["name"] != "Earth"]
        # sort the planets by probability score
        response_planet_recommendations = sorted(response_planet_recommendations, key=lambda planet: planet["probability_score"], reverse=True)

        # create a list of planet names and a list of probability scores
        planet_names = [planet["name"] for planet in response_planet_recommendations]
        probability_scores = [planet["probability_score"] for planet in response_planet_recommendations]

        # create a bar graph
        plt.figure(figsize=(14, 10))
        plt.bar(planet_names, probability_scores)
        plt.xlabel("Planet")
        plt.ylabel("Probability Score")
        plt.title("Probability of Life on Planets Similar to Earth")
        # rotate the x-axis labels
        plt.xticks(rotation=90)
        plt.show()
        return

    """
    Description: Function that visualizes the planets that are recommended.
    Parameters: response_planet_recommendations - a list of the planets that are recommended
                earth_data - a dictionary of Earth's attributes
    Return: None
    """


    def visualize_response(response_planet_recommendations, earth_data):
        fig1 = plt.figure(figsize=(14, 10))
        ax1 = fig1.add_subplot(111, projection='3d')

        fig2 = plt.figure(figsize=(14, 10))
        ax2 = fig2.add_subplot(111, projection='3d')

        fig3 = plt.figure(figsize=(15, 10))
        ax3 = fig3.add_subplot(111)

        # first draw the earth data point
        earth_mass = earth_data[0]["mass"]
        earth_radius = earth_data[0]["radius"]
        earth_period = earth_data[0]["period"]
        earth_semi_major_axis = earth_data[0]["semi_major_axis"]
        earth_temperature = earth_data[0]["temperature"]
        earth_distance_light_year = earth_data[0]["distance_light_year"]
        earth_host_star_mass = earth_data[0]["host_star_mass"]
        earth_host_star_temperature = earth_data[0]["host_star_temperature"]

        ax1.scatter(earth_mass, earth_radius, earth_period, color="blue", label="Earth")
        ax2.scatter(earth_semi_major_axis, earth_temperature, earth_distance_light_year, color="blue", label="Earth")
        ax3.scatter(earth_host_star_mass, earth_host_star_temperature, color="blue", label="Earth")

        # draw the recommended planets
        for planet in response_planet_recommendations:
            planet_mass = planet["mass"]
            planet_radius = planet["radius"]
            planet_period = planet["period"]
            planet_semi_major_axis = planet["semi_major_axis"]
            planet_temperature = planet["temperature"]
            planet_distance_light_year = planet["distance_light_year"]
            planet_host_star_mass = planet["host_star_mass"]
            planet_host_star_temperature = planet["host_star_temperature"]
            # make a 3d scatter plot
            ax1.scatter(planet_mass, planet_radius, planet_period, color=(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255), label=planet["name"])
            ax2.scatter(planet_semi_major_axis, planet_temperature, planet_distance_light_year, color=(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255), label=planet["name"])
            # make a 2d one with the last two attributes
            ax3.scatter(planet_host_star_mass, planet_host_star_temperature, color=(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255), label=planet["name"])
        ax1.set_xlabel("Mass")
        ax1.set_ylabel("Radius")
        ax1.set_zlabel("Period")
        ax1.set_title("Similar Planets to Earth in Terms of Mass, Radius, and Period")
        ax2.set_xlabel("Semi Major Axis")
        ax2.set_ylabel("Temperature")
        ax2.set_zlabel("Distance Light Year")
        ax2.set_title("Similar Planets to Earth in Terms of Semi Major Axis, Temperature, and Distance Light Year")
        #move the legend to the left side
        ax1.legend(loc='upper left', bbox_to_anchor=(-0.2, 1.0))
        ax2.legend(loc='upper left', bbox_to_anchor=(-0.2, 1.0))
        ax3.set_xlabel("Host Star Mass")
        ax3.set_ylabel("Host Star Temperature")
        ax3.set_title("Similar Planets to Earth in Terms of Host Star Mass and Host Star Temperature")
        ax3.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.0))
        plt.show()
        return

    slider_list = []
    slider_name = [("mass", 0.001, 0.006), ("radius", 0.04, 0.14), ("period", 0 , 4000), ("semi_major_axis", 0 , 10 ), ("temperature", 100, 500), ("distance_light_year", 0, 200)]
    for i  in range(6):
        frame = tk.Frame(root)
        frame.pack()

        slider = tk.Scale(frame, from_=slider_name[i][1], to=slider_name[i][2], orient=tk.HORIZONTAL, length=1000, label=slider_name[i][0],
                        showvalue=0, tickinterval=20, resolution=(slider_name[i][2] - slider_name[i][1])/ 50, command=on_slider_change)
        slider.set(earth_data[0][slider_name[i][0]])
        slider.pack(side=tk.LEFT)

        ignore_button = tk.Button(frame, text="Ignore", command=partial(ignore_slider, slider))
        ignore_button.pack(side=tk.RIGHT)
        slider_list.append(slider)



    range_slider_frame = tk.Frame(root)
    range_slider_frame.pack()

    range_slider = tk.Scale(range_slider_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=200, label="Range",
                            showvalue=0, tickinterval=20, resolution=1, command=on_slider_change)
    range_slider.pack(side=tk.LEFT)

    slider_list.append(range_slider)

    record_button = tk.Button(root, text="Record Response", command=lambda: record_response([slider.get() if slider.cget("state") != "disabled" else 0 for slider in slider_list]))
    record_button.pack()

    root.mainloop()

if __name__ ==  "__main__" :
    main()