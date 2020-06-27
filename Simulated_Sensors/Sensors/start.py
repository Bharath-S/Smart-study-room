
import threading, time
from TemperatureSensor_Node import TemperatureNode
from LdrIndoorSensor_Node import LdrIndoorNode
from LdrOutdoorSensor_Node import LdrOutdoorNode
from UltrasonicOutdoorSensor_Node import UltrasonicOutdoorSensorNode
from UltrasonicIndoorSensor_Node import UltrasonicIndoorSensorNode

print("Starting all the sensor nodes")

def Ldr1():
    LdrIndoorNode(2).start()

def Ldr2():
    LdrOutdoorNode(2).start()

def Temp():
    TemperatureNode(2).start()

def Ultr1():
    UltrasonicIndoorSensorNode(2).start()

def Ultr2():
    UltrasonicOutdoorSensorNode(2).start()

threading.Thread(target=Ldr1).start()
threading.Thread(target=Ldr2).start()
threading.Thread(target=Temp).start()
threading.Thread(target=Ultr1).start()
threading.Thread(target=Ultr2).start()
