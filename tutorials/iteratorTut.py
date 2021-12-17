class zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)


class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        # Removing this function makes the class just an iterator and not iterable.
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


z = zrange(5)
print(z)
print(list(z))
print(list(z))

z = zrange_iter(5)
print(z)
print(list(z))
print(list(z))
