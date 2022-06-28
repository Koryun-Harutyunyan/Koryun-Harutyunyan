def inter_list():
    n = int(input('n='))
    for i in range(n):
        a = [float(input())]
    m = int(input('m='))
    for i in range(m):
        b = [float(input())]
    for x in a:
        for y in b:
            if x == y:
                return True
    return False


print(inter_list())
