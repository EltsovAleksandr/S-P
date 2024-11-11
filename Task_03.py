import itertools


def max_odd(array):
    a = [i for i in array if isinstance(i, (int, float))]
    b = list(itertools.chain(*[i for i in array if isinstance(i, (list, tuple, set))]))
    if a == []:
        return None
    elif len(b) > 0:
        c = [i for i in a if i % 2 != 0] + [i for i in b if i % 2 != 0]
        if c == []:
            return None
        else:
            return (max(c))
    else:
        c = [i for i in a if i % 2 != 0]
        if c == []:
            return None
        else:
            return (max(c))
