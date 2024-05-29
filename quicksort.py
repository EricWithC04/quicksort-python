numeros = [17, 2, 1, 8, 5, 3, 6, 3, 2, 4, 5, 3, 4, 6, 75, 5, 2, 42, 4, 23]
numeros2 = [12, 20, 3, 8, 19, 1, 23, 7, 14, 16, 21, 6, 5, 24, 10, 4, 25, 18, 21]
numeros3 = [17, 3, 22, 11, 19, 6, 25, 9, 2, 20, 5, 12, 24, 4, 15, 13, 10, 8, 21, 7]

# Funcion para realizar la particion en cada iteración y obtener el indice de el elemento ordenado
def partition(arr, min, max):
	pivot = arr[max]

	# Indice del elemento
	i = min - 1

	# Recorremos la lista desde la posicion minima hasta la maxima
	for j in range(min, max):
		if arr[j] <= pivot:

			i = i + 1

			# En el caso de que se encuente un elemento superior al actual, ese elemento y el actual son intercambiados
			(arr[i], arr[j]) = (arr[j], arr[i])
	# Se intercambian el elemento de la ultima posicion con el siguiente de la lista con la posicion actual
	(arr[i + 1], arr[max]) = (arr[max], arr[i + 1])

	# Retornamos el siguiente de la posicion actual (debido a que el actual ya está colocado donde debe estar)
	return i + 1

# Funcion del algoritmo de ordenamiento
def quick_sort(arr, min, max):
	# Es caso de cierre será cuando la posicion minima coincida con la maxima
	if min < max:
		# Invocamos la función de partición para ordenar un numero y obtener su posicion
		pi = partition(arr, min, max)

		# Invocamos recursivamente quick_sort y le pasamos las posiciones con las cuales se armaran ambas sublistas
		quick_sort(arr, min, pi - 1)
		quick_sort(arr, pi + 1, max)

# Prueba 1
print(numeros)
quick_sort(numeros, 0, len(numeros) - 1)
print(numeros)

# Prueba 2
print(numeros2)
quick_sort(numeros2, 0, len(numeros2) - 1)
print(numeros2)

# Prueba 3
print(numeros3)
quick_sort(numeros3, 0, len(numeros3) - 1)
print(numeros3)