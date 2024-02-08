# Calculadora simple en Python

# Funciones para realizar operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por ceros"

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número : "))
num2 = float(input("Ingrese el segundo número : "))

# Menú de operaciones
print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Obtener la opción del usuario
opcion = input("Ingrese el número que desee operar (1/2/3/4): ")

# Realizar la operación seleccionada
if opcion == '1':
    resultado = suma(num1, num2)
elif opcion == '2':
    resultado = resta(num1, num2)
elif opcion == '3':
    resultado = multiplicacion(num1, num2)
elif opcion == '4':
    resultado = division(num1, num2)
else:
    resultado = "Opción no válida"

# Imprimir el resultado
print("Resultado: ", resultado)
