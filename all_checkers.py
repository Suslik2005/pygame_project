# проверка на победу
# true and flase выиграл  и проиграл соответсвенно
def winchecker(m):
    c = 0
    for i in m:
        for j in i:
            if j[1] == 2:
                c += 1
    if c == 36:
        return True
    else:
        return False


#просто чекер
def check(m):
    c = 0
    for i in m:
        for j in i:
            if j[1] == 1:
                c += 1
    if c != 2:
        return True
    else:
        return False


#проверка
#на
#similarity
def checksimilar(m, r):
    a = 0
    b = 0
    global map
    for i in m:
        for j in i:
            if j[1] == 1 \
                    and a == 0:
                a = j[0]
            elif j[1] == 1:
                b = j[0]
    if a == 0 or b == 0:
        return ["a", r]
    elif a == b:
        for i in range(6):
            for j in range(6):
                if map[i][j][1] == 1:
                    map[i][j][1] = 2
        r += 1
        return ["b", r]
    else:
        r += 1
        return ["c", r]
