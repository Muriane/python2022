def multiplication(valeur, max=10):
    for i in range(1, max):
     print("{:1}".format(valeur * i), end=" : ")
    print("{:1}".format(valeur * max))


def table_pythagore(max = 10):
    print(("------" * max)[:-3])
    for i in range(1, max + 1):
        multiplication(i, max)
        print(("------" * max)[:-3])


#multiplication(4)
table_pythagore()