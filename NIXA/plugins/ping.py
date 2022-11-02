import os

from telethon import Button, events

from NIXA import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/83fe7f289d905033724b4.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Loveofmusic_assistant"
)

CAPTION = f"**𝗣 𝗢 𝗡 𝗚 😂 **\n\n   » {ms}\n   » ᴍʏ ᴍᴀsᴛᴇʀ ~『{ALIVE}』"


@NIXA.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[
             Button.url("• sᴜᴘᴘᴏʀᴛ •", url="https://t.me/Loveofmusic_assistant"),
             Button.url("• ᴏᴡɴᴇʀ •", url="•https://t.me/LoCaL_kInG_01")
                       ]]
    await NIXA.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
