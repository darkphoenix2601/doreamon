from telethon import events, Button, custom
import re, os
from tg_bot.events import register
from tg_bot import telethn as tbot
from tg_bot import telethn as tgbot
PHOTO = "https://telegra.ph/file/c32d7da072ed1416f82b3.jpg"
@register(pattern=("/alive"))
async def awake(event):
 Miss_Akshi = event.sender.first_name
 Miss_Akshi = "** I,m Doreamon** \n\n"
 Miss_Akshi += "** I'm Working with awesome speed**\n\n"
 Miss_Akshi += "** Doreamon : 1.0 LATEST**\n\n"
 Miss_Akshi += "** 𝘔𝘺 𝘰𝘸𝘯𝘦𝘳 :** [𝘈𝘴𝘩𝘶👑](t.me/akshi_S_ashu)\n\n"
 Miss_Akshi += "** Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("𝘚𝘶𝘱𝘱𝘰𝘳𝘵🔥", "https://t.me/phoenix_music_suport"), Button.url("𝘜𝘱𝘥𝘢𝘵𝘦𝘴", "https://t.me/phoenix_music_new")]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Miss_Akshi,  buttons=BUTTON)
