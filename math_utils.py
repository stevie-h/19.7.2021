# ex23


def compare(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        raise Exception("Numbers are equal")


def three_multiple(x):
    if x % 3 == 0:
        return True
    else:
        return False


def power(a, n):
    return a ** n
