def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        trocou = False  # Otimização: evita loops desnecessários
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        # Se não houve troca, já está ordenado
        if not trocou:
            break
