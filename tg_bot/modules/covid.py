from telegram import ParseMode, Update, Bot, Chat, MessageEntity, Filters
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
        "➥ *Tips*\n☞ 😷 Wear A Mask.\n
        ☞ 🧻 Use Tissue When Sneezing Or Blowing Nose.\n
        ☞ 🧼 Wash Your Hands Frequently.\n
        ☞︎︎︎ 👬 Avoid Contact With Others.\n
        ☞︎︎︎ 🍎 Wash Foods After buying it.", parse_mode=ParseMode.MARKDOWN)
  
@run_async
def corona(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))
  
  
__help__ = """
 
 - /covid - Get World Wide Corona Status
 - /corona - Tips For Preventing You From Corona
"""

__mod_name__ = 'Covid-19'

COVID_HANDLER = CommandHandler("covid", covid, admin_ok=True)
CRNA_HANDLER = DisableAbleCommandHandler("corona", corona)

dispatcher.add_handler(COVID_HANDLER)
dispatcher.add_handler(CRNA_HANDLER)


