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



lol_ani = [ 
          
            "  *WAAH* ㅤㅤ[ㅤ](https://telegra.ph/file/a19b0bf4760fca85bd961.png) ",
            "  *LOL* ㅤㅤㅤ[ㅤ](https://telegra.ph/file/ed23819c84bab66e7d92f.png) ",
            "  *ELECTRIC BILL KON BHAREGA* ㅤ[ㅤ](https://telegra.ph/file/53c85b5b354212496746f.png) ",
            "  *JHINGA LALA*   [ㅤ](https://telegra.ph/file/1379a8c9ea40eaa463fd8.png) ",
            "  *NINJA TECHNIQUE* [ㅤ](https://telegra.ph/file/891a05f03399fb48f40f3.png) ",
            "  *STICKER CHOR* [ㅤ](https://telegra.ph/file/542a1f433c263e4f3f984.png)",
            "  *SAAR DARD* ㅤ[ㅤ](https://telegra.ph/file/bfa114bbd4b2044cf5933.png)",
            "  *SWAD AAYA* ㅤ[ㅤ](https://telegra.ph/file/3830d44f9333e3c21b2cd.png)",
            "  *KAAM TAMMAM* ㅤ[ㅤ](https://telegra.ph/file/ececebb55e5f29be0afcf.png)",
            "  *JHALEBI KHAYI* ㅤ[ㅤ](https://telegra.ph/file/389a857af3bf833d3ccb2.png)"
]



          
@run_async
def lol(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('DEKHNA AAB MAJA AAEGA 😂')
    for x in range(EDIT_TIMES):
        msg.edit_text(lol_ani[x%10],parse_mode='markdown')
        time.sleep(2)
    msg.edit_text('*MAJA AAYA KYA 😄*[ㅤ](https://telegra.ph/file/381dd2ea242e0bd292434.png)*AGAR HA THEN ADD ME TO YOUR GROUP*👻',parse_mode='markdown')
          
          


          
          

__help__ = """
➥ /lol  
"""


LOL_HANDLER =DisableAbleCommandHandler("lol", lol)


dispatcher.add_handler(LOL_HANDLER)



__mod_name__ = "Animation"
__command_list__ = ["lol"]
__handlers__ = [LOL_HANDLER]
