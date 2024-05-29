numeros = [17, 2, 1, 8, 5, 3, 6, 3, 2, 4, 5, 3, 4, 6, 75, 5, 2, 42, 4, 23]

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