# Importar Bilbioteca
from deepface import DeepFace
import pandas as pd
# python 3.6
import random
import time
from paho.mqtt import client as mqtt_client
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("img_src", help="Imagen a buscar en la DB del caras")
parser.add_argument("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

#Variables y constantes
#Datos del broker
broker = '127.0.0.1'
port = 1883
topic = "codigoIoT/mqtt/python"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

#Definicion de funciones
#Conexion al Broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

#Publicador
def publish2(client, mensaje):
    #msg_count = 0
    #while True:
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    print(result)
    # result: [0, 1]
    status = result[0]
    if status == 0:
         print(f"Send `{msg}` to topic `{topic}`")
    else:
         print(f"Failed to send message to topic {topic}")
    #msg_count += 0

# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find(img_path = args.img_src, db_path = args.db_path, enforce_detection = "false")
print ("Resultado ")
print (df)
json_view=df.to_json(orient="index")
print ("Seleccion")
print(json_view)
#print (df.identity[0])

client = connect_mqtt()
client.loop_start()
print ("Enviando mensaje")
#publish2(client, df.identity[0])
publish2(client, json_view)
print ("mensaje Enviado!")