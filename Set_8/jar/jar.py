class Jar(object):
    def __init__(self, capacity=12):
        self._size = 0
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self._size

    def deposit(self,n):
        if self._size + n <= self.capacity:
            self._size += n
        else:
            raise ValueError ("Not enough capacity")

    def withdraw(self,n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError ("Not enough cookies left")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity > 0 and capacity >= self._size:
            self._capacity = capacity
        else:
            raise ValueError ("Invalid capacity")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        raise AttributeError("Size can only be changed only by .deposit and .withdraw methods")


def main():
    jar = Jar()
    jar.deposit(2)
    jar.deposit(5)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()

