import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, message):

    print("Message topic {}".format(message.topic))
    print("Message payload")
    print(json.loads(message.payload.decode()))


mqtt_sub =  mqtt.Client("Gateway Subscriber")
mqtt_sub.on_message = on_message

mqtt_sub.connect("127.0.0.2", 1883, 71)
mqtt_sub.subscribe("#", qos=2)


mqtt_sub.loop_forever()
