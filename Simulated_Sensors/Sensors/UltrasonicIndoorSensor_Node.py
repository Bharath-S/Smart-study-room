import time
from  datetime import datetime
import json
import paho.mqtt.client as mqtt
from UltrasonicIndoorSensor import UltrasonicIndoorSensor


class UltrasonicIndoorSensorNode:

    def __init__(self, interval):
        self.interval = interval
        self.prev_Value = False
        self.isFirstMsg = True

    def start(self):
        print("Started {}".format("UltrasonicIndoorSensor"))
        ts = UltrasonicIndoorSensor(0.8)
        mqtt_pub = mqtt.Client("Ultrasonic Indoor signal publisher")
        mqtt_pub.connect("127.0.0.1", 1883, 70)
        mqtt_pub.loop_start()

        while True:
            curr_Value = ts.sense()
            if self.isFirstMsg==True or self.prev_Value != curr_Value:
                self.isFirstMsg = False
                self.prev_Value = curr_Value
                dt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
                message = {
                    "type-id":"de.uni-stuttgart.iaas.sc.simulated/"+ ts.sensor_type,
                    "instance-id":ts.instance_id,
                    "timestamp":dt,
                    "value":{
                        ts.unit: curr_Value
                    }
                }
                jmsg = json.dumps(message, indent = 4)
                mqtt_pub.publish("u38/room/" + ts.sensor_type + "/" + ts.instance_id,
                                   jmsg,2)
            time.sleep(self.interval)
            time.sleep(self.interval)

#UltrasonicIndoorSensorNode(2).start()
