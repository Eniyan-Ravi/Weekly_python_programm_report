a="python is easy python is powerful"
b=a.split()
c={}
for x in b:
    if x in c:
        c[x]+=1
    else:
        c[x]=1
print(c)