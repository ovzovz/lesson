import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i+1} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    start1=asyncio.create_task(start_strongman('Pasha', 3))
    start2 = asyncio.create_task(start_strongman('Denis', 4))
    start3 = asyncio.create_task(start_strongman('Apollon', 5))
    await start1
    await start2
    await start3

asyncio.run(start_tournament())


