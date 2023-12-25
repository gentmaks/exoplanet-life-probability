"""
Name: Gent Maksutaj
Date: 12/08/2023
Description: This file contains the Planet class, which is used to store the
                information about a planet. It also contains the get_params
                method, which returns a dictionary of the parameters of the
                planet that are not 0.
Class: CS
"""

# Planet class
class Planet:
    # Init method
    def __init__(self):
        self.name = ""
        self.min_mass = 0.0
        self.max_mass = 0.0
        self.min_radius = 0.0
        self.max_radius = 0.0
        self.min_period = 0.0
        self.max_period = 0.0
        self.min_semi_major_axis = 0.0
        self.max_semi_major_axis = 0.0
        self.min_temperature = 0.0
        self.max_temperature = 0.0
        self.min_distance_light_years = 0.0
        self.max_distance_light_years = 0.0

    # Getters and setters
    def get_name(self):
        return self.name
    
    def get_min_mass(self):
        return self.min_mass
    
    def get_max_mass(self):
        return self.max_mass
    
    def get_min_radius(self):
        return self.min_radius
    
    def get_max_radius(self):
        return self.max_radius
    
    def get_min_period(self):
        return self.min_period
    
    def get_max_period(self):
        return self.max_period
    
    def get_min_semi_major_axis(self):
        return self.min_semi_major_axis
    
    def get_max_semi_major_axis(self):
        return self.max_semi_major_axis
    
    def get_min_temperature(self):
        return self.min_temperature
    
    def get_max_temperature(self):
        return self.max_temperature
    
    def get_min_distance_light_years(self):
        return self.min_distance_light_years
    
    def get_max_distance_light_years(self):
        return self.max_distance_light_years
    
    def __str__(self):
        return self.name + " " + str(self.min_mass) + " " + str(self.max_mass) + " " + str(self.min_radius) + " " + str(self.max_radius) + " " + str(self.min_period) + " " + str(self.max_period) + " " + str(self.min_semi_major_axis) + " " + str(self.max_semi_major_axis) + " " + str(self.min_temperature) + " " + str(self.max_temperature) + " " + str(self.min_distance_light_years) + " " + str(self.max_distance_light_years)
    
    def set_name(self, name):
        self.name = name

    def set_min_mass(self, min_mass):
        self.min_mass = min_mass

    def set_max_mass(self, max_mass):
        self.max_mass = max_mass

    def set_min_radius(self, min_radius):
        self.min_radius = min_radius

    def set_max_radius(self, max_radius):
        self.max_radius = max_radius

    def set_min_period(self, min_period):
        self.min_period = min_period

    def set_max_period(self, max_period):
        self.max_period = max_period

    def set_min_semi_major_axis(self, min_semi_major_axis):
        self.min_semi_major_axis = min_semi_major_axis

    def set_max_semi_major_axis(self, max_semi_major_axis):
        self.max_semi_major_axis = max_semi_major_axis

    def set_min_temperature(self, min_temperature):
        self.min_temperature = min_temperature

    def set_max_temperature(self, max_temperature):
        self.max_temperature = max_temperature

    def set_min_distance_light_years(self, min_distance_light_years):
        self.min_distance_light_years = min_distance_light_years
    
    def set_max_distance_light_years(self, max_distance_light_years):
        self.max_distance_light_years = max_distance_light_years


    def get_params(self):
        params = {}
        if self.min_mass != 0.0:
            params['min_mass'] = self.min_mass
        if self.max_mass != 0.0:
            params['max_mass'] = self.max_mass
        if self.min_radius != 0.0:
            params['min_radius'] = self.min_radius
        if self.max_radius != 0.0:
            params['max_radius'] = self.max_radius
        if self.min_period != 0.0:
            params['min_period'] = self.min_period
        if self.max_period != 0.0:
            params['max_period'] = self.max_period
        if self.min_semi_major_axis != 0.0:
            params['min_semi_major_axis'] = self.min_semi_major_axis
        if self.max_semi_major_axis != 0.0:
            params['max_semi_major_axis'] = self.max_semi_major_axis
        if self.min_temperature != 0.0:
            params['min_temperature'] = self.min_temperature
        if self.max_temperature != 0.0:
            params['max_temperature'] = self.max_temperature
        if self.min_distance_light_years != 0.0:
            params['min_distance_light_years'] = self.min_distance_light_years
        if self.max_distance_light_years != 0.0:
            params['max_distance_light_years'] = self.max_distance_light_years
        return params