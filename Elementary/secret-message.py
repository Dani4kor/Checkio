def find_message(text):
    """Find a secret message"""
    upp_word = ""
    for is_upp in text:
        if is_upp.isupper():
            upp_word += is_upp
    return upp_word


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message(u"How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message(u"hello world!") == "", "Nothing"
    assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
