from math import pi, acos


def checkio(a, b, c):
    a, b, c = sorted([x for x in a, b, c])

    # https://en.wikipedia.org/wiki/Solution_of_triangles
    if a + b <= c or b + c <= a or c + a <= b:
        return [0, 0, 0]
    anglA = round(acos((b ** 2 + c ** 2 - a ** 2) / float(2 * b * c)) / pi * 180)
    anglB = round(acos((a ** 2 + c ** 2 - b ** 2) / float(2 * a * c)) / pi * 180)
    anglY = 180 - anglA - anglB
    return [anglA, anglB, anglY]

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
