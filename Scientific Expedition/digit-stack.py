def digit_stack(commands):
    l, k = [], []
    if not commands:
        return 0
    else:
        for x in commands:
            if "PUSH" in x:
                l.append(int(x[-1]))
            elif "POP" in x:
                if not l:
                    k.append(0)
                else:
                    k.append(l.pop())
            elif "PEEK" in x:
                if not l:
                    k.append(0)
                else:
                    k.append(l[-1])
    return sum(k)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
