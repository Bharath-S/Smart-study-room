from random import random

class LdrOutdoorSensor:
    sensor_type = "lightOutdoor"
    unit = "celsius"
    instance_id = "1"

    def __init__(self, average_light_Intensity, light_Intensity_variation, min_intensity, max_intensity):
        self.average_light_Intensity = average_light_Intensity
        self.light_Intensity_variation = light_Intensity_variation
        self.min_intensity = min_intensity
        self.max_intensity = max_intensity
        self.value = 0.0


    def sense(self):
        self.value = self.value + self.simple_random()
        return self.value

    def simple_random(self):
        value = self.min_intensity + (random() * (self.max_intensity - self.min_intensity))
        return value

    def complex_random(self):
        value = self.average_light_Intensity * (1 + (self.light_Intensity_variation/100) * (3*random() -1))
        value = max(value, self.min_intensity)
        value = min(value, self.max_intensity)
        return value
        
