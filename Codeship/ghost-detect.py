def recognize(number):
    import re
    return len(set(re.findall('1+', bin(number)[2:]))) == 1
