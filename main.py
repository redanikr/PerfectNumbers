def basic(a):
    b = 1
    array = []
    while b < a:
        if a % b == 0:
            array.append(b)
        b += 1
    if sum(array) == a:
        print("Number is perfect")
    else:
        print("Number is not perfect")


def finder(a):
    b = 1
    z = a
    array = []
    a = 1
    while a <= z:
        while b < a:
            if a % b == 0:
                array.append(b)
            b += 1
        if sum(array) == a:
            print("Number\t" + str(a) + "\tis perfect")
        else:
            pass
            #print("Number\t" + str(a) + "\tis not perfect")
        b = 1
        a += 1
        array.clear()


basic(33550336)
