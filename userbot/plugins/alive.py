"""Check if userbot alive."""
#IMG CREDITS: @CallPrime
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/30f297984523fccb8ce8c.jpg"
pm_caption = "`PrimeUserbot IS:` **Online**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.15.0**\n`Python:` **3.9. 1**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**PrimeUserbot OS** : `8.0`\n"
pm_caption += "**Current Sat** : `PrimeUserbotSat-8.00`\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Database** : `Online`\n\n"
pm_caption += "**License** : [MIT Licence](https://github.com/primeuserbot/PrimeUserbot/blob/main/LICENSE)\n"]
pm_caption += "Copyright : By [PrimeUserbot@Github](GitHub.com/PrimeUserbot\n"
pm_caption += " [Deploy PrimeUserbot](https://github.com/primeuserbot/PrimeUserbot)"

@borg.on(admin_cmd(pattern=r"alive"))
async def PrimeUserbot(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
