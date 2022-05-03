def get_url_chat_id(chat_id: int):
    return abs(chat_id + 1_000_000_000_000)

async def fetch_bin(session, url: str):
    async with session.get(url) as resp:
        return await resp.read()

