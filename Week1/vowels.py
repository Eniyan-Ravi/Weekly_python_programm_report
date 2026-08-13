a="programmig"
vovels=['a','e','i','o','u']
b=a.lower()
c=set()
for x in b:
    if x in vovels:
        c.add(x)
print(c)