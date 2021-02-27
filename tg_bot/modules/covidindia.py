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
      "*🦠 COVID-19 Stats In India 🦠:*\n\n"
        "➥ *Total Confirmed* \nㅤㅤ╚» `" + str(JHU.India.confirmed) + "`\n"
        "➥ *Total Deaths* \nㅤㅤ╚» `" + str(JHU.India.deaths) + "`\n"
        "➥ *Total Recovered* \nㅤㅤ╚» `" + str(JHU.India.recovered) +"`\n"
        "➥ *Active Cases* \nㅤㅤ╚» `"+ str(JHU.India.cases) + "`\n\n"
        "➥ *Tips*\n☞ 😷 Wear A Mask.\n ☞ 🧻 Use Tissue When Sneezing Or Blowing Nose.\n☞ 🧼 Wash Your Hands Frequently.\n☞︎︎︎ 👬 Avoid Contact With Others.\n☞︎︎︎ 🍎 Wash Foods Before Eating It.\n☞︎︎︎ 🛀 Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  
@run_async
def covidc(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*🦠 COVID-19 Stats In China 🦠:*\n\n"
        "➥ *Total Confirmed* \nㅤㅤ╚» `" + str(JHU.china.confirmed) + "`\n"
        "➥ *Total Deaths* \nㅤㅤ╚» `" + str(JHU.China.deaths) + "`\n"
        "➥ *Total Recovered* \nㅤㅤ╚» `" + str(JHU.China.recovered) +"`\n"
        "➥ *Active Cases* \nㅤㅤ╚» `"+ str(JHU.China.cases) + "`\n\n"
        "➥ *Tips*\n☞ 😷 Wear A Mask.\n ☞ 🧻 Use Tissue When Sneezing Or Blowing Nose.\n☞ 🧼 Wash Your Hands Frequently.\n☞︎︎︎ 👬 Avoid Contact With Others.\n☞︎︎︎ 🍎 Wash Foods Before Eating It.\n☞︎︎︎ 🛀 Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  
  

  
__help__ = """
 
 ➥ /cov india - Get Corona Status Of India
 ➥ /cov china - Get Corona Status Of China
 
"""

__mod_name__ = 'Covid Tracker'

COVIDI_HANDLER = CommandHandler("cov india", covidi, admin_ok=True)
COVIDC_HANDLER = CommandHandler("cov china", covidc, admin_ok=True)


dispatcher.add_handler(COVIDI_HANDLER)
dispatcher.add_handler(COVIDC_HANDLER)


