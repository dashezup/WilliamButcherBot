from wbb import app
from pyrogram import filters
from wbb.utils import cust_filter, random_line

__MODULE__ = "Commit"
__HELP__ = "/commit - To Generate Funny Commit Messages"


@app.on_message(cust_filter.command(commands=("commit")))
async def commit(client, message):
    await message.reply_text((await random_line('wbb/utils/commit.txt')))
