#. Write a Python program to get the largest and smallest numbers from a list.
a = []
n = int(input())
for i in range(n):
    a.append(float(input()))

max1=a[1]
min1=a[1]
for elem in a:
	if elem > max1:
		max1 = elem
print(max1)
for elem in a:
	if elem < min1:
		min1=elem
print(min1)