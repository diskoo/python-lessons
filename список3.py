n = list(range(1000, 1025))
a = n[::-1]
m = []

for i, v in enumerate(n):
    if v % 2 != 0:
        m.append(n.pop(i))
    

print(m)
print(a)