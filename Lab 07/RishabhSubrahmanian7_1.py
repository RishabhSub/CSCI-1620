def one(n):
    if n == 1:
        return 1
    else:
        return n + one(n - 1)


def two(num, exp):
    if exp == 1:
        return num
    else:
        return num * two(num, exp - 1)


def three(n):
    if n == 1:
        print(n)
    else:
        print(n, end=' ')
        three(n - 1)


def main():
    print(one(1))       # 1
    print(one(2))       # 3
    print(one(3))       # 6
    print(one(4))       # 10

    print()
    print(two(2, 1))    # 2
    print(two(2, 2))    # 4
    print(two(2, 3))    # 8
    print(two(3, 4))    # 81

    print()
    three(5)            # 5 4 3 2 1
    print()
    three(10)           # 10 9 8 7 6 5 4 3 2 1


if __name__ == '__main__':
    main()


