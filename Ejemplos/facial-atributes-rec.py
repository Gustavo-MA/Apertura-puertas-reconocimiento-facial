from deepface import DeepFace
obj = DeepFace.analyze(img_path = "/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/carrie1.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)
print ("El resultado del analisis es:")
print (obj)