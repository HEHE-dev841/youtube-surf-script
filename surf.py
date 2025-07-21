import asyncio
import aiohttp

class SurfWeb:
    def __init__(self, proxy=None):
        self.proxy = proxy

    async def surf(self, url):
        try:
            connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url, proxy=self.proxy) as response:
                    return await response.text()
        except Exception as e:
            print(f"Error: {e}")
            return None

    async def start(self):
        urls = [
            "https://www.youtube.com",  # Example real URL
            # Add more URLs if you want
        ]
        for url in urls:
            print(f"Surfing: {url}")
            content = await self.surf(url)
            if content:
                print(f"Received {len(content)} characters from {url}\n")
            else:
                print("Failed to get content\n")

async def main():
    # Use proxy if you have one, e.g. 'http://user:pass@proxyserver:port'
    proxy = None
    surfer = SurfWeb(proxy=proxy)
    await surfer.start()

if __name__ == "__main__":
    asyncio.run(main())
