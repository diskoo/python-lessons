n = list(range(1000, 1025))
print(n)
m = []

for i, v in enumerate(n):
    if v % 2 != 0:
        m.append(n.pop(i))

print(m)