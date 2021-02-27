from telegram import ParseMode, Update, Bot, Chat, MessageEntity
from telegram.ext import CommandHandler, MessageHandler, BaseFilter, run_async

from tg_bot import dispatcher
from covid19_data import JHU

from requests import get
from tg_bot.modules.disable import DisableAbleCommandHandler

import json
from urllib.request import urlopen

SFW_STRINGS = (
    
    "🧼 WASH YOUR HANDS FREQUENTLY",
    "🚴‍ ♂️EXCERCISE AND PROPER SLEEP🛌 WILL BOLSTER THE IMMUNE SYSTEM",
    "🛀 MAINTAIN GOOD HYGIENE HABHITS AT ALL TIMES",
    "👬 AVOID CONTACT WITH OTHERS",
    "😷 WEAR A FACE MASK WHEN DEALING WITH INFECTED PATIENT'S",
    "🧻 USE TISSUES WHEN COUGHING OR BLOWING NOSE",
    "🍎 WASH AND PREPARE FOODS CAREFULLY",
    "STAY HOME STAY SAFE",
  )



@run_async
def covid(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*🦠 COVID-19 Stats 🦠:*\n\n"
        "➥ *Total Confirmed* \nㅤㅤ╚» `" + str(JHU.Total.confirmed) + "`\n"
        "➥ *Total Deaths* \nㅤㅤ╚» `" + str(JHU.Total.deaths) + "`\n"
        "➥ *Total Recovered* \nㅤㅤ╚» `" + str(JHU.Total.recovered) +"`\n"
        "➥ *Active Cases* \nㅤㅤ╚» `"+ str(JHU.India.cases) + "`\n\n"
        "➥ *Tips*\n☞ 😷 Wear A Mask.\n ☞ 🧻 Use Tissue When Sneezing Or Blowing Nose.\n☞ 🧼 Wash Your Hands Frequently.\n☞︎︎︎ 👬 Avoid Contact With Others.\n☞︎︎︎ 🍎 Wash Foods Before Eating It.\n☞︎︎︎ 🛀 Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  

  
__help__ = """
 
 ➥ /covid - Get World Wide Corona Status
 
"""

__mod_name__ = 'Corona'

COVID_HANDLER = CommandHandler("covid", covid, admin_ok=True)


dispatcher.add_handler(COVID_HANDLER)


