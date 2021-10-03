import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('car.csv',header= None)

data.columns = ['Price', 'Maintenance Cost', 'Number de Doors', 'Capacity', 'Size of Luggage Boot','Safety','Decision']

print(data.head(5))