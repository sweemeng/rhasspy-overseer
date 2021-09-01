import json

import paho.mqtt.client as mqtt
import get_time
import set_light

def on_connect(client, userdata, flags, rc):
    client.subscribe("hermes/intent/#")
    client.subscribe("hermes/nlu/intentNotRecognized")
    print("Connected, waiting for event")


def on_disconnect(client, userdata, rc):
    client.reconnect()


def on_message(client, userdata, msg):
    nlu_payload = json.loads(msg.payload)
    if msg.topic == "hermes/nlu/intentNotRecognized":
        sentence = "Unrecognized command"
        print("Recognition failure")
    elif msg.topic == "hermes/intent/GetTime":
        print("Got intent:", nlu_payload["intent"]["intentName"])
        time_sentence = get_time.say() 
        print(time_sentence)
        sentence = f"It is now {time_sentence}"
    elif msg.topic == "hermes/intent/ChangeLightState":
        print("Got intent:", nlu_payload["intent"]["intentName"])
        topic, state = set_light.set_light(nlu_payload)
        client.publish(topic, state)
        sentence = "Acknowledged"
    else:
        print("Got intent:", nlu_payload["intent"]["intentName"])
        sentence = nlu_payload["input"]
    site_id = nlu_payload["siteId"]
    client.publish("hermes/tts/say", json.dumps({"text": sentence, "siteId": site_id}))


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.username_pw_set(username="username",password="password")
    client.connect("localhost", 1883)
    client.loop_forever()


if __name__ == "__main__":
    main()
