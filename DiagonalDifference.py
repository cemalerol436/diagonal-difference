import numpy as np

t =np.array([[-25, 12, 5, -2], [15, 6, 10, -26], [5, 6, 7, -8], [9, -10, 11, -12]])
print(t)

l = len(t)
k = []
p = []
i = 0
while i<l:
    a = t[i][i]
    k.append(a)
    b = t[i][l-i-1]
    p.append(b)

    i +=1
res = abs(sum(k)-sum(p))

print(sum(k), sum(p))
print(f"absolute difference:{res}")
