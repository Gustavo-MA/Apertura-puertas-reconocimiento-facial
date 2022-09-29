# Importar Bilbioteca
from deepface import DeepFace
import pandas as pd

# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/test/Carrie.jpg", db_path = "/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/DeepFace/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Seleccion")
print (df.identity[0])