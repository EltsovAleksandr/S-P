def connect_dicts(dict1, dict2):
    s1 = sum(dict1.values())
    s2 = sum(dict2.values())
    dict3 = dict()
    if s1 <= s2:
        for k, v in dict1.items():
            if v > 10:
                dict3[k] = v
        for k, v in dict2.items():
            if v > 10:
                dict3[k] = v
    else:
        for k, v in dict2.items():
            if v > 10:
                dict3[k] = v
        for k, v in dict1.items():
            if v > 10:
                dict3[k] = v

    dict3 = dict(sorted(dict3.items(), key = lambda val: val[1]))
    return dict3
