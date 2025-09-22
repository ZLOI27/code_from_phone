class LimitedCounter(Counter):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        super().inc(amount)
        self.value = min(self.value, 10)
