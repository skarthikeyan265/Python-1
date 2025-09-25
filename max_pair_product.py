# Maximum Product of Two Numbers in a List
nl = list(map(int, input().split(",")))

r = 0
for i in range(len(nl)-1):
    for j in range(i+1, len(nl)):
        mul = nl[i] * nl[j]
        if (mul > r):
            r = mul
print(r)