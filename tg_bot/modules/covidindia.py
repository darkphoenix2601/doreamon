from telegram import ParseMode, Update, Bot, Chat, MessageEntity
from telegram.ext import CommandHandler, MessageHandler, BaseFilter, run_async

from tg_bot import dispatcher
from covid19_data import JHU

from requests import get
from tg_bot.modules.disable import DisableAbleCommandHandler

import json
from urllib.request import urlopen

@run_async
def covidi(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*🦠 COVID-19 Stats 🦠:*\n\n"
        "➥ *Total Confirmed* \nㅤㅤ╚» `" + str(JHU.Total.confirmed) + "`\n"
        "➥ *Total Deaths* \nㅤㅤ╚» `" + str(JHU.Total.deaths) + "`\n"
        "➥ *Total Recovered* \nㅤㅤ╚» `" + str(JHU.Total.recovered) +"`\n"
        "➥ *Active Cases* \nㅤㅤ╚» `"+ str(JHU.India.cases) + "`\n\n"
        "➥ *Tips*\n☞ 😷 Wear A Mask.\n ☞ 🧻 Use Tissue When Sneezing Or Blowing Nose.\n☞ 🧼 Wash Your Hands Frequently.\n☞︎︎︎ 👬 Avoid Contact With Others.\n☞︎︎︎ 🍎 Wash Foods Before Eating It.\n☞︎︎︎ 🛀 Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  

  
__help__ = """
 
 ➥ /covid india - Get Corona Status Of India
 
"""

__mod_name__ = 'Covid Tracker'

COVIDI_HANDLER = CommandHandler("covid india", covidi, admin_ok=True)


dispatcher.add_handler(COVIDI_HANDLER)


