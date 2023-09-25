def produce_fibonacci_sequence(n):
    cache = {0: 0, 1: 1}
    def _get_fibonacci(x):
        if not x in cache:
            cache[x] = _get_fibonacci(x - 1) + _get_fibonacci(x - 2)
        return cache[x]
    
    return "0".join([str(_get_fibonacci(i)) for i in range(n)])

print(produce_fibonacci_sequence(15) == "0010102030508013021034055089014402330377")

