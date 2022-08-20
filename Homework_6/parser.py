import asyncio
from aiopath import AsyncPath
import shutil
from normalize import normalize
from aiologger import Logger

logger = Logger.with_default_handlers(name='parser', level='INFO')


async def folder_parse(source_folder: AsyncPath, output_folder: AsyncPath) -> None:
    tasks = []

    async for item in source_folder.iterdir():
        if await item.is_dir():
            tasks.append(asyncio.create_task(folder_parse(item, output_folder)))
        else:
            tasks.append(asyncio.create_task(copy_file(item, output_folder)))

    await asyncio.gather(*tasks)

    if output_folder != source_folder:
        await handle_delete_folder(source_folder)


async def copy_file(file: AsyncPath, output_folder: AsyncPath) -> None:
    # logger.info(f'Copying {file} to {output_folder}')
    # tasks = []

    file_folder = file.suffix[1:].upper()
    if file.suffix in ('.jpeg', '.jpg', '.png', '.svg'):
        # tasks.append(asyncio.create_task(handle_media(file, output_folder / 'Images' / file_folder)))
        await handle_media(file, output_folder / 'Images' / file_folder)
    elif file.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
        # tasks.append(asyncio.create_task(handle_media(file, output_folder / 'Audio' / file_folder)))
        await handle_media(file, output_folder / 'Audio' / file_folder)
    elif file.suffix in ('.mp4', '.avi', '.mkv', '.mov'):
        # tasks.append(asyncio.create_task(handle_media(file, output_folder / 'Video' / file_folder)))
        await handle_media(file, output_folder / 'Video' / file_folder)
    elif file.suffix in ('.pdf', '.doc', '.docx', '.xlsx', '.txt', '.pptx', '.xml'):
        # tasks.append(asyncio.create_task(handle_documents(file, output_folder / 'Documents' / file_folder)))
        await handle_documents(file, output_folder / 'Documents' / file_folder)
    elif file.suffix in ('.zip', '.tar', '.gz'):
        # tasks.append(asyncio.create_task(handle_archive(file, output_folder / 'Archive' / file_folder)))
        await handle_archive(file, output_folder / 'Archives')
    else:
        # tasks.append(asyncio.create_task(handle_other(file,output_folder / 'Trash')))
        await handle_other(file, output_folder / 'Trash')

    # await asyncio.gather(*tasks)


async def handle_media(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(str(target_folder / normalize(filename.name)))


async def handle_documents(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(str(target_folder / normalize(filename.name)))


async def handle_other(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    await filename.replace(str(target_folder / normalize(filename.name)))


async def handle_archive(filename: AsyncPath, target_folder: AsyncPath):
    await target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    await folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename), str(folder_for_file))
    except shutil.ReadError:
        print(f'Fake archive {filename} was not unpacked!')
        await folder_for_file.rmdir()
        return None
    await filename.unlink()


async def handle_delete_folder(folder: AsyncPath):
    # logger.info(f'Deleting {folder}')
    if await folder.is_dir():
        try:
            await folder.rmdir()
        except OSError:
            print(f'Folder {folder} was not deleted!')
    else:
        print(f'{folder} is not a folder!')
