def checkio(text):

    l = text.split(' ', )
    print l
    for x in l:
        if x[0] == '$':
            splitdot = ""
            nonitem = ""
            indexitem = l.index(x)
            l.remove(x)
            if x[-1] == ',' or x[-1] == '.':
                x, nonitem = x[:-1], x[-1]
            countdot = x.count(".")
            countdot = countdot + x.count(",")
            if countdot < 2:
                splitdot = x.replace(',','.')
            else:
                splitdot = x.replace(',','.')
                splitdot = splitdot.replace('.', ',', (splitdot.count('.')-1))
            if nonitem == ',' or nonitem == '.':
                splitdot = splitdot + nonitem
            l.insert(indexitem,splitdot)
    print ' '.join(l)










if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    # assert checkio("$0,89") == "$0.89", "2nd Example"
    # assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
    #        "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    # assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
    #        "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
           "$1,234, $5,678 and $9", "Dollars without cents"
