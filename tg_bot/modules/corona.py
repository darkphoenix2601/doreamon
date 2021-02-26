import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "HOW CAN I PROTECT MYSELF FROM CORONAVIRUS?",
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
def corona(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /corona  😷 Make Yourself Safe From Corona Just Do /corona And Get Tips.
"""

__mod_name__ = "Avoid Corana"

CRNA_HANDLER = DisableAbleCommandHandler("corona", corona)

dispatcher.add_handler(CRNA_HANDLER)
