import asyncio
from bot import Bot
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1002807868892
#If Bot goes rogue use pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
if __name__ == "__main__":
    asyncio.run(Bot().run())
