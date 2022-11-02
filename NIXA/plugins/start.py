from NIXA import NIXA
from telethon import events, Button
from Config import BOT_USERNAME

@NIXA.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ʜᴇʟʟᴏ ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ ʙᴏᴛ")
ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs. ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ʙᴀsᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ
@Loveofmusic_assistant ...",
                    buttons=[
                        [
                          Button.url("➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url="https://t.me/{BOT_USERNAME}?startgroup=true")],
                       ],
                       [
                          Button.url("• sᴜᴘᴘᴏʀᴛ •", url="https://t.me/all_bot_lucky"),
                          Button.url("• ᴏᴡɴᴇʀ •", url="https://t.me/Ishq_ka_raja_143")
                       ],
                       [
                          Button.url("• ᴀssɪsᴛᴀɴᴛ •", url="https://t.me/DX_LUCKY"),
                          Button.url("• ᴛʜᴀᴍʙɪ    •", url="https://t.me/all_bot_lucky")
                       ]
                       )
