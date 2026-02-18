p = int(input("termo: "))
r = int(input("razão: "))

termo = p
c = 1

while c <=10:
    print("{} -> ".format(termo), end="")
    termo += r
    c += 1
print("finito")