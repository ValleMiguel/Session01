#Declara una lista que contenga por elementos los nombres de alumnos de un curso (minimo 5)
#Usa sort() para ordenar a los alumnos
#Imprime el nombre del primer alumno
#Inscribe un nuevo alumno en el curso(lo cuál puede alterar el orden)

grupo_A = ["Marcos","Alicia","Juan","Maria","Pancho"]
print(grupo_A)
grupo_A.sort()
print(grupo_A)
grupo_1 = grupo_A[0]
print(grupo_1)
grupo_A.append("Manuel")
print(grupo_A)