n = int(input('n='))
a = []
for i in range(n):
    i = float(input())
    a.append(i)

print('the second smallest number is', + sorted(a)[1])
print('the second largest number is', + sorted(a)[-2])