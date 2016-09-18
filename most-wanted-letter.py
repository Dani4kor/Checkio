from collections import Counter

def checkio(text):
    text = text.lower()
    n_text = ""
    return_word = []
    if not text.isalpha():
        for digit in text:
            if digit.isalpha():
                n_text = n_text + digit
        c = [c * 1 for c in n_text]
        d_count = Counter(c)
        text = sorted(d_count.items(), key=lambda x: -x[1])
    else:
        c = [c * 1 for c in text]
        d_count = Counter(c)
        text = sorted(d_count.items(), key=lambda x: -x[1])
    for word in text:
        if text[0][1] == word[1]:
            return_word.append(word[0])

    return_word.sort()
    return return_word[0]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
