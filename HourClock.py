class HourClock:
    def __init__(self):
        self.hours_num = 0

    @property
    def hours(self):
        return self.hours_num

    @hours.setter
    def hours(self, incom_hours):
        self.hours_num = incom_hours % 12
        return self.hours_num
