import calendar


def most_frequent_days(year):
    freq_day = []

    first = calendar.weekday(year, 1, 1)
    last = calendar.weekday(year, 12, 31)

    if first == last:
        freq_day.append(calendar.day_name[first])
    elif first > last:
        freq_day.append(calendar.day_name[last]), freq_day.append(calendar.day_name[first])
    else:
        freq_day.append(calendar.day_name[first]), freq_day.append(calendar.day_name[last])
    return freq_day


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
     assert most_frequent_days(2399) ==  ['Friday'], "1st example"
     assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
     assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
     assert most_frequent_days(2909) == ['Tuesday'], "4th example"
