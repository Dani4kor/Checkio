def checkio(data):
    l = data
    l.sort()
    if len(l) % 2 == 1:
        odd = len(l)//2
        return l[odd]
    else:
        upp_middle = len(l)//2
        low_middle = len(l)//2-1
        left_corner = l[upp_middle]
        right_corner = l[low_middle]
        sum_result = (left_corner+right_corner)
        float_type = float(sum_result)
        result = float(float_type/2)
        return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(range(1000000)) == 499999.5, "Long."
    print("The local tests are done.")