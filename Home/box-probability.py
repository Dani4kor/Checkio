def checkio(marbles, step):
    l = len(marbles)
    w = marbles.count('w')
    white = float(w)            # 1.0
    black = float(l - w)        # 2.0
    for i in xrange(step - 1):
        white, black = [white / l * (white - 1) + black / l * (white + 1),
                        black / l * (black - 1) + white / l * (black + 1)]
    return round(white / l, 2)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
