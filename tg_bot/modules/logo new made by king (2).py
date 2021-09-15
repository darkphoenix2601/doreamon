from tg_bot.events import register
from tg_bot import OWNER_ID
from tg_bot import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random, re
import glob
import time
from telethon.tl.types import InputMessagesFilterPhotos


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
"https://telegra.ph/file/96e801400487d0a120715.jpg", 
                         "https://telegra.ph/file/6ae8e799f2acc837e27eb.jpg",
                         "https://telegra.ph/file/265ff1cebbb7042bfb5a7.jpg",
                         "https://telegra.ph/file/4c8c9cd0751eab99600c9.jpg", 
                         "https://telegra.ph/file/1c6a5cd6d82f92c646c0f.jpg", 
                         "https://telegra.ph/file/2c1056c91c8f37fea838a.jpg",
                         "https://telegra.ph/file/f140c121d03dfcaf4e951.jpg", 
                         "https://telegra.ph/file/39f7b5d1d7a3487f6ba69.jpg"
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./MashaRoBot/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype(".//resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "LogoByLovely

.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="💕 Made By @dore_amon_bot Support @phoenix_music_suport")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @phoenix_music_suport, {e}')



   
@register(pattern="^/wlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./MashaRoBot/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./MashaRoBot/resources/Maghrib.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "LogoByLovely.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @dore_amon_bot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @dore_amon_bot, {e}')

file_help = os.path.basename(file)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


help = """
 ❍ /logo text :  Create your logo with your name
 ❍ /wlogo text :  Create your logo with your name
"""
mod_name = "Lᴏɢᴏ😍"