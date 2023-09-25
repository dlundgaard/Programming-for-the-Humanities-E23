class _str(str):
    def __init__(self, string):
        assert isinstance(string, (str, self))
        self.content = string

    def __mul__(self, other):
        assert isinstance(other, (str, self))
        return self + other

    def __rmul__(self, other):
        return self.__mul__(other)[::-1]

print(_str("a") * "b")
print("a" * _str("b"))
