import asyncio
from BinaryOptionsToolsV2.pocketoption import PocketOptionAsync

async def main():
    # Initialize client with SSID
    ssid = (r'your_ssid_here')
    client = PocketOptionAsync(ssid)

    await asyncio.sleep(3)  # Wait for initialization

    # Get account balance
    balance = await client.balance()
    print(f"Balance: ${balance}")

if __name__ == "__main__":
    asyncio.run(main())
