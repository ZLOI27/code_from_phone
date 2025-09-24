class Klass():
    X = 42
    def __init__(self, y):
        self.y = y

klass = Klass(9)
print(klass.X, klass.y)
