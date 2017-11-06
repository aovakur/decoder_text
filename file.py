a = str(input("Ener string= "))
b = ['']*len(a)
for i in range(len(a)):
    b[i]=chr(ord(a[i])+2)
for i in b:
    print(i, sep='', end='')