def fibonacci():
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a + b


def p2():
    print(60 * 60)
    seconds_per_hour = 60 * 60
    print(seconds_per_hour * 24)
    seconds_per_day = seconds_per_hour * 24
    print(seconds_per_day / seconds_per_hour)
    print(seconds_per_day // seconds_per_hour)


def p4_1():
    guess_me = 7
    if guess_me < 7:
        print('too low')
    elif guess_me > 7:
        print('too high')
    else:
        print('just right')


def p4_2(start=0):
    guess_me = 7
    while True:
        if start < guess_me:
            print('too low')
        elif start == guess_me:
            print('found it!')
        elif start > guess_me:
            print('oops')
            break
        start = start + 1


def p4_3():
    l = [3, 2, 1, 0]
    for e in l:
        print(e)


def main():
    print("Hello, world!")
    fibonacci()
    p2()
    p4_1()
    p4_2(8)
    p4_3()


if __name__ == '__main__':
    main()
