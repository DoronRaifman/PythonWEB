class Foo:
    def __init__(self):
        self._fs: int = int(5000)

    @property
    def fs(self):
        return self._fs

    @fs.setter
    def fs(self, value: int):
        self._fs = value


if __name__ == '__main__':
    print("Demonstrate properties")
    foo1 = Foo()
    print(f"fs={foo1.fs}")
    foo1.fs = 200
    print(f"fs={foo1.fs}")

