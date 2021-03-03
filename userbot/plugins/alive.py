"""Check if userbot alive."""
#IMG CREDITS: @CallPrime
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/30f297984523fccb8ce8c.jpg"
pm_caption = "`PrimeUserbot :` **Online**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.20.0**\n`Python:` **3.9.2**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**PrimeUserbot OS** : `9.0`\n"
pm_caption += "**Current Sat** : `PrimeUserbotSat-9.0`\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Database** : `Online`\n\n"
pm_caption += "**License** : [MIT Licence](https://t.me/CallPrime)\n"
pm_caption += "Copyright : By [Prime@Github](t.me/callprime)\n"
pm_caption += " [Deploy](t.me/callprime)"

@borg.on(admin_cmd(pattern=r"alive"))
async def PrimeUserbot(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
