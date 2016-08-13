def checkio(text):
    l = text.split(' ', )
    for x in l:
        if '$' in x:
            splitext, nonitem = "", ""
            dot, coma = '.', ','
            c = False
            count = 0
            indexedot = l.index(x)
            l.remove(x)
            if x[-1] == coma or x[-1] == dot:
                x, nonitem = x[:-1], x[-1]
            countdot = x.count(dot)
            countdot = countdot + x.count(coma)
            for i in x:
                if i == coma or i == dot:
                    c = True
                    count = 0
                if c:
                    count += 1
            count -= 1
            if countdot < 2:
                if count <= 2:
                    splitext = x.replace(coma, dot)
                elif count > 2:
                    splitext = x.replace(dot, coma)
            else:
                if count <= 2:
                    splitext = x.replace(coma, dot)
                    splitext = splitext.replace(dot, coma, (splitext.count(dot) - 1))
                elif count > 2:
                    splitext = x.replace(dot, coma)
            if nonitem == coma or nonitem == dot:
                splitext = splitext + nonitem
            l.insert(indexedot, splitext)
    return ' '.join(l)




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
           "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
           "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
           "$1,234, $5,678 and $9", "Dollars without cents"

    assert checkio("Clayton Kershaw $31.000.000\n"
                   "Zack Greinke   $27.000.000\n"
                   "Adrian Gonzalez $21.857.143\n") == \
           ("Clayton Kershaw $31,000,000\n"
            "Zack Greinke   $27,000,000\n"
            "Adrian Gonzalez $21,857,143\n")
