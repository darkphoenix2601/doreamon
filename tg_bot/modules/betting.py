import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

import tg_bot.modules.fun_strings as fun_strings
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user


@run_async
def bet1(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(betting_strings.BET))

@run_async
def bet2(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(betting_strings.BET))

@run_async
def bet3(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(betting_strings.BET))

@run_async
def bet4(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(betting_strings.BET))
    
@run_async
def bet5(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(betting_strings.BET))
    
@run_async
def bet(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(betting_strings.BETT))
    
    
    __help__ = """
 - /bet(x) --- INSTEAD OF x TYPE ANY NUMBER BETWEEN 1 AND 5\n IF YOU WANT TO BET MORE JOIN @bettinggamerobotchat

    
    BET1_HANDLER = DisableAbleCommandHandler("bet1", bet1)
    BET2_HANDLER = DisableAbleCommandHandler("bet2", bet2)
    BET3_HANDLER = DisableAbleCommandHandler("bet3", bet3)
    BET4_HANDLER = DisableAbleCommandHandler("bet4", bet4)
    BET5_HANDLER = DisableAbleCommandHandler("bet5", bet5)
    
    BET_HANDLER = DisableAbleCommandHandler("bet", bet)
    
    
    dispatcher.add_handler(BET1_HANDLER)
    
    dispatcher.add_handler(BET2_HANDLER)
    
    dispatcher.add_handler(BET3_HANDLER)
    
    dispatcher.add_handler(BET4_HANDLER)
    
    dispatcher.add_handler(BET5_HANDLER)
    
    dispatcher.add_handler(BET_HANDLER)
    
    
   __mod_name__ = "BETTING"
   __command_list__ = ["bet1", "bet2", "bet3", "bet4", "bet5", "bet",
   __handlers__ = ["BET1_HANDLER", "BET2_HANDLER", "BET3_HANDLER", "BET4_HANDLER", "BET5_HANDLER", "BET_HANDLER"]
