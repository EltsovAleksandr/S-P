def sort_list(list: list):
    x = len(list)
    if not list:
        return []
    elif x == 1:
        list.append(list[0])
        return list
    else:
        tMax = list.index(max(list))  # индекс макс
        nMax = max(list)  # Число макс
        tMin = list.index(min(list))  # индекс мин
        nMin = min(list)  # Число мин
        a = []  # для индексов макc
        b = []  # для индексов мин
        for i in range(x):
            if list[i] == nMax:
                a.append(i)
                a.sort()
            elif list[i] == nMin:
                b.append(i)
                b.sort()
        if len(a) == 1 and len(b) == 1:
            list[tMax], list[tMin] = list[tMin], list[tMax]
            list.append(nMin)
            return list
        elif len(b) > 1 and len(a) == 1:
            for i in b:
                list.pop(i)
                list.insert(i, nMax)
            list.pop(a[0])
            list.insert(a[0], nMin)
            list.append(nMin)
            return list

        elif len(a) > 1 and len(b) == 0:
            for i in a:
                list.pop(i)
                list.insert(i, nMin)
            list.pop(b[0])
            list.insert(b[0], nMax)
            list.append(nMin)
            return list
