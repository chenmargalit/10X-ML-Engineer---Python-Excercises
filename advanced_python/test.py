import asyncio
import time

async def t1():
    print('1 is on')
    await asyncio.sleep(1)
    print('1 finished')


async def t2():
    print('2 is on')
    await asyncio.sleep(1)
    print('2 finished')


async def main():
    s = time.perf_counter()
    print('main started')
    await t1()
    await t1()


    elapsed = time.perf_counter() - s
    print(elapsed)

asyncio.run(main())