# Chunk a List into Sublist
nl = list(map(int, input().split(",")))
n = int(input())
r = []
for i in range(0, len(nl), n):
    r += [nl[i:n+i]]
print(r) 
