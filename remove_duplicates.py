# Remove Duplicates from a List
nl = list(map(int, input().split(",")))
r = []
for n in nl:
    if n not in r:
        r += [n]
print(r)

        
