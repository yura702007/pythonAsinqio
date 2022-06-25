import time


def fun1(x):
    print(x ** 2)
    time.sleep(3)
    print(f'fun1 завершена')


def fun2(x):
    print(x ** .5)
    time.sleep(3)
    print(f'fun2 завершена')


def main():
    fun1(4)
    fun2(4)


if __name__ == '__main__':
    print(time.strftime('%X'))
    main()
    print(time.strftime('%X'))
