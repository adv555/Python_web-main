import asyncio
from aiopath import AsyncPath
from parser import folder_parse
from time import time


async def start():
    path = input("Enter path to folder: ").strip()
    folder = AsyncPath(path)
    if await folder.exists() and len(path) > 0:
        try:
            start_time = time()
            await folder_parse(folder, folder)

            print(f'Parsing finished in {time() - start_time} seconds')

        except Exception as e:
            print('Error: ', e)

    else:
        print("Invalid path! Try again")
        await start()


if __name__ == '__main__':
    asyncio.run(start())

