#### CI2692
#### SD 2019
#### Oliver Bueno y Miguel Vélez


# Proyecto1
## Comparación de algoritmos de aprendizaje


### Resumen
>Se realizó un archivo ‘sorts.py’ siguiendo los pseudo códigos de las laminas vistas en clase de CI2612, donde se implementaron algoritmos de ordenamiento, los cuales son InsertionSort, MergeSort, Quicksort, RandomizedQuicksort, CountinSort y RadixSort.  
También se realizó un archivo “test_sort.py” en el cual se hizo uso de los algoritmos en “sort.py” para calcular el promedio y la desviación estándar de los tiempos de ejecución de los distintos algoritmos de ordenamiento, con el fin de evaluar su comportamiento con arreglos de varios tamaños y así verificar si se cumplen las cotas teóricas que se vieron en clase. 

##Descripción de los algoritmos


##InsertionSort

###Descripción:

>InsertionSort es un algoritmo de ordenamiento que dado un arreglo, inserta los elementos del arreglo en la posición correcta, ordenando el arreglo  dentro del mismo de forma ascendente.

El algoritmo InsertionSort presenta un tiempo para el peor caso de Θ(n∧2) y un tiempo promedio de Θ(n∧2)

###Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  *A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  *p: Número entero que indica la posición del primer elemento del arreglo.
  *r: Número entero que indica la posición del último elemento del arreglo.

####Detalles de la implementación:
El procedimiento InsertionSort(A, p, r), compara los elementos del arreglo desde el primero hasta el último o hasta encontrar uno mayor, ordenando el arreglo de forma ascendente.


##MergeSort

###Descripción:

>Mergersort es un algoritmo de ordenamiento que divide en dos partes iguales los elementos de un arreglo, ordenando estas partes por medio de llamadas recursivas y combinando la solución de cada parte en orden ascendente.

>El algoritmo Mergersort presenta la siguiente recurrencia: t(n) = t( n/2 ) + t( n/2 ) + Θ(n). En donde el tiempo para el peor caso es Θ(n log n) y un tiempo promedio de Θ(n log n).

###Implementación:

Estructura de datos: En cuanto a los parámetros que recibe la función, tenemos:

  *A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  *p: Número entero que indica la posición del primer elemento del arreglo.
  *r: Número entero que indica la posición del último elemento del arreglo.

####Detalles de la implementación:
El procedimiento MergerSort(A, p, r),  se llama a ella misma dos veces y luego llama al procedimiento merge para combinar las soluciones, ordenando el arreglo de forma ascendente.


##HeapSort

###Descripción:

>HeapSort es un algoritmo de ordenamiento basado en comparaciones, el cual utiliza la estructura de datos heap binario, implementando una cola de prioridades. HeapSort ordena los elementos del arreglo dentro del mismo de forma ascendente.

>El algoritmo HeapSort presenta un tiempo para el peor caso de Θ(n log n) y un tiempo promedio de Θ(n log n).

###Implementación:

Estructura de datos: En cuanto a los parámetros que recibe la función, tenemos:

  *A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.

En cuanto a las estructuras de datos utilizadas en el algoritmo HeapSort, tenemos:

  *Maxheap: Es una estructura de árbol binario que almacena una colección de claves, que tiene la propiedad  de que la clave de un nodo x es menor o igual a la clave del padre, esto es Parent(x) ≥ x.
  *Cola de prioridades: Una cola de prioridades es una estructura de datos que mantiene un conjunto S de elementos.

####Detalles de la implementación: 
El procedimiento MergerSort(A), llama al procedimiento buildmaxheap para construir un maxheap, a su vez el procedimiento buildmaxheap llama al procedimiento recursivo maxheapify el cual se encarga de mantener las propiedades del maxheap. Luego se intercambia la clave más grande con el nodo menor, se descarta el último intercambio para decrementar el tamaño del heap, finalmente se llama a maxheapify, continuando el proceso hasta que solo quede un nodo, al finalizar este proceso el arreglo quedará ordenado de forma ascendente.

##QuickSort

###Descripción:

>QuickSort es un algoritmo de ordenamiento recursivo que toma el último elemento x del arreglo y se divide de tal forma que todos los elementos menores de x están antes que el y los mayores que x, están después de el. Luego a través de llamadas recursivas ordena el arreglo de forma ascendente.

>El algoritmo QuickSort presenta la siguiente recurrencia t(n) = t(q) + t(n − q) + n. En donde el tiempo para el peor caso es de Θ(n∧2) y para el caso promedio es de Θ(n log n).

###Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  *A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  *p: Número entero que indica la posición del primer elemento del arreglo.
  *r: Número entero que indica la posición del último elemento del arreglo.

####Detalles de la implementación:
El procedimiento QuickSort(A, p, r), llama al procedimiento Partition, que particiona el  arreglo A de la forma A[p. . q − 1] y A[q + 1. . q], tal que todos los elementos A[p. . q − 1] son menores o igual a A[q] y todos elementos A[p. . q − 1] son mayores o iguales a A[q] . Luego se ordenan A[p. . q − 1] y A[q + 1. . q] con llamadas recursivas a QuickSort , en donde al final el arreglo termina estando ordenado de forma ascendente.

##RandomizedQuicksort

###Descripción:

>RandomizedQuicksort es un algoritmo de ordenamiento recursivo que toma un elemento al azar x del arreglo y se divide de tal forma que todos los elementos menores de x están antes que el y los mayores que x, están después de el. Luego a través de llamadas recursivas ordena el arreglo de forma ascendente.

>El algoritmo RandomizedQuicksort presenta la siguiente recurrencia t(n) = t(q) + t(n − q) + n. En donde el tiempo para el peor caso es de Θ(n∧2) y para el caso promedio es de Θ(n log n).

###Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  *A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  *p: Número entero que indica la posición del primer elemento del arreglo.
  *r: Número entero que indica la posición del último elemento del arreglo.

####Detalles de la implementación:
El procedimiento RandomizedQuicksort(A, p, r), llama al procedimiento RandomizedPartition, que particiona el  arreglo A de la forma A[p. . q − 1] y A[q + 1. . q], tal que todos los elementos A[p. . q − 1] son menores o igual a A[q] y todos elementos A[p. . q − 1] son mayores o iguales a A[q] . Luego se ordenan A[p. . q − 1] y A[q + 1. . q] con llamadas recursivas a RandomizedQuicksort , en donde al final el arreglo termina estando ordenado de forma ascendente.

##CountingSort

###Descripción:

>CountingSort es un algoritmo de ordenamiento, que lo primero que se hace es contar cuantos elementos son menores a k, para cada elemento x de un arreglo. Una vez que la información es calculada, cada elemento x es colocado directamente en su posición final en el arreglo de salida.

>El algoritmo CountingSort presenta un tiempo para el peor caso de Θ(k + n) y un tiempo promedio de Θ(k + n).

###Implementación:

Estructura de datos: En cuanto a los parámetros que recibe la función, tenemos:

  *A: Arreglo de tipo entero, con enteros mayores o iguales a 0 de tamaño n, que contiene los elementos a ser ordenados.
  *B: Arreglo de tipo entero, con entero mayores o iguales a 0 de tamaño n, que es usado para almacenar el arreglo  A ya ordenado.
  *k: Número entero, el cual es elemento más grande que contiene el arreglo A .

####Detalles de la implementación:
La función CountingSort(A,B,k), primero cuenta cuantas veces aparece un elemento en el arreglo A, luego cuenta cuantos elementos tiene el arreglo A y finalmente construye el arreglo B de forma ordenada ascendentemente.


##RadixSort

###Descripción:

>RadixSort es un algoritmo de ordenamiento, que utiliza algún algoritmo estable como CountingSort para ordenar cifras dígito a dígito. Primero clasifica la cifra por el dígito menos significativo, luego clasifica la cifra de nuevo por el segundo dígito menos significativo, repitiendo el proceso hasta concatenar por el dígito más significativo.

>El algoritmo RadixSort presenta un tiempo para el peor caso de Θ(d(n + k)) y un tiempo promedio de Θ(d(n + k)).

###Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  *A: Arreglo de tipo entero, con enteros mayores o iguales a 0 de tamaño n, que contiene los elementos a ser ordenados.

  *d: Número entero, que contiene la cantidad de dígitos que tiene el número más grande dentro del arreglo a ordenar.

####Detalles de la implementación:
La función RadixSort(A, d), ordena las cifras en el arreglo A según el dígito indicado, en donde para ello utiliza el algoritmo CountingSort.


### Actividades

1. Implemente los siguientes algoritmos (puede usar las implementaciones realizadas en los laboratorios previos): 

	- 1.1. Inserción 
	- 1.2. MergerSort
	- 1.3. HeapSort
	- 1.4. Quicksort
	- 1.5. Randomized Quicksort 
	- 1.6. Counting Sort
	- 1.7. Radix Sort

Sus implementaciones deberán realizarse en un archivo denominado: `sorts.py`. En el repositorio se les incluye una versión inicial de este archivo con las firmas (Nombre de la función y los parámetros) de las funciones a  implementar. 

2. Implemente un programa de prueba `test_sorts.py` que le permita evaluar los algoritmos implementados en la actividad anterior. Esta aplicación se ejecutará usando el siguiente comando:
> python3 test_sorts.py [num pruebas] [num elems]
	
donde:
- [num pruebas] : Es el número de veces que se ejecuta cada algoritmo de ordenamiento sobre diferentes arreglos.
- [num elems] :  Es el número de elementos que contiene el arreglo a ordenar. Pueden asumir que los elementos de los arreglos son números enteros (no hace falta que lo verifiquen).

Por ejemplo, la llamada `python3 test_sorts.py 5 1000` ejecutará 5 veces todos los algoritmos de ordenamiento sobre arreglos de tamaño 1000. 

Este programa prueba debe mostrar por la salida estándar el tiempo promedio de ejecución en milisegundos y la desviación estandar de cada algoritmo.  Para ello: 
- El contador de tiempo debe empezar al arrancar el algoritmo de
ordenamiento y detenerse al terminar de ordenarse el arreglo. 
- Los números deben mostrarse con 2 decimales.

El formato de la salida es el siguiente:

```
<Algoritmo 1> <tiempo promedio 1> <desviación estandar 1>
<Algoritmo 2> <tiempo promedio 2> <desviación estandar 2>
...
<Algoritmo N> <tiempo promedio N> <desviación estandar N>
```

Por ejemplo:
```
Insercion 2575.43 28.12
Mergesort 1569.21 24.14
Heapsort 1567.98 24.76
Quicksort 1463.11 25.61
RadomizedQuicksort 1871.34 23.87
Countingsort 2078.33 24.76
Radixsort 1443.33 22.89
```
 
*NOTAS IMPORTANTES*: 

- Todo su código deberá estar documentado. 
- Su código deberá cumplir con la [guía de estilo de PEP8](https://www.python.org/dev/peps/pep-0008/), y estar documentado siguiendo las [convenciones de numpy](https://numpydoc.readthedocs.io/en/latest/format.html). Especialmente la documentación de cada función (resumen, parámetros y retorno) 
que pueden leer el [Sections](https://numpydoc.readthedocs.io/en/latest/format.html#sections) del documento.
- Deben verificar que las llamadas a su programa de prueba se hagan de forma adecuada.


3. Con los resultados de la actividad anterior, deberán completar el siguiente cuadro, colocando el tiempo promedio y la desviación estándar para `10 corridas` de cada algoritmo para cada `n`

| Algoritmo             |  1.000 |  5.000 | 10.000 | 20.000 | 40.000 | 80.000 | 160.000 |
|----------------------	|------- |--------|--------|--------|--------|--------|---------|
| Insertion            	|        |        |        |        |        |        |         |
| Merge Sort           	|       |      	|       |       |       |       |       |
| Heap Sort            	|       |      	|       |       |       |       |       |
| Quicksort            	|       |      	|       |       |       |       |       |
| Randomized Quicksort 	|       |      	|       |       |       |       |       |
| Counting sort        	|       |      	|       |       |       |       |       |
| Radix sort           	|       |      	|       |       |       |       |       |



4. Debe realizar un breve informe que debe contener:
- Un resumen
- Breve descripción de su implementación (detalles relevantes de las estructuras de datos y la implementación de los algoritmos)
- Los resultados de la tabla de la actividad 3, 
- **Una gráfica para cada algoritmo** que presente un punto para el tiempo promedio para cada tamaño de entrada, estos puntos estarán unidos por una línea de tendencia (línea que une los puntos); sobre esta misma gráfica dibujarán una línea que muestre el comportamiento teórico del algorimo; deberán indicar en la leyenda cuál es la constante usada para ajustar esta línea (Cota superior).
- **Una gráfica con los tiempos promedios de todos los algoritmos** (menos el de ordenamiento por inserción). Esta gráfica contendrá una línea de tendencia para cada algoritmo.  
- Un breve análisis de los resultados de la tabla y las gráficas.
Este informe deberá incluirse como un archivo .md ([Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)) en su repositorio.  
- Conclusiones 
- Bibliografía

### Entrega
- En el repositorio git del equipo: los archivos .py documentados y el informe en el archivo INFORME.md
- La fecha de entrega es el Jueves 31 de Octubre a las 12:00 del medio día. No se aceptarán cambios a su repositorio Git posteriores a esa fecha/hora.

