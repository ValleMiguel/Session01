#1. Imprimir la lista de opciones en la pantalla
#2. Leer la opcióm elegida por el usuario
#3. En base a la opcion del usuario imprimir el valor del helado

print("""
	------------------------
1. Helado con oreo: $19
2. Helado con m&m: $25
3. Helado con fresas: $22
4. Helado con brownie: $28
------------------------------
""")

opcion_str = input("Elige el topping: ")
opcion = int(opcion_str)

if opcion == 1:
	precio = 19
elif opcion == 2:
	precio = 25
elif opcion == 3:
	precio = 22
elif opcion == 4:
	precio = 25
else:
	precio = 0

if precio == 0:
	print("el helado elegido no existe")
else:
	#print(" el valor del Helado es ${:.2f} M.N.".format(precio))
	print(f" el valor del Helado es ${precio:.2f} M.N.")
