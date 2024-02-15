#Задача 1 
#Получить с клавиатуры скорость самолета, названия городов и расстояние (на 12 баллов координаты lat, lon). 
#Вычислить время в пути, считая скорость постоянной. Записать ответ, как в слайде с примером.
skorost=input('Введите скорость самолета')
gorod_1=input('Место вылета')
gorod_2=input('Место прилета')
print('Координаты места вылета:')
lat_1=input('Северная широта:')
lon_1=input('Восточная долгота:')
x1=float(lat_1)
y1=float(lon_1)
print('Координаты места прилета:')
lat_2=input('Северная широта:')
lon_2=input('Восточная долгота:')
x2=float(lat_2)
y2=float(lon_2)
import math
rasstoianie=math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(y1 - y2)
d=math.cos(rasstoianie)
radius=6371
l=radius*d
print(l)
v=float(skorost)
t=l/v
print('Время пути займет',t,'часов')