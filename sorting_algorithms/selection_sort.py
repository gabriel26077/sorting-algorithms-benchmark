def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume que o menor elemento está na posição i
        min_index = i
        # Encontra o índice do menor elemento na parte não ordenada
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca o elemento atual pelo menor encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]
