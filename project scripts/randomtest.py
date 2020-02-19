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