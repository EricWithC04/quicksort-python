numeros = [17, 2, 1, 8, 5, 3, 6, 3, 2, 4, 5, 3, 4, 6, 75, 5, 2, 42, 4, 23]
numeros2 = [12, 20, 3, 8, 19, 1, 23, 7, 14, 16, 21, 6, 5, 24, 10, 4, 25, 18, 21]
numeros3 = [17, 3, 22, 11, 19, 6, 25, 9, 2, 20, 5, 12, 24, 4, 15, 13, 10, 8, 21, 7]

def partition(arr, min, max):
	pivot = arr[max]

	i = min - 1

	for j in range(min, max):
		if arr[j] <= pivot:

			i = i + 1

			(arr[i], arr[j]) = (arr[j], arr[i])

	(arr[i + 1], arr[max]) = (arr[max], arr[i + 1])

	return i + 1

def quickSort(arr, min, max):
	if min < max:
		pi = partition(arr, min, max)

		quickSort(arr, min, pi - 1)
		quickSort(arr, pi + 1, max)

print(numeros)
quickSort(numeros, 0, len(numeros) - 1)
print(numeros)

print(numeros2)
quickSort(numeros2, 0, len(numeros2) - 1)
print(numeros2)

print(numeros3)
quickSort(numeros3, 0, len(numeros3) - 1)
print(numeros3)