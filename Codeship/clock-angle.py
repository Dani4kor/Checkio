def clock_angle(time):
    hour, minute = time.split(':')
    hour, minute = float(hour), float(minute)
    if hour >= 12:
        hour -= 12
    min_angle, hour_angle = float((360/60)*minute), float((minute/2)+(360/12)*hour)
    if min_angle == 0 and hour_angle == 180:
        return 180
    elif abs(min_angle-hour_angle) <= 180:
        return abs(min_angle-hour_angle)
    else:
        return 360-abs(min_angle-hour_angle)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"



