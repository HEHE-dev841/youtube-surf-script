import asyncio

async def main():
    loop = asyncio.get_event_loop()

    coro = asyncio.open_connection('192.168.124.2', 8888)
    conn, addr = await loop.run_until_complete(coro)

    message = "Hello from client"
    data = f"{message}\n".encode()
    await conn.send_all(data)

    while True:
        response = await conn.receive()
        print(response.decode())

    conn.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
