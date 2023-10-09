class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        if self.size == 0:
            return "No cookies in jar"
        else:
            return "🍪" * self.size

    def deposit(self,n):
        try:
            int(n)
            if self.size + n <= self.capacity:
                self._size += n
            else:
                raise ValueError ("Not enough capacity")
        except ValueError:
            raise ValueError ("Invalid number of cookies")

    def withdraw(self,n):
        try:
            int(n)
            if self.size - n >= 0:
                self._size -= n
            else:
                raise ValueError ("Not enough cookies left")
        except ValueError:
            raise ValueError ("Invalid number of cookies")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        try:
            int(capacity)
            if capacity > 0 and capacity >= self.size:
                self._capacity = capacity
            else:
                raise ValueError ("Invalid capacity")
        except ValueError:
            raise ValueError ("Invalid capacity")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size == 0:
            self._size = size
        else:
            print ("Size can only be changed only by .deposit and .withdraw methods")


def main():
    jar = Jar()
    jar.deposit(3)
    jar.deposit(5)
    jar.withdraw(3)
    print(jar)


if __name__ == "__main__":
    main()

