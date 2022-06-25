import asyncio
import time


async def fun1(x):
    print(x ** 2)
    await asyncio.sleep(3)
    print(f'fun1 завершена')


async def fun2(x):
    print(x ** .5)
    await asyncio.sleep(3)
    print(f'fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2


if __name__ == '__main__':
    print(time.strftime('%X'))
    asyncio.run(main())
    print(time.strftime('%X'))
