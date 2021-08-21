#Se deben solicitar al usuario dos números
#Se puede seleccionar entre diferentes operaciones(suma, resta, multiplicación y división).
#Imprimir resultados
#Considerar división entre cero y caracteres no definidos como operaciones.

print("insertar primer numero")
num1 = int(input())
print("insertar segundo numero")
num2 = int(input())
print("Selecciona operación que quieres realizar con su respectivo signo")
print("+ -> Suma")
print("- -> Resta")
print("* -> Multiplicaión")
print("/ -> División")
print("% -> Modulo")
operacion = input()

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 == '0':
        print("ERROR: División entre 0")
        resultado = 'ERROR'
    else:
        resultado = num1 / num2
elif operacion == '%':
    resultado = num1 % num2
else:
    resultado = 'ERROR'
    print("Operacion no definida")

print("{} {} {} = {}".format(num1,operacion, num2, resultado))