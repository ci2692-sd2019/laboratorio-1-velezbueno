#### CI2692
#### SD 2019
#### Oliver Bueno y Miguel Vélez


# Proyecto1
## Comparación de algoritmos de aprendizaje


### Resumen
>Se realizó un archivo ‘sorts.py’ siguiendo los pseudo códigos de las laminas vistas en clase de CI2612, donde se implementaron algoritmos de ordenamiento, los cuales son InsertionSort, MergeSort, Quicksort, RandomizedQuicksort, CountinSort y RadixSort.  
También se realizó un archivo “test_sort.py” en el cual se hizo uso de los algoritmos en “sort.py” para calcular el promedio y la desviación estándar de los tiempos de ejecución de los distintos algoritmos de ordenamiento, con el fin de evaluar su comportamiento con arreglos de varios tamaños y así verificar si se cumplen las cotas teóricas que se vieron en clase. 


## Descripción de los algoritmos


## InsertionSort

### Descripción:

>InsertionSort es un algoritmo de ordenamiento que dado un arreglo, inserta los elementos del arreglo en la posición correcta, ordenando el arreglo  dentro del mismo de forma ascendente.  
El algoritmo InsertionSort presenta un tiempo para el peor caso de Θ(n∧2) y un tiempo promedio de Θ(n∧2)

### Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  * A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  * p: Número entero que indica la posición del primer elemento del arreglo.
  * r: Número entero que indica la posición del último elemento del arreglo.

#### Detalles de la implementación:
El procedimiento InsertionSort(A, p, r), compara los elementos del arreglo desde el primero hasta el último o hasta encontrar uno mayor, ordenando el arreglo de forma ascendente.


## MergeSort

### Descripción:

>Mergersort es un algoritmo de ordenamiento que divide en dos partes iguales los elementos de un arreglo, ordenando estas partes por medio de llamadas recursivas y combinando la solución de cada parte en orden ascendente.  
El algoritmo Mergersort presenta la siguiente recurrencia: t(n) = t( n/2 ) + t( n/2 ) + Θ(n). En donde el tiempo para el peor caso es Θ(n log n) y un tiempo promedio de Θ(n log n).

### Implementación:

Estructura de datos: En cuanto a los parámetros que recibe la función, tenemos:

  * A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  * p: Número entero que indica la posición del primer elemento del arreglo.
  * r: Número entero que indica la posición del último elemento del arreglo.

#### Detalles de la implementación:
El procedimiento MergerSort(A, p, r),  se llama a ella misma dos veces y luego llama al procedimiento merge para combinar las soluciones, ordenando el arreglo de forma ascendente.


## HeapSort

### Descripción:

>HeapSort es un algoritmo de ordenamiento basado en comparaciones, el cual utiliza la estructura de datos heap binario, implementando una cola de prioridades. HeapSort ordena los elementos del arreglo dentro del mismo de forma ascendente.  
El algoritmo HeapSort presenta un tiempo para el peor caso de Θ(n log n) y un tiempo promedio de Θ(n log n).

### Implementación:

Estructura de datos: En cuanto a los parámetros que recibe la función, tenemos:

  - A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.

En cuanto a las estructuras de datos utilizadas en el algoritmo HeapSort, tenemos:

  * Maxheap: Es una estructura de árbol binario que almacena una colección de claves, que tiene la propiedad  de que la clave de un nodo x es menor o igual a la clave del padre, esto es Parent(x) ≥ x.
  * Cola de prioridades: Una cola de prioridades es una estructura de datos que mantiene un conjunto S de elementos.

#### Detalles de la implementación: 
El procedimiento MergerSort(A), llama al procedimiento buildmaxheap para construir un maxheap, a su vez el procedimiento buildmaxheap llama al procedimiento recursivo maxheapify el cual se encarga de mantener las propiedades del maxheap. Luego se intercambia la clave más grande con el nodo menor, se descarta el último intercambio para decrementar el tamaño del heap, finalmente se llama a maxheapify, continuando el proceso hasta que solo quede un nodo, al finalizar este proceso el arreglo quedará ordenado de forma ascendente.

## QuickSort

### Descripción:

>QuickSort es un algoritmo de ordenamiento recursivo que toma el último elemento x del arreglo y se divide de tal forma que todos los elementos menores de x están antes que el y los mayores que x, están después de el. Luego a través de llamadas recursivas ordena el arreglo de forma ascendente.  
El algoritmo QuickSort presenta la siguiente recurrencia t(n) = t(q) + t(n − q) + n. En donde el tiempo para el peor caso es de Θ(n∧2) y para el caso promedio es de Θ(n log n).

### Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  * A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  * p: Número entero que indica la posición del primer elemento del arreglo.
  * r: Número entero que indica la posición del último elemento del arreglo.

#### Detalles de la implementación:
El procedimiento QuickSort(A, p, r), llama al procedimiento Partition, que particiona el  arreglo A de la forma A[p. . q − 1] y A[q + 1. . q], tal que todos los elementos A[p. . q − 1] son menores o igual a A[q] y todos elementos A[p. . q − 1] son mayores o iguales a A[q] . Luego se ordenan A[p. . q − 1] y A[q + 1. . q] con llamadas recursivas a QuickSort , en donde al final el arreglo termina estando ordenado de forma ascendente.

## RandomizedQuicksort

### Descripción:

>RandomizedQuicksort es un algoritmo de ordenamiento recursivo que toma un elemento al azar x del arreglo y se divide de tal forma que todos los elementos menores de x están antes que el y los mayores que x, están después de el. Luego a través de llamadas recursivas ordena el arreglo de forma ascendente.  
El algoritmo RandomizedQuicksort presenta la siguiente recurrencia t(n) = t(q) + t(n − q) + n. En donde el tiempo para el peor caso es de Θ(n∧2) y para el caso promedio es de Θ(n log n).

### Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  * A: Arreglo de tipo flotante o  entero de tamaño n, que contiene los elementos a ser ordenados.
  * p: Número entero que indica la posición del primer elemento del arreglo.
  * r: Número entero que indica la posición del último elemento del arreglo.

#### Detalles de la implementación:
El procedimiento RandomizedQuicksort(A, p, r), llama al procedimiento RandomizedPartition, que particiona el  arreglo A de la forma A[p. . q − 1] y A[q + 1. . q], tal que todos los elementos A[p. . q − 1] son menores o igual a A[q] y todos elementos A[p. . q − 1] son mayores o iguales a A[q] . Luego se ordenan A[p. . q − 1] y A[q + 1. . q] con llamadas recursivas a RandomizedQuicksort , en donde al final el arreglo termina estando ordenado de forma ascendente.

## CountingSort

### Descripción:

>CountingSort es un algoritmo de ordenamiento, que lo primero que se hace es contar cuantos elementos son menores a k, para cada elemento x de un arreglo. Una vez que la información es calculada, cada elemento x es colocado directamente en su posición final en el arreglo de salida.  
El algoritmo CountingSort presenta un tiempo para el peor caso de Θ(k + n) y un tiempo promedio de Θ(k + n).

### Implementación:

Estructura de datos: En cuanto a los parámetros que recibe la función, tenemos:

  * A: Arreglo de tipo entero, con enteros mayores o iguales a 0 de tamaño n, que contiene los elementos a ser ordenados.
  * B: Arreglo de tipo entero, con entero mayores o iguales a 0 de tamaño n, que es usado para almacenar el arreglo  A ya ordenado.
  * k: Número entero, el cual es elemento más grande que contiene el arreglo A .

#### Detalles de la implementación:
La función CountingSort(A,B,k), primero cuenta cuantas veces aparece un elemento en el arreglo A, luego cuenta cuantos elementos tiene el arreglo A y finalmente construye el arreglo B de forma ordenada ascendentemente.


## RadixSort

### Descripción:

>RadixSort es un algoritmo de ordenamiento, que utiliza algún algoritmo estable como CountingSort para ordenar cifras dígito a dígito. Primero clasifica la cifra por el dígito menos significativo, luego clasifica la cifra de nuevo por el segundo dígito menos significativo, repitiendo el proceso hasta concatenar por el dígito más significativo.  
El algoritmo RadixSort presenta un tiempo para el peor caso de Θ(d(n + k)) y un tiempo promedio de Θ(d(n + k)).

### Implementación:

Estructura de datos: En cuanto a los parámetros que recibe el procedimiento, tenemos:

  *A: Arreglo de tipo entero, con enteros mayores o iguales a 0 de tamaño n, que contiene los elementos a ser ordenados.

  *d: Número entero, que contiene la cantidad de dígitos que tiene el número más grande dentro del arreglo a ordenar.

#### Detalles de la implementación:
La función RadixSort(A, d), ordena las cifras en el arreglo A según el dígito indicado, en donde para ello utiliza el algoritmo CountingSort.


## Tabla de tiempos

| Algoritmo  |  1.000    |      5.000  | 10.000        | 20.000         |         40.000  |            80.000  | 160.000            |
|------------|-----------|-------------|---------------|----------------|-----------------|--------------------|--------------------|
|Insertion   |119.17 4.37|3176.05 85.15|12636.64 176.93|54047.06 2732.47|222359.91 7240.41|1058902.12 141495.14|3919739.13 176022.85|
|MergeSort   |9.51   5.82|48.32    3.99|100.85     2.89|215.71     13.62|456.32       22.2|1082.6        230.08|2155.61       238.75|
|HeapSort    |14.06	 3.35|113.11    4.6|237.97     6.53|543.87     54.56|1145.31      53.5|2618.15       386.66|5331.61       209.64|
|QuickSort   |7.55   6.76|32.11    3.66|66.64      5.21|155.12      16.2|326.55      15.81|756.63         79.65|1575.38         74.6|
|RadQuickSort|5.94   6.69|47.97    3.96|92.88      2.36|218.09     30.24|427.07      24.19|967.93        134.56|2009.47       123.43|
|CountingSort|84.15  5.17|91.44    5.67|100.06     3.44|118.55     11.87|140.73       7.37|211.82         20.01|319.92         17.63|
|RadixSort   |12.04  3.35|60.82    3.05|112.33     3.63|247.4      29.91|496         48.06|1114.31          184|2125.91        98.67|

## Gráficas

![InsertionSort](images/Insertion.png?raw=true "InsertionSort")

### Actividades

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

