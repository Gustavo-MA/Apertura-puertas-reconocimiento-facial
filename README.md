# Apertura-puertas-reconocimiento-facial
Ejemplos: Apertura-puertas-reconocimiento-facial

Introduccion
En este trabajo se estudia el reconocimiento de Rostror por medio de la biblioteca deeFace
Para ello etnemos que instalar los complementos de importacion ded biblioteca que vienen en material necesario.
Se lograra realizar el estado de animo de una persona mediante una imagen
y la comparacion de dos rostros en de diferente imagen.


Material Necesario

Se necesitara Visual StudioCode
y descargar las bibliotecas del paquete deepFace  en la siguiente
pagina: https://github.com/serengil/deepface


Para que el programa funcione , se deben instalar los siguientes requisitos:

* gustavo@gustavo-VirtualBox:~$ sudo apt-get python3-pip
* gustavo@gustavo-VirtualBox:~$ pip install deepface

POsteriormente se crea una carpeta (Faces) en nuestro repositorio para guardar imagenes de rostros
se pueden descargar de la pagina:
https://this-person-does-not-exist.com/en

Donde se generan rostros aleatorios no existentes.
En mi caso descargue esta imagen:

![image](https://user-images.githubusercontent.com/111370930/192594420-1042b6d8-6cd4-45f8-9654-52ba678cb0c8.png)

Con una resolucion de 1024 \times 1024 pixeles de resolucion.

Instrucciones de preparación del entorno

Se teclea el siguiente codigo, donde se importan las bibliotecas: DeepFace y result.

...........................................................................................
from deepface import DeepFace
obj = DeepFace.analyze(img_path = "/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/carrie1.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)
print ("El resultado del analisis es:")
print (obj)
...........................................................................................

Este codigo devolvera un JSON con los valores correspondientes al analisis de la fotografia anteriormente descargada de la pagina:https://this-person-does-not-exist.com/en, en donde se muestran las caracteristicas de edad aproximada, raza y estado de animo.

El valor puede ser compilado en consola, imprimiendo el JSON y descargando los complementos de la biblioteca.

-           -                -                  -                 -                 -

gustavo@gustavo-VirtualBox:~/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Ejemplos$ python3 facial-atributes-rec.py
Directory  /home/gustavo /.deepface created
Directory  /home/gustavo /.deepface/weights created
facial_expression_model_weights.h5 will be downloaded...
Downloading...
From: https://github.com/serengil/deepface_models/releases/download/v1.0/facial_expression_model_weights.h5
To: /home/gustavo/.deepface/weights/facial_expression_model_weights.h5
100%|██████████████████████████████████████| 5.98M/5.98M [00:01<00:00, 5.07MB/s]
age_model_weights.h5 will be downloaded...
Downloading...
From: https://github.com/serengil/deepface_models/releases/download/v1.0/age_model_weights.h5
To: /home/gustavo/.deepface/weights/age_model_weights.h5
100%|████████████████████████████████████████| 539M/539M [01:25<00:00, 6.31MB/s]
gender_model_weights.h5 will be downloaded...
Downloading...
From: https://github.com/serengil/deepface_models/releases/download/v1.0/gender_model_weights.h5
To: /home/gustavo/.deepface/weights/gender_model_weights.h5
100%|████████████████████████████████████████| 537M/537M [01:25<00:00, 6.30MB/s]
race_model_single_batch.h5 will be downloaded...
Downloading...
From: https://github.com/serengil/deepface_models/releases/download/v1.0/race_model_single_batch.h5
To: /home/gustavo/.deepface/weights/race_model_single_batch.h5
100%|████████████████████████████████████████| 537M/537M [01:24<00:00, 6.33MB/s]
1/1 [==============================] - 4s 4s/step         | 0/4 [00:00<?, ?it/s]
1/1 [==============================] - 1s 574ms/step1/4 [00:10<00:31, 10.52s/it]
1/1 [==============================] - 1s 568ms/step2/4 [00:11<00:09,  4.71s/it]
1/1 [==============================] - 0s 304ms/step3/4 [00:11<00:02,  2.85s/it]
Action: emotion: 100%|████████████████████████████| 4/4 [00:12<00:00,  3.15s/it]
El resultado del analisis es:
{'age': 38, 'region': {'x': 170, 'y': 212, 'w': 691, 'h': 691}, 'gender': 'Man', 'race': {'asian': 3.7788756971211073, 'indian': 5.0019221755173415, 'black': 1.4279849666935165, 'white': 45.44505422652414, 'middle eastern': 25.63143976109502, 'latino hispanic': 18.71473118242397}, 'dominant_race': 'white', 'emotion': {'angry': 2.0181071576233847e-12, 'disgust': 9.346201861827638e-20, 'fear': 0.3340015886351466, 'happy': 3.6181122542444655e-07, 'sad': 2.127008968955124e-05, 'surprise': 3.6706195860602975e-07, 'neutral': 99.66597557067871}, 'dominant_emotion': 'neutral'}

...........................................................................................

Para la comparacion de 2 rostro se realiza la misma importacion y se descargan 2 imagenes diferentes y 2 iguales en mi casodescargue las imagenes que se muestran en mi carpeta Faces(Dentro de este repositorio):
Se importa el paquete result
y con la instruccion verify, se procede a poner las 2 rtas donde se encuentran los rostros en mi caso Mee, Hugo con extencion *.jpeg., como se muestra en el siguiente codigo:

from unittest import result
from deepface import DeepFace

print ("Se han cargado 2 imagenes para verificar que la persona sea la misma")
print ("Cargando ....")
result =DeepFace.verify(img1_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/Hugo.jpeg", img2_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/Mee.jpeg")

print ("Resultados")
print(result)

-           -          -            -         -        -
El resultado dara como consecuencia un JSON donde se muestra Tru o False, segun las fotos analizadas.

........................................................................
gustavo@gustavo-VirtualBox:~/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Ejemplos$ python3 Check-Face.py
Se han cargado 2 imagenes para verificar que la persona sea la misma
Cargando ....
1/1 [==============================] - 2s 2s/step
1/1 [==============================] - 0s 290ms/step
Resultados
{'verified': False, 'distance': 0.43321696789354147, 'threshold': 0.4, 'model': 'VGG-Face', 'detector_backend': 'opencv', 'similarity_metric': 'cosine'}


........................................................................

Realizamos el mismo procedimiento pero ahora con fotografias iguales en mi caso: carri1 y carrie2(Que se encuentran en este repositorio en la carpeta Faces):
En este ejemplo solo cambiamos la liea donde se agregan la ruta de las imagenes a comparar:
result =DeepFace.verify(img1_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/carrie1.png", img2_path="/home/gustavo/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Faces/carrie2.png")
..........................................................................

gustavo@gustavo-VirtualBox:~/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Ejemplos$ python3 Check-Face.py
Se han cargado 2 imagenes para verificar que la persona sea la misma
Cargando ....
vgg_face_weights.h5 will be downloaded...
Downloading...
From: https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5
To: /home/gustavo/.deepface/weights/vgg_face_weights.h5
100%|████████████████████████████████████████| 580M/580M [01:32<00:00, 6.29MB/s]
1/1 [==============================] - 3s 3s/step
1/1 [==============================] - 0s 449ms/step
Resultados
{'verified': True, 'distance': 0.24235788220619503, 'threshold': 0.4, 'model': 'VGG-Face', 'detector_backend': 'opencv', 'similarity_metric': 'cosine'}


..........................................................................

Resultados


Los resultados de la ejecucion se muestran a continuacion en el orden que se describieron en este docmento.

![image](https://user-images.githubusercontent.com/111370930/192590385-f1445792-730f-472a-a410-a98f40915ac5.png)

![image](https://user-images.githubusercontent.com/111370930/192590613-e82857cc-bddb-46a7-a5fe-45b2c80bda3b.png)

![image](https://user-images.githubusercontent.com/111370930/192590701-2bbb51b9-b7e0-429b-a495-640e8523f3ba.png)


Evidencias

Repositorio github: https://github.com/Gustavo-MA/Apertura-puertas-reconocimiento-facial
Créditos

Desarrollado por Gustavo Medina e-mail: gustavo.medina@uaem.edu.mx
