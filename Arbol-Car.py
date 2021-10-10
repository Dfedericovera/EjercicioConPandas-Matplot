#Modelo de aprendisaje automatico de tipo supervisado
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('car.csv', header = None)
data.columns = ['Price', 'Maintenance Cost', 'N_doors', 'Capacity', 'size_lig','Safety','Decision']
print(data.sample(3))

#Convertimos los valores string a numericos
data['Price'].replace(('vhigh','high','med','low'), (4,3,2,1), inplace = True)
data['Maintenance Cost'].replace(('vhigh','high','med','low'), (4,3,2,1), inplace = True)
data['N_doors'].replace(('2','3','4','5more'), (1,2,3,4), inplace = True)
data['Capacity'].replace(('2','4','more'), (1,2,3), inplace = True)
data['size_lig'].replace(('small','med','big'), (1,2,3), inplace = True)
data['Safety'].replace(('low','med','high'), (1,2,3), inplace = True)
#data 'class' es lo que tiene que aprender el algoritmo para saber si nos conviene comprar o no. También cambiamos los valores por valores numéricos.
data['Decision'].replace(('unacc','acc','good','vgood'), (1,2,3,4), inplace = True)
print(data.head(5))

#Recomendación de división de datos: 80% aprendizaje 20 % pruebas

dataset = data.values #solo nos interesan sus valores, no su cabecera
X = dataset[:,0:6] #Columnas (datos con los que va a aprender)
Y = np.asarray(dataset[:,6], dtype = 'S6') # Este arreglo es nuestra ultima columna del set (que es nuestra clase o decisión)

from sklearn import tree 
from sklearn.model_selection import train_test_split, cross_val_score 
from sklearn import metrics

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y, test_size= 0.2 , random_state= 0) #solo quiero el 20% de los datos
tr = tree.DecisionTreeClassifier(max_depth=10) #Profundidad del arbol
print( tr.fit(X_Train,Y_Train) ) #Entrenando
y_pred = tr.predict(X_Test) #Le pedimos que nos haga una predicción
print(y_pred) #Esta seria nuestra decicion o clase

score = tr.score(X_Test,Y_Test)
print('Precisión: %0.4f' % (score))
#Existen otros modelos como redes bayesianas,redes neuronales, clustering ,etc.