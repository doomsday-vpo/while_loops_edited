# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети може да стане това.

# coins = [200, 100, 50, 20, 10, 5, 2, 1]
# change = float(input()) * 100
# coin_count = 0
# index = 0
#
# while change > 0 and index < len(coins):
#     coin_value = coins[index]
#     coin_count += change // coin_value
#     change %= coin_value
#     index += 1
#
# print(int(coin_count))

change = int(float(input()) * 100)
coin_count = 0
index = 0

while change > 0 and index < 8:
    coin_value = 200 if index == 0 else 100 if index == 1 else 50 if index == 2 else 20 if index == 3 else 10 if index == 4 else 5 if index == 5 else 2 if index == 6 else 1
    if change >= coin_value:
        coin_count += change // coin_value
        change %= coin_value
    else:
        index += 1

print(coin_count)




