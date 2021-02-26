import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'lol' 
EDIT_SLEEP = 1
#edit how many times in 'lol' 
EDIT_TIMES = 10

#sleep how many times after each edit in 'repo' 
EDIT_SLEEP = 1
#edit how many times in 'repo' 
EDIT_TIMES = 2


lol_ani = [ 
          
            " ✰ WAAH ✰ㅤㅤ[ㅤ](https://telegra.ph/file/a19b0bf4760fca85bd961.png) ",
            " ✰ LOL ✰ㅤㅤㅤ[ㅤ](https://telegra.ph/file/ed23819c84bab66e7d92f.png) ",
            " ✰ ELECTRIC BILL KON BHAREGA ✰ㅤ[ㅤ](https://telegra.ph/file/53c85b5b354212496746f.png) ",
            " ✰ JHINGA LALA ✰  [ㅤ](https://telegra.ph/file/1379a8c9ea40eaa463fd8.png) ",
            " ✰ NIMJA TECHNIQUE ✰[ㅤ](https://telegra.ph/file/891a05f03399fb48f40f3.png) ",
            " ✰ STICKER CHOR ✰[ㅤ](https://telegra.ph/file/542a1f433c263e4f3f984.png)",
            " ✰ SAAR DARD ✰ㅤ[ㅤ](https://telegra.ph/file/bfa114bbd4b2044cf5933.png)",
            " ✰ SWAD AAYA ✰ㅤ[ㅤ](https://telegra.ph/file/3830d44f9333e3c21b2cd.png)",
            " ✰ KAAM TAMMAM ✰ㅤ[ㅤ](https://telegra.ph/file/ececebb55e5f29be0afcf.png)",
            " ✰ JHALEBI KHAYI ✰ㅤ[ㅤ](https://telegra.ph/file/389a857af3bf833d3ccb2.png)"
]


repo = [
          
            " [ʀᴇᴘᴏ](https://github.com/black_legend) "
            " [ʀᴇᴘᴏ](https://github.com/black_legend) "
          
          
@run_async
def lol(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('DEKHNA AAB MAJA AAEGA 😂')
    for x in range(EDIT_TIMES):
        msg.edit_text(lol_ani[x%10],parse_mode='markdown')
        time.sleep(2)
    msg.edit_text('*MAJA AAYA KYA 😄*[ㅤ](https://telegra.ph/file/381dd2ea242e0bd292434.png)*AGAR HA THEN MAKE* [LEGEND USERBOT](t.me/teamishere)',parse_mode='markdown')
          
          
@run_async
def repo(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Showing Repo For @Black_Legend_Bot')
    for x in range(EDIT_TIMES):
        msg.edit_text(repo[x%2],parse_mode='markdown')
        time.sleep(2)
    msg.edit_text('[ʀᴇᴘᴏ](https://github.com/black_legend)\n\n[ᴏᴡɴᴇʀ](t.me/Alain_Champion)\n\n[ɢʀᴏᴜᴘ](t.me/black_legend_support)\n\n[ᴄʜᴀɴɴᴇʟ](t.me/blacklegend_bot)\n\n[ᴅᴇᴠ](t.me/infotechbro)\n\n[ᴜsᴇʀʙᴏᴛ](t.me/teamishere)',parse_mode='markdown')

          
          

__help__ = """
- /lol  
"""


LOL_HANDLER =DisableAbleCommandHandler("lol", lol)
REPO_HANDLER =DisableAbleCommandHandler("repo", repo)

dispatcher.add_handler(LOL_HANDLER)
dispatcher.add_handler(REPO_HANDLER)


__mod_name__ = "ANIMATION"
__command_list__ = ["lol", "repo"]
__handlers__ = [LOL_HANDLER, REPO_HANDLER]
