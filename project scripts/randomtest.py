import random

sample_num = 1000000

randomnums = []
for i in range(sample_num):
    randomnums.append(random.randint(0, 100))

total = 0

for num in randomnums:
    total = total + num

#print(randomnums)

print(total/sample_num)


range_test = []
range_test2 = []

for i in range(10000):
    range_test.append(random.randint(0, 10))

for i in range(10000):
    range_test2.append(random.randint(0, 10))

print(len(range_test))

total = 0
for i in range(len(range_test)):
    star_diff = range_test[i] - range_test2[i]
    star_diff = abs(star_diff)
    star_diff =  star_diff * 10
    total = total + star_diff

eff_accu = 100 - total/len(range_test)

print("Random range acuuracy: ", eff_accu)