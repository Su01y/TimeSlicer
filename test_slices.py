from TimeSlicer import TimeSlices
import arrow


def test_year_by_weeks():
    date_from = arrow.utcnow().shift(years=-1)
    date_to = arrow.utcnow()

    slices = tuple(i for i in TimeSlices(date_from, date_to))
    
    assert len(slices) == 53
    assert slices[0][0] == date_from
    assert slices[-1][1] == date_to


def test_months_by_weeks():
    date_from = arrow.utcnow().shift(months=-1)
    date_to = arrow.utcnow()

    slices = tuple(i for i in TimeSlices(date_from, date_to))
    
    assert len(slices) == 5
    assert slices[0][0] == date_from
    assert slices[-1][1] == date_to


def test_small_period():
    date_from = arrow.utcnow().shift(hours=-1)
    date_to = arrow.utcnow()

    slices = tuple(i for i in TimeSlices(date_from, date_to))
    
    assert len(slices) == 0


def non_correct_period():
    date_to = arrow.utcnow().shift(months=-1)
    date_from = arrow.utcnow()

    slices = tuple(i for i in TimeSlices(date_from, date_to))
    
    assert len(slices) == 0


if __name__ == "__main__":
    test_year_by_weeks()
    test_months_by_weeks()
    test_small_period()
    non_correct_period()
