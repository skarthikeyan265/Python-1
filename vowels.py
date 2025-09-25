s = input().lower()
vowels = "aeiou"
c = 0
for l in s:
    if l in vowels:
        c += 1
print(c)