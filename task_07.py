def combine_anagrams(words_array: list):
    a = {''.join(sorted(i)): [] for i in words_array}
    b = [''.join(sorted(i)) for i in words_array]
    for i in range(len(words_array)):
        a[b[i]].append(words_array[i])
    return (list(a.values()))

