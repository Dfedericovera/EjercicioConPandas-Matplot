import pandas as pd
import matplotlib.pyplot as plt

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
#data 'class' es lo que tiene que aprender el algoritmo para saber si nos conviene comprar o no. Tambien cambiamos los valores por valores numericos
data['Decision'].replace(('unacc','acc','good','vgood'), (1,2,3,4), inplace = True)

print(data.head(5))