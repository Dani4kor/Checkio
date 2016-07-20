def checkpol(last_result, new_result):
    if str(last_result) == str(last_result)[::-1]:
        if len(last_result) > len(new_result):
            new_result = last_result
    return new_result


def longest_palindromic(text):
    work_text = ""
    result = ""
    count = 0

    for i in text:
        work_text = work_text + i
        result = checkpol(work_text, result)
    for x in xrange(len(text)):
        count += 1
        result = checkpol(text[count:], result)
    for x in xrange(len(text)):
        count = 0
        count += 1
        result = checkpol(text[count:-count], result)

    return result



if __name__ == '__main__':
    assert longest_palindromic("artrrtrt") == "rtrrtr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    # assert longest_palindromic("sosaddasli") == "saddas", "THE sad das"
