
n =1260
count =0

coin_types=[500, 100, 50, 10]

for c in coin_types:
     count += n//c
     n = n%c

print(count)