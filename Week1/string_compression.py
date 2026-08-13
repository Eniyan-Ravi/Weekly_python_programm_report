#string compression 
a="aabbccccd"
store=""
count=1
for x in range(len(a)):
    if x<len(a)-1 and a[x]==a[x+1]:
        count+=1
    else:
        store+=a[x]+str(count)
        count=1
print(store)