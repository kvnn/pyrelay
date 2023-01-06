import asyncio
import logging
from itertools import count

import websockets

from pynostr.client.client import NostrClient
from pynostr.nostr.event import NostrTag

WS_LOCALHOST = "ws://localhost:8001"

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger("PRODUCER CLIENT")


async def producer() -> None:
    async with websockets.connect(WS_LOCALHOST) as websocket:
        client = NostrClient(websocket)
        for i in count():
            tags = []
            tag = NostrTag(type="e", key="asdasdasdasdasd", extra=[WS_LOCALHOST])
            tags.append(tag)

            await client.send_event(f"{i}", tags=tags)
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(producer())
