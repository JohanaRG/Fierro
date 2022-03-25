'''
------------------------------
Autor: Johana Rangel
email: johanarang@hotmail.com

Descripción:
Programa que analiza el archivo de recorridos de Bicicletas 
de la Ciudad y devuelve las tres estaciones de origen más 
“calientes” (de las que salen más recorridos) en la mañana 
(de 6 a 11:59) 
'''

import csv
from datetime import datetime

datos = []  
with open("trips_2021.csv", newline='', encoding='utf-8') as csvfile:
    data = csv.DictReader(csvfile)
    
    for fila in data:
        fecha, horario, texto = fila['fecha_origen_recorrido'].split(sep=' ')

        date = fecha +' '+ horario  
        fecha_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S') #Objeto datetime.

        if fecha_time.hour in range(6, 12): #Filtrando por intervalo de horas entre las 6 y 11.
            #datos sera una lista de diccionarios con valores de fecha_origen_recorrido y nombre_estacion_origen.
            datos.append({'fecha_origen_recorrido': date,'nombre_estacion_origen': fila['nombre_estacion_origen']})
            


estacion_origen = [] #Lista las estaciones de origen.
estaciones_conteo = {}  #Diccionario con estaciones y conteo de uso.

for fila in datos:
    contador = 0
    estacion = fila['nombre_estacion_origen']
        
    if estacion not in estacion_origen:
        estacion_origen.append(estacion)
        contador += 1
        estaciones_conteo[estacion] = contador
        
    elif estacion in estacion_origen:
        estaciones_conteo[estacion] += 1
       

estaciones_order = sorted(estaciones_conteo.values()) #Ordena los valores de las estaciones por valor. 

primer = estaciones_order[-1]
segundo = estaciones_order[-2]
tercero = estaciones_order[-3]


estaciones_calientes = {}  #Guarda las estaciones con más recorrido k:v
for k,v in estaciones_conteo.items():
    if v == primer:
        estaciones_calientes[k]=v
        
    elif v == segundo:
        segunda = k
        estaciones_calientes[k]=v

    elif v == tercero:
        estaciones_calientes[k]=v

lugar_top = []       #Lista con nombres de las tres primeras estaciones más concurridas.                
for i in estaciones_calientes.keys():
    numero, lugar = i.split(sep='-')
    lugar_top.append(lugar)


print(f'''Estaciones calientes entre las 6am y 11am son: \n 
        Primer estación: {lugar_top[0]} con {primer} recorridos  
        Segunda estación: {lugar_top[1]} con {segundo} recorridos 
        tercera estación: {lugar_top[2]}con {tercero} recorridos ''')
    
    



        




