import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    result = 0
    check = ""
    words = filter(bool, re.split(",| |\.|\?", text.upper()))
    for i in words:
        for let in i:
            if let in VOWELS:
                check += "1"
            if let in CONSONANTS:
                check += "0"
        q, p = 1, 0
        if len(check) == 1 or any(char.isdigit() for char in i):
            result += 1
        else:
            for x in xrange(len(i) - 1):
                if check[q] != check[p]:
                    q, p = q + 1, p + 1
                else:
                    q, p = q + 1, p + 1
                    result += 1
                    break
        check = ""
    result = len(words) - result
    return result


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"


