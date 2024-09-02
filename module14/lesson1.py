import time
import asyncio

async def get_temp():
    print('First message')
    time.sleep(2)
    print('24 c')

async def get_pres():
    print('Second message')
    time.sleep(4)
    print('101 kpa')

async def main():
    print('Start')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_pres())
    await task1
    await task2
    print('Finish')

start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Work time = {round(finish-start, 2)} seconds' )














