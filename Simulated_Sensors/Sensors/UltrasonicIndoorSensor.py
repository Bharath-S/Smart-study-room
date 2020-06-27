import random

class UltrasonicIndoorSensor:
    sensor_type = "Ultrasonic_Indoor_Sensor"
    unit = "boolean"
    instance_id = "1"

    def __init__(self, prob):
        self.prob = prob
        self.value = False


    def sense(self):
        if random.random() > self.prob:
            self.value = True
        else:
            self.value = False
        return self.value

