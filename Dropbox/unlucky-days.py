import datetime,calendar

def checkio(year):
    count = 0
    for x in range(1, 13):
        date = datetime.datetime(year, x, 13)
        if datetime.date.weekday(date) == calendar.FRIDAY:
            count += 1
    return count

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"