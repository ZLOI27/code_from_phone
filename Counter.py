class Counter:
    value = 0

    def inc(self, delta=1):
        self.value += delta
        return self.value

    def dec(self, delta=1):
        self.value -= delta
        return self.value

