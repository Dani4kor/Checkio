from datetime import date,timedelta


def checkio(from_date, to_date):
    weekend = 0
    while from_date <= to_date:
        if from_date.isoweekday() == 7 or from_date.isoweekday() == 6:
            weekend += 1
        from_date += timedelta(days=1)

    return weekend


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

