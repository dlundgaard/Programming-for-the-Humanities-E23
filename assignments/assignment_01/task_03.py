"""
Returns string of joined, 0-padded terms of the fibonacci sequence. 
Caching/memoization reduces time complexity to O(n).
"""
def produce_fibonacci_sequence(n):
    cache = {0: 0, 1: 1}
    def _get_fibonacci(x):
        if not x in cache:
            cache[x] = _get_fibonacci(x - 1) + _get_fibonacci(x - 2)
        return cache[x]
    return "0".join([str(_get_fibonacci(i)) for i in range(n)])

if __name__ == "__main__":
    print("Produced sequence:           ", produce_fibonacci_sequence(15))
    print("Matches prescribed sequence: ", produce_fibonacci_sequence(15) == "0010102030508013021034055089014402330377")