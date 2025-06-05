def counting_sort(arr):
    if len(arr) == 0:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Conta as ocorrências de cada valor
    for num in arr:
        count[num] += 1
    
    # Reconstrói o array ordenado
    index = 0
    for num, freq in enumerate(count):
        for _ in range(freq):
            arr[index] = num
            index += 1
