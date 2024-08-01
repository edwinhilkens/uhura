import paho.mqtt.client as mqtt #import the client1
import time
import json
import requests

broker_address="192.168.1.6"
bathroom_player_address="192.168.1.29"
rflink_address="192.168.1.6"

def on_message(client, userdata, message):
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

    m_decode=str(message.payload.decode("utf-8","ignore"))
    print("data Received",m_decode)
    m_in=json.loads(m_decode) #decode json data
    action = m_in["action"]

    match message.topic:

        case "zigbee2mqtt/house/kitchen/shutter":
            match action:

                case "1_single":
                    print("1 single")

                case "2_single":
                    print("2 single")
                
                case "1_double":
                    print("1 double")

                case "2_double":
                    print("2 double")

        case "zigbee2mqtt/house/bathroom/player":

            r =  "http://" + bathroom_player_address + "/httpapi.asp?command="

            match action:

                case ["1_single" | "2_single" | "3 single" | "4_single"]:
                    print("single")
                    r = r + "MCUKeyShortClick" + action[0]
                    #x = requests.get(r)
                
                case ["1_double" | "2_double" | "3_double" | "4_double"]:
                    print("double")
                    r = r + "SetPlayerCmd:stop"
                    #x = requests.get(r)

        case "zigbee2mqtt/house/living/shutterlights":
            print("shutterlights")

    
    print("######################################################################", flush=True)

def on_connect(mqttc, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code))

def on_subscribe(mqttc, obj, mid, reason_code_list, properties):
    print("Subscribed: " + str(mid) + " " + str(reason_code_list))


def on_log(mqttc, obj, level, string):
    print(string)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

client.connect(broker_address) #connect to broker
client.publish("zigbee2mqtt/foo","OFF")#publish
client.subscribe("zigbee2mqtt/house/#")

client.loop_forever() 
