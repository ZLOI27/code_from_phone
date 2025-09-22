class LimitedCounter(Counter):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def inc(self, amount=1):
        self.value = min(super().inc(amount), 10)

