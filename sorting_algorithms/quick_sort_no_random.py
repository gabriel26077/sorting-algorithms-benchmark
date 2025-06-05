def quick_sort_no_random(arr):
    def _quick_sort(arr, baixo, alto):
        if baixo < alto:
            pi = particionar(arr, baixo, alto)
            _quick_sort(arr, baixo, pi - 1)
            _quick_sort(arr, pi + 1, alto)

    def particionar(arr, baixo, alto):
        pivo = arr[alto]
        i = baixo - 1
        for j in range(baixo, alto):
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
