#Calcula el area de un circulo en base al radio proporcionado por el usuario

# 1.Leer el valor del radio del usuario (entrada estandar)
# 2. Calcular el area del circulo
# 3. Imprimir el area en la pantalla (salida estandar)
# area = pi x radio ^ 2

PI = 3.14159

radio_str = input("Dame el valor del radio= ")
radio = float(radio_str)
area = PI * radio ** 2
print("El area del circulo es: ", area)


