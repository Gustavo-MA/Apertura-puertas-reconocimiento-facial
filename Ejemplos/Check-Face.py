from unittest import result
from deepface import DeepFace

print ("Se han cargado 2 imagenes para verificar que la persona sea la misma")
print ("Cargando ....")
result =DeepFace.verify(img1_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/Hugo.jpeg", img2_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/Mee.jpeg")
#result =DeepFace.verify(img1_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/carrie1.png", img2_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/carrie2.png")
print ("Resultados")
print(result)