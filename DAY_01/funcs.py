def add(x, y):
    return x+y


def div(x, y):
    return x/y if y else None


if __name__ == '__main__':
    print(add(3, 4))
    print(div(3, 4))
