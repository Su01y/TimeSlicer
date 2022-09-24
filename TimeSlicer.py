import arrow
import datetime as dt


class TimeSlices:
    def __init__(self, start: arrow, end: arrow) -> None:
        self.start = start
        self.end = end
        self.now = self.start

    def __iter__(self):
        return self

    def __next__(self) -> arrow:
        if self.end - self.now.shift(days=+6) >= dt.timedelta(0):
            left = self.now
            self.now = self.now.shift(days=+6)
            right = self.now
            self.now = self.now.shift(days=+1)
            return left, right
        elif self.end - self.now > dt.timedelta(days=1):
            left = self.now
            self.now = self.now.shift(days=+6)
            right = self.end
            return left, right
        else:
            raise StopIteration


if __name__ == "__main__":
    sliser = tuple(TimeSlices(arrow.utcnow().shift(months=-1), arrow.utcnow()))
    for week in sliser:
        print(week)