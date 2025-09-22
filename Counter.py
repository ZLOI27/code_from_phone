class Counter:
    value = 0

    def inc(self, delta=1):
        value += delta
        return value

    def dec(self, delta=1):
        value -= delta
        return value

