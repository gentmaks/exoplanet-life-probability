"""
Name: Gent Maksutaj
Date: 12/08/2023
Description: This file is used to make a request to the API and get the data
                that is needed. The data is then returned to the main file.
Class: CS
"""
from pip._vendor import requests
from planets import Planet

# This class is used to make a request to the API and get the data that is needed.
class BaseRequest:
    def __init__(self, name):
        self.name = name
        self.url = "https://planets-by-api-ninjas.p.rapidapi.com/v1/planets"
        self.headers =         {
            "X-RapidAPI-Key": "fbb5454998msh4eccf9d237e1ef2p181f1fjsn122171538447",
            "X-RapidAPI-Host": "planets-by-api-ninjas.p.rapidapi.com"
        }
    """
    Description: This method is the base method for getting the data from the API.
                Parameters: self, params
                Return: response dictionary
    """
    def get_response(self, params):
        response = requests.get(self.url, headers=self.headers, params=params)
        return response.json()

# This class is used to get the data for a specific planet from the API.
class RequestWorlds(BaseRequest):
    """
    Description: This method is used to get the data from the API and return it
                    to the main file.
    Parameters: self
    Return: response_dict
    """
    def get_worlds(self):
        querystring = {"name": self.name}
        return self.get_response(querystring)

# This class is used to get the data for all the planets that satisfy the user's input.
# The data is filtered based on the user's input. The data is then returned to the main file.
class RequestPlanetsValues(BaseRequest):
    """
    Description: This method is used to get the data from the API and return it
                    to the main file.
                In this method, the data is filtered based on the user's input.
    Parameters: self
    Return: response_dict
    """
    def get_planets_values(self, query):
        planet = Planet()
        if query["mass"] != 0:
            min_mass = query["mass"] - (query["mass"] * query["range"] / 100)
            max_mass = query["mass"] + (query["mass"] * query["range"] / 100)
            planet.set_min_mass(min_mass)
            planet.set_max_mass(max_mass)
        if query["radius"] != 0:
            min_radius = query["radius"] - (query["radius"] * query["range"] / 100)
            max_radius = query["radius"] + (query["radius"] * query["range"] / 100)
            planet.set_min_radius(min_radius)
            planet.set_max_radius(max_radius)
        if query["period"] != 0:
            min_period = query["period"] - (query["period"] * query["range"] / 100)
            max_period = query["period"] + (query["period"] * query["range"] / 100)
            planet.set_min_period(min_period)
            planet.set_max_period(max_period)
        if query["temperature"] != 0:
            min_temperature = query["temperature"] - (query["temperature"] * query["range"] / 100)
            max_temperature = query["temperature"] + (query["temperature"] * query["range"] / 100)
            planet.set_min_temperature(min_temperature)
            planet.set_max_temperature(max_temperature)
        if query["distance_light_year"] != 0:
            min_distance = query["distance_light_year"] - (query["distance_light_year"] * query["range"] / 100)
            max_distance = query["distance_light_year"] + (query["distance_light_year"] * query["range"] / 100)
            planet.set_min_distance_light_years(min_distance)
            planet.set_max_distance_light_years(max_distance)
        if query["semi_major_axis"] != 0:
            min_axis = query["semi_major_axis"] - (query["semi_major_axis"] * query["range"] / 100)
            max_axis = query["semi_major_axis"] + (query["semi_major_axis"] * query["range"] / 100)
            planet.set_max_semi_major_axis(max_axis)
            planet.set_min_semi_major_axis(min_axis)
        response = self.get_response(planet.get_params())
        return response