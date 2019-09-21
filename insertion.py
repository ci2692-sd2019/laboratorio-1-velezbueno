# Def de insertionsort
def InsertionSort(lineas, n):
	for i in range(1, n):
		#Elemento que se va a insertar
		num = lineas[i]
		j = i - 1
		while(j >= 0 and lineas[j] > num):
			lineas[j+1] = lineas[j]
			j = j - 1
		lineas[j+1] = num
	return lineas