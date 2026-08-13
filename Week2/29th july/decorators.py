#Decorators 
def greatfirst(func):
    def wrap(a,b):
        if a>b:
            a,b=b,a
        return func(a,b)
    return wrap
@greatfirst
def sub(a,b):
    return a-b

def divide(a,b):
    return a/b

divide=greatfirst(divide)
res1=divide(20,80)
print(res1)
res2=sub(2,8)
print(res2)