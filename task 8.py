random_list = []
for i in range(int(input('n='))):
    random_list.append(input())
frequency = {}

for item in random_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)
