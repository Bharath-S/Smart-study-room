from random import random

class TemperatureSensor:
    sensor_type = "temperature"
    unit = "celsius"
    instance_id = "1"

    def __init__(self, average_temperature, temperature_variation, min_temp, max_temp):
        self.average_temperature = average_temperature
        self.temperature_variation = temperature_variation
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.value = 0.0


    def sense(self):
        self.value = self.value + self.simple_random()
        return self.value

    def simple_random(self):
        value = self.min_temp + (random() * (self.max_temp - self.min_temp))
        return value

    def complex_random(self):
        value = self.average_temperature * (1 + (self.temperature_variation/100) * (3*random() -1))
        value = max(value, self.min_temp)
        value = min(value, self.max_temp)
        return value
        

