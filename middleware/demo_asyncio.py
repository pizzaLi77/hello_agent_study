import asyncio

async def main():
    loop = asyncio.get_running_loop()
    print(loop)

asyncio.run(main())