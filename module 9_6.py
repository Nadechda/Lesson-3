def all_variants(text):
    i = 1
    while i !=len(text)+1:
        for k in range(len(text)-i+1):
            yield text[k:k + i]
        i += 1

a = all_variants("abc")
for i in a:
    print(i)
