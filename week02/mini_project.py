import math
import os


def clear():
    if os.name == 'nt':
        os.system('cls')  # Windows Console Command
    else:
        os.system('clear')  # Unix-like Console Command


def print_menu():
    clear()
    print('Conversion Menu')
    print('#' * 40)
    print('1. Meter to Mile')
    print('2. Gram to Pound')
    print('3. Celsius to Fahrenheit')
    print('4. Degree to Radian')
    print('q. 종료')
    print('#' * 40)


def meter_to_mile():
    clear()
    print('Meter to Mile Conversion')
    print('#' * 40)
    meter = input('meter: ')
    print(f'{meter} meter >> {float(meter) / 1609} mile')
    input('press enter to exit')


def gram_to_pound():
    clear()
    print('Gram to Pound Conversion')
    print('#' * 40)
    gram = input('gram: ')
    print(f'{gram} gram >> {float(gram) / 453.6} pound')
    input('press enter to exit')


def celsius_to_fahrenheit():
    clear()
    print('Celsius to Fahrenheit Conversion')
    print('#' * 40)
    celsius = input('celsius: ')
    print(f'{celsius} celsius >> {float(celsius) * (9 / 5) + 32} fahrenheit')
    input('press enter to exit')


def degree_to_radian():
    clear()
    print('Degree to Radian Conversion')
    print('#' * 40)
    degree = input('degree: ')
    print(f'{degree} degree >> {float(degree) * (math.pi / 180)} radian')
    input('press enter to exit')


def main():
    while True:
        print_menu()
        menu = input('i: ')
        if menu == '1':
            meter_to_mile()
        elif menu == '2':
            gram_to_pound()
        elif menu == '3':
            celsius_to_fahrenheit()
        elif menu == '4':
            degree_to_radian()
        elif menu == 'q':
            break


if __name__ == '__main__':
    main()
