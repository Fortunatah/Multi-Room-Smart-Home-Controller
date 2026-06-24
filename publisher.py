#######################
#                     # 
#     Publisher.py    #
# by Hayden Fortunata #
#     Ver 1.0         #
#                     #
#######################


## IMPORTS ##

import serial
import time
import paho.mqtt.client as mqtt
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes


## VARIABLES ##
ser = serial.Serial('/dev/ttyACM0', 9600)
## Initialize the client in MQTT 5 format
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
client.connect("localhost", 1883)
client.loop_start()
LONG_TOPIC = "home/sandown/climate/data"

## FUNCTIONS ##
def get_room( line ):
    ## see what room we are dealing with
    if "bedRoom" in line: return "bedRoom"
    elif "livingRoom" in line: return "livingRoom"

## START PROCESS ##

print("Pi Publisher running. Grabing data from living room and bedroom...")

try:
    while True:
        if ser.in_waiting > 0: # checks if data is available before trying to read it
            line = ser.readline().decode('utf-8').rstrip()
            if line:
                room = get_room(line) ## get the room for publishing
                
                temperature = float(line[(line.find(">")) + 1:])
                print(f"{room} == {temperature}")


except KeyboardInterrupt:
    client.loop_stop()
    ser.close()
