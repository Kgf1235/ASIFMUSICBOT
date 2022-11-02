import os

from telethon import Button, events

from NIXA import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/8a8b83c89ebd4cf872a19.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Ishq_ka_raja_143"
)

CAPTION = f"**𝗣 𝗢 𝗡 𝗚 😂 **\n\n   » {ms}\n   » ᴍʏ ᴍᴀsᴛᴇʀ ~『{ALIVE}』"


@NIXA.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[
             Button.url("• sᴜᴘᴘᴏʀᴛ •", url="https://t.me/DX_LUCKY"),
             Button.url("• ᴏᴡɴᴇʀ •", url="•https://t.me/Ishq_ka_raja_143")
                       ]]
    await NIXA.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
