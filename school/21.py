def int_R(n):
    print("первый перебор")
    yield n
    print("второй перебор")
    yield n+1

m = int(input("m="))
c = int_R(m)
print(next(c))

list_1=[4,9,25,36]
list_2=(i**(1/2) for i in list_1)
next
print(next(list_2))
print(next(list_2))

a=["Den","Vova","Sasha"]
def name():
    for t in a:
        yield t
c=name()
for i in c:
    print(i)
