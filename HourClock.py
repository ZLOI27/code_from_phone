class HourClock:
    def __init__(self):
        self.hours = 0

    @property
    def hours(self):
        return hours

    @hours.setter
    def hours(self, incom_hours):
        self.hours = incom_hours % 12
        return hours
