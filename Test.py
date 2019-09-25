class Date():
    def __init__(self, year, month, day):
        self.j_Day = self._toJulianDay(year, month, day)

    def _toJulianDay(self, year, month, day):
        return 1

a = Date(1, 2, 3)

