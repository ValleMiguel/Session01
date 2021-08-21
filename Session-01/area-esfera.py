#Calcula el volumen de una esfera en base al radio proporcionado por el usuario
#ejemplo calcula el volumen de la tierra
# 1.Leer el valor del radio del usuario (entrada estandar)
# 2. Calcular el volumen del circulo
# 3. Imprimir el volumen en la pantalla (salida estandar)
# volumen = (4/3) * pi x radio ^ 3

PI = 3.14159

radio_str = input("Dame el valor del radio= ")
radio = float(radio_str)
volumen = (4/3) * PI * radio ** 3
print("El volumen de la esfera es:{:.2f} m3".format(volumen))
