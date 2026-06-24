import os
import anthropic
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

API_ID = 33156265
API_HASH = "519c4be248db5d5c4494f34f2147659f"
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY")

claude = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

async def auto_reply(client, message):
    if not message.text:
        return
    response = claude.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": message.text}]
    )
    await message.reply(response.content[0].text)

app.add_handler(MessageHandler(auto_reply, filters.incoming & filters.private))
app.run()
