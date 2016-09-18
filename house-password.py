def checkio(data):
    # not the best solution... Yep.
    upp, low, dig = 0, 0, 0
    l = [l * 1 for l in data]
    if len(l) >= 10:
        for word in l[:]:
            if str.isupper(str(word)):
                upp = + 1
                if upp > 1:
                    upp -= 1
            if str.islower(str(word)):
                low += 1
                if low > 1:
                    low -= 1
            if str.isdigit(str(word)):
                dig += 1
                if dig > 1:
                    dig -= 1
    result = upp + low + dig
    if result == 3:
        return True
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
