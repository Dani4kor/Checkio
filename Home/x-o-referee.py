def checkio(game_result):
    hor_result = ""
    rotate_game_result  = zip(*game_result)
    l =[]


    for hor_elem in game_result:
       if hor_elem[0] == hor_elem[1] == hor_elem[2] and hor_elem[0] != ".":
           return hor_elem[0]


    for ver_elem in rotate_game_result:
        if ver_elem[0] == ver_elem[1] == ver_elem[2] and ver_elem[0] != ".":
            return ver_elem[0]

    for diagnl_elem in game_result:
        l.append(diagnl_elem)

    if l[0][0] == l[1][1] == l[2][2] and l[0][0] != ".":
        return l[0][0]

    if l[0][2] == l[1][1] == l[2][0] and l[0][2] != ".":
        return l[0][2]
        
    return "D"
    
    
    


    #return "D" or "X" or "O"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

