import csv
from datetime import datetime
import operator

from django.db import ProgrammingError

datos = []
with open("trips_2021.csv", newline='', encoding='utf-8') as csvfile:
    data = csv.DictReader(csvfile)
    
    for fila in data:
        fecha_str = fila['fecha_origen_recorrido']
        fecha, horario, texto = fecha_str.split(sep=' ')
                        
        date = fecha +' '+ horario  
        fecha_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S') #Objeto datetime

        if fecha_time.hour in range(6, 12):
            lista_dict = {'fecha_origen_recorrido': date,
                         'nombre_estacion_origen': fila['nombre_estacion_origen']}
            datos.append(lista_dict)
            
  
print(len(datos)) #595888

# datos = [{'fecha_origen_recorrido': '2021-04-10 07:25:08', 'nombre_estacion_origen': '004 - Plaza Roma'},
# {'fecha_origen_recorrido': '2021-04-10 09:39:10', 'nombre_estacion_origen': '006 - Parque Lezama'},
# {'fecha_origen_recorrido': '2021-04-10 09:30:37', 'nombre_estacion_origen': '012 - Plaza Vicente Lopez'},
# {'fecha_origen_recorrido': '2021-04-10 07:45:39', 'nombre_estacion_origen': '012 - Plaza Vicente Lopez'},
# {'fecha_origen_recorrido': '2021-04-10 08:38:25', 'nombre_estacion_origen': '013 - ONCE'},
# {'fecha_origen_recorrido': '2021-04-10 08:57:10', 'nombre_estacion_origen': '022 - Arenales'},
# {'fecha_origen_recorrido': '2021-04-10 11:22:41', 'nombre_estacion_origen': '022 - Arenales'}]

estacion_origen = []
estaciones_conteo = {}

for fila in datos:
    contador = 0
    estacion = fila['nombre_estacion_origen']
    #estacion = estacion_str.split(sep=' - ')
    
    if estacion not in estacion_origen:
        estacion_origen.append(estacion)
        contador += 1
        estaciones_conteo[estacion] = contador
        
    elif estacion in estacion_origen:
        estaciones_conteo[estacion] += 1
       
  
print(estaciones_conteo)

estaciones_order = sorted(estaciones_conteo.values())
primer = estaciones_order[-1]
segundo = estaciones_order[-2]
tercero = estaciones_order[-3]

estaciones_calientes = []
for k,v in estaciones_conteo.items():
    if v == primer:
        estaciones_calientes.append({k:v})

    elif v == segundo:
        segunda = k
        estaciones_calientes.append({k:v})

    elif v == tercero:
        estaciones_calientes.append({k:v})
    
    

print(f'''Estaciones calientes: \n 
        Primer estación es {estaciones_calientes[0]}\n 
        Segunda estación es {estaciones_calientes[1]}\n
        tercera estación es {estaciones_calientes[2]}''')
    
    




        




