import time
from  datetime import datetime
import json
import paho.mqtt.client as mqtt
from LdrIndoorSensor import LdrIndoorSensor


class LdrIndoorNode:

    def __init__(self, interval):
        self.interval = interval

    def start(self):
        print("Started {}".format("LdrIndoorNode"))
        ts = LdrIndoorSensor(20,30,16,35)
        mqtt_pub = mqtt.Client("Indoor light publisher")
        mqtt_pub.connect("127.0.0.1", 1883, 70)
        mqtt_pub.loop_start()

        while True:
            dt = datetime.now().strftime("%d-%m-%YT%H:%M:%S")
            message = {
                "type-id":"de.uni-stuttgart.iaas.sc.simulated/"+ ts.sensor_type,
                "instance-id":ts.instance_id,
                "timestamp":dt,
                "value":{
                    ts.unit: ts.sense()
                }
            }
            jmsg = json.dumps(message, indent = 4)
            mqtt_pub.publish("u38/room/" + ts.sensor_type + "/" + ts.instance_id,
                                   jmsg,2)
            time.sleep(self.interval)

#LdrIndoorNode(2).start()
