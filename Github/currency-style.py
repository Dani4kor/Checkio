def checkio(text):

    l = text.split(' ', )
    print l
    for x in l:
        if x[0] == '$':
            splitdot,nonitem = "", ""
            c = False
            count = 0

            indexitem = l.index(x)
            l.remove(x)

            if x[-1] == ',' or x[-1] == '.':
                x, nonitem = x[:-1], x[-1]
            countdot = x.count(".")
            countdot = countdot + x.count(",")

            for i in x:
                if i == ',' or i == '.':
                    c = True
                    count = 0
                if c:
                    count += 1
            count -= 1
            if countdot < 2:
                if count <= 2:
                    splitdot = x.replace(',', '.')
                elif count > 2:
                    splitdot = x.replace('.', ',')
            else:

                if count <= 2:
                    splitdot = x.replace(',','.')

                    splitdot = splitdot.replace('.', ',', (splitdot.count('.')-1))

                elif count > 2:
                    splitdot = x.replace('.', ',')
                    print splitdot


            if nonitem == ',' or nonitem == '.':
                splitdot = splitdot + nonitem
            l.insert(indexitem,splitdot)
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
