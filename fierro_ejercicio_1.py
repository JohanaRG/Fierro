'''
------------------------------
Autor: Johana Rangel
email: johanarang@hotmail.com

Descripción:
Programa que imprime los X primeros “Happy Numbers"
'''

def suma_digitos(number):
    '''Función que separa digitos y retorna la 
    suma de los cuadrados de los dígitos'''

    digitos_obtenidos = [int(digit) for digit in str(number)]
    
    suma_cuadrados = sum([x**2 for x in digitos_obtenidos])
    return suma_cuadrados

def evaluar_suma(numero, cantidad_nros):
    '''Función que evalua la suma si es igual a 1 y 
    retorna el resultado de suma'''

    suma = 0
    contador = 0

    while suma != 1:        
        suma = suma_digitos(numero)  
        if suma == 1:
            return suma
        
        numero = suma  
        contador += 1
        if contador > cantidad_nros: #Para evitar el bucle infinito
            return suma
    

def happy_number(numero, resultado_suma):
    '''Compara si la suma es igual a uno lo identifica como Happy Number 
    y sino lo desestima como No Happy Number'''

    if resultado_suma == 1:
        return print(f'El número {numero} Es un happy number')
    else:
        return print(f'El número {numero} NO es un happy number')


if __name__=="__main__":
    '''Happy_Number'''
    cantidad_nros = int(input('Ingrese la cantidad de números a evaluar: \n'))
    for numero in range(1,cantidad_nros):
        resultado_suma = evaluar_suma(numero, cantidad_nros)
        happy_number(numero, resultado_suma)
        
    