from telegram import ParseMode, Update, Bot, Chat
from telegram.ext import CommandHandler, MessageHandler, BaseFilter, run_async

from tg_bot import dispatcher

from covid19_data import JHU

from requests import get

import json
from urllib.request import urlopen



@run_async
def covid(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*🦠 COVID-19 Stats 🦠:*\n\n"
        "➥ *Total Confirmed* \nㅤㅤ╚» `" + str(JHU.Total.confirmed) + "`\n"
        "➥ *Total Deaths* \nㅤㅤ╚» `" + str(JHU.Total.deaths) + "`\n"
        "➥ *Total Recovered* \nㅤㅤ╚» `" + str(JHU.Total.recovered) +"`\n"
        "➥ *Active Cases* \nㅤㅤ╚» `"+ str(JHU.India.cases) + "`\n\n"
        "➥ *Tips*\n☞ 😷 Wear A Mask.\n☞ 🧻 Use Tissue When Sneezing Or Blowing Nose.\n☞ 🧼 Wash Your Hands Frequently.\n☞︎︎︎ 👬 Avoid Contact With Others.\n☞︎︎︎ 🍎 Wash Foods After buying it.", parse_mode=ParseMode.MARKDOWN)
__help__ = """
 
 - /covid get worldwide corona status
"""

__mod_name__ = 'Covid-19'

COVID_HANDLER = CommandHandler("covid", covid, admin_ok=True)
dispatcher.add_handler(COVID_HANDLER)


