# Minimum Number of Coins
cl = list(map(int, input().split(",")))
amount = int(input())
cl = cl[::-1]
no_of_coins = 0
for c in cl:
    count = amount // c
    if count > 0:
        no_of_coins += count
        amount -= c * count 
print(no_of_coins)
