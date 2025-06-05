import random

def generate_arrays(n, seed=None):
    if seed is not None:
        random.seed(seed)
    return {
        'sorted': list(range(n)),
        'reversed': list(range(n, 0, -1)),
        'random': random.sample(range(n * 2), n)
    }
