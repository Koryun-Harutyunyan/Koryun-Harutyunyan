#Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter. (try to find the optimal solution :))
def add_it_up():
    m = int(input('m='))
    sum1 = 0
    while m != 0:
        m -= 1
        sum1 += m
    print(sum1)
add_it_up()