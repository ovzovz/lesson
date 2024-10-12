def all_variants(text):
    for len_ in range(1, len(text) + 1):
        for i in range(0, len(text) + 1 - len_):
            yield text[i: (i + len_)]


a = all_variants("abc")
for i in a:
    print(i)
