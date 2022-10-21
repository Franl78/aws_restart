#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
print("Lista de precios:")
precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios [0]
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
        
print("el minimo es ' + str(min)")
print("el maximo es ' + str(max)")