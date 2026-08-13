a="python programming language"
b=a.split()
c=[]
for x in b:
    c.append(x[0].upper()+x[1:])
print(c)