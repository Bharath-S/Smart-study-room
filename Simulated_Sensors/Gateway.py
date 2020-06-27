import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):

    print("Message topic {}".format(message.topic))
    print("Message payload")
    print(json.loads(message.payload.decode()))
    mqtt_pub.publish("U38Gateway", message,2)

mqtt_sub =  mqtt.Client("Sensors ECUs Subscriber")
mqtt_sub.on_message = on_message

mqtt_sub.connect("127.0.0.1", 1883, 70)
mqtt_sub.subscribe("u38/#", qos=2)

mqtt_pub = mqtt.Client("Gateway Messages")
mqtt_pub.connect("127.0.0.2", 1883, 71)
mqtt_pub.loop_start()

mqtt_sub.loop_forever()
