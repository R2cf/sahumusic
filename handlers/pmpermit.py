import asyncio
from pyrogram import Client
from helpers.filters import command
from config import SUDO_USERS, BOT_NAME as bn, BOT_USERNAME as lel, PMPERMIT, OWNER_USERNAME
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                f"ʜᴇʏ {message.from_user.mention()},\nᴛʜɪs ɪs [{bn}](t.me/{lel}) ᴠɪᴊᴀʏ sᴀʜᴜ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴅᴏɴ'ᴛ ᴛʀʏ ᴛᴏ sᴘᴀᴍ ʜᴇʀᴇ ᴇʟsᴇ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ꜰᴜ*ᴋᴇᴅ ʙʏ [☠︎︎𝐯𝐢𝐣𝐚𝐲 𝐬𝐚𝐡𝐮☠︎︎](t.me/{OWNER_USERNAME}).\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥱 ʙᴏᴛ 🥱", url=f"https://t.me/{lel}"
                    ),
                    InlineKeyboardButton(
                        "💖 sᴜᴩᴩᴏʀᴛ 💖", url="https://t.me/ANKITSERVER"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💞 ᴏᴡɴᴇʀ​​ 💞", url=f"https://t.me/{OWNER_USERNAME}"
                    )]
            ]
        ),

    )
            return


@Client.on_message(filters.command(["pm", "pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("» ᴠɪᴊᴀʏ sᴀʜᴜ ᴘᴍ ᴘᴇʀᴍɪᴛ ᴇɴᴀʙʟᴇᴅ ʙᴀʙʏ.")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("» ᴘᴍ ᴘᴇʀᴍɪᴛ ᴅɪsᴀʙʟᴇᴅ ʙᴀʙʏ.")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("» ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ​ ʙᴀʙʏ.")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", ["!", ".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("» ᴄʜᴀʟ ᴀᴀʙ ᴍᴀssᴀɢᴇ ᴋᴀʀᴏ​.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", ["!", ".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("» ᴅɪsᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ​.")
        return
    message.continue_propagation()
