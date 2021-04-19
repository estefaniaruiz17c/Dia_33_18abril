# Funciones Lambda: conocidas también como funciones anónimas porque se definen sin un nombre
print("Funciones Lambda")


print()
# Ejercicio 1
print("\n- Ejercicio 1:\n")

# Crear la función 1 que reciba 2 números, los sume y los multiplique por una variable x = 4
fn1 = lambda a,b,x=4 : (a+b)*x

# Mostrar la descripción de lo que hace la función
print("Función que recibe 2 números, los suma, y luego los multiplica por el valor de x que es 4")

# Asignación de las variables a evaluar: a = 5, b = 3
print("\nCon los números 5 y 3, la respuesta es:",fn1(5,3))

# También podemos reasignar el valor a x, indicando un tercer argumento dentro del paréntesis de la función
print("\nCon los números 5 y 3, y reasignando el valor de x a 2 la respuesta es:",fn1(5,3,2))


print()
# Ejercicio 2
print("\n- Ejercicio 2:\n")

# Crear la función 2 que permite identificar si un número es par
fn2 = lambda y: y%2 == 0


# Mostrar la descripción de lo que hace la función
print("Función que evalúa si un número es par. Retorna True o Flase según el caso ")

# Asignación de la variable a evaluar
print("\nEl número 1432 es par?:", fn2(1432))

# Asignación de la variable a evaluar
print("\nEl número 669 es par?:", fn2(699))


print()
# Ejercicio 3
print("\n- Ejercicio 3:\n")

# Crear función 3 que permite realizar una comparación después de una operación según una condicional establecida
fn3 = lambda t: True if t**2 <= 30 else False

# Mostrar la descripción de lo que hace la función
print("Función que eleva un número a la potencia 3, lo compara, si es menor o igual a 30, retornará True ")

# Asignación de la variable a evaluar
print("\nEl número 6 elevado a la 3, es menor o igual a 30:", fn3(6))

# Asignación de la variable a evaluar
print("\nEl número 3 elevado a la 3, es menor o igual a 30:", fn3(3))

print()
print("----------"*7)
print()

# Funciones comunes de lambda
print("\nFunciones comunes de Lambda\n")

# map(): aplica una función a cada uno de los elementos de una lista. Recibe 2 argumentos
print("\nmap():\n")

# Función 4 usando map(). Crearemos una lista y le aplicaremos una función a cada elemento de la lista. En este caso multiplicar por 9 cada número de la lista
fn4 = lambda f: f*9

# Asignación de la variable a evaluar, una lista números int
lista1 = [4,7,9,2]
num1 = list(map(fn4,lista1))

# Mostrar la respuesta
print("Multiplicar cada número de la lista {} por 9: {}".format(lista1,num1))

# Asignación de la variable a evaluar, una listan de números decimales
lista2 = [0.3,4.6,2.8]
num2 = list(map(fn4,lista2))

# Mostrar la respuesta
print("\nMultiplicar cada número de la lista {} por 9: {}".format(lista2,num2))

print()
# filter(): filtra una lista de elementos para los que una función devuelve True. Recibe 2 argumentos
print("\nfilter():\n")

# Función para identificar números impares
fn5 = lambda y: y%2 != 0

# Asignación de la variable a evaluar
list1 = [34,17,88,3,109,95]
impar = list(filter(fn5, list1))

# Mostrar la respuesta
print("De la lista {}, los números impares son: {}".format(list1,impar))

print()
# reduce(): se utiliza para llevar a cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado. Para utlizarla, necesitamos importar reduce de functools
print("\nreduce():")

from functools import reduce

# Función que sirve para ir restando los valores de la lista y devuelve el resultados
fn6 = lambda x,r: x-r

# Asignación de la variable a evaluar
valores = [54,16,21,6]

# Uso de la función reduce() invocando la función 6 y la lista valores
reduc = reduce(fn6,valores)

# Mostrar la respuesta
print("\nResta en orden de cada elemento de la lista {}: {}".format(valores,reduc))
