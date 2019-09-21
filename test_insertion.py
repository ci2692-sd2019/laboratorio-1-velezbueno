#Se importan las funciones que se van a usar
from insertion import InsertionSort

#Funcion que carga el arreglo de un archivo
def LecturaDeDatos (arreglos):
	w=open(arreglos,"rt")
	O=[]
	for i in w:
		O.append(i)
	m=O[0].split()    
	m=[int(i) for i in O]
	w.close()
	return m

arreglo=LecturaDeDatos(input("Ingrese el nombre del archivo: "))
#Se carga el arreglo desde el archivo que ingrese el usuario
print(InsertionSort(arreglo,len(arreglo)))
#Se muestra el arreglo ordenado por Inserción