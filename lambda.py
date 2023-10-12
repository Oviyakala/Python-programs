#x=lambda a: a+10
#print(x(10))
#x=lambda a,b :a*b
#print(x(5,6))
#x=lambda a,b,c :a+b+c
#print(x(5,6,2))
def myfun(n):
    return lambda a:a*n
mydoubler = myfun(2)
mytripler = myfun(3)
print(mydoubler(11))
print(mytripler(11))