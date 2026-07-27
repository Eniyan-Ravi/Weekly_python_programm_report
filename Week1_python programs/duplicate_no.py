a=[2, 5, 1, 7, 5, 9]
b=set()
c=set()
for x in a:
    if x in b:
        c.add(x)
    else:
        b.add(x)
print(c)