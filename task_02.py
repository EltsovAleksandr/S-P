def coincidence(list = None, range = None):
    if list == None or range == None:
        return []
    a = [i for i in range]
    b = []
    for i in list:
        if (type(i) in (int, float)) and a[0] <= i <= a[-1]:
            b.append(i)
    return b
