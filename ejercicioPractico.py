import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('car.csv',header= None)
#Columnas 
data.columns = ['Price', 'Maintenance Cost', 'Number de Doors', 'Capacity', 'Size of Luggage Boot','Safety','Decision']
#top 5
print(data.head(5))
#aleatorios
print(data.sample(5))
#ultimos 5
print(data.tail)
#registros y cant de atributos
print(data.shape)
#total de datos
print(data.size)
#Unicamente los registros de cierta columna
print(data['Price'].sample(3))
#Extraer solo un rango
print(data['Price'][:3])
#Extraer mas de una columna
print( data[ ['Price','Decision'] ].tail())
#Contar valores(registros)
print( data['Decision'].value_counts() )
#Ordenar asc o desc
print ( data['Decision'].value_counts().sort_index(ascending = False) )

decision = data['Decision'].value_counts()

decision.plot(kind = 'bar')
plt.show()
#Traer los datos con los cuales esta conformada una columna
print ( data['Price'].unique())

#Es recomendable para ciertos metodos trabajar con numeros por eso podemos reemplazar datos por numeros

data['Price'].replace(('vhigh','high','med','low'), (4,3,2,1), inplace = True)
print ( 'Valores unicos Price:', data['Price'].unique())

#Ahora en lugar de categorias tenemos datos numericos
price = data['Price'].value_counts()

colors = ['#DDEE01','#CC0101','#FE10D1','#BCC111']
price.plot( kind = 'bar', color = colors)
plt.xlabel('Precio')
plt.ylabel('Autos')
plt.title('Precio de los autos')
plt.show()

print( 'Cantidad de valores Safety:\n', data['Safety'].value_counts() )
labels = ['low','med','high']
size = [576,576,576]
colors = ['cyan','gray','orange']
#destacar un atributo
explode = [0.2,0,0]

plt.pie(size, labels = labels, colors = colors , explode=explode, shadow= True, autopct= '%.2f%%')
plt.title('Niveles de seguridad', fontsize = 10)
plt.axis('off')
plt.legend(loc = 'best')
plt.show()