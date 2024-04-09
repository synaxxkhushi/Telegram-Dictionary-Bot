import os
import dictionary
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Dictionary Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """𝐇ᴇʟʟᴏ {},

⊚ ɪ ᴀᴍ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴡᴏʀᴅs 
    ᴅɪᴄᴛɪᴏɴᴀʀʏ ʙᴏᴛ.
⊚ ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛʜᴇ ᴍᴇᴀɴɪɴɢ ᴏғ 
    ᴀɴʏ ᴡᴏʀᴅ."""

HELP_TEXT = """--**𝐌ᴏʀᴇ 𝐇ᴇʟᴘ**--

⊚ ᴊᴜsᴛ sᴇɴᴅ ᴀ ᴡᴏʀᴅ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴇᴀɴɪɴɢ 
    ᴏғ ɪᴛ.

⊚ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛʜᴇ ᴍᴇᴀɴɪɴɢ ᴏғ ᴛʜᴇ 
    ᴡᴏʀᴅ.

⊚ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴍᴇ ɪɴ ɢʀᴏᴜᴘs ᴜsɪɴɢ
    /dict ᴄᴏᴍᴍᴀɴᴅ
    ᴇɢ:- /dict ʜᴇʟʟᴏ

⊚ ᴏʀ , sᴇɴᴅ ᴀ ᴡᴏʀᴅ ᴀɴᴅ ʀᴇᴘʟʏ/dict

⊚ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛʜᴇ ᴍᴇᴀɴɪɴɢ ᴏғ ᴛʜᴇ
    ᴡᴏʀᴅ.


⊚ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @synaxnetwork 🇮🇳❤️
"""

ABOUT_TEXT = """--**𝐀ʙᴏᴜᴛ 𝐌ᴇ**--

⊚ 𝗕𝗼𝘁 : ᴅɪᴄᴛɪᴏɴᴀʀʏ ʙᴏᴛ 🇮🇳
⊚ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 :
  • [ ɢɪᴛʜᴜʙ ](https://github.com/SynaxBots)  • [ ᴛᴇʟᴇɢʀᴀᴍ ](https://telegram.me/sanatanisynax)
⊚ 𝗦𝗼𝘂𝗿𝗰𝗲 : [ ᴄʟɪᴄᴋ ᴋʀ ᴍᴄ 🐰](https://t.me/synaxnetwork)
⊚ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : [ ᴘʏᴛʜᴏɴ3 ](https://python.org)
⊚ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆 : [ ᴘʏʀᴏɢʀᴀᴍ ](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🇮🇳 ᴜᴘᴅᴀᴛᴇ ʜᴇʀᴇ 🇮🇳', url='https://telegram.me/synaxnetwork')
        ],
        [
            InlineKeyboardButton('ʜᴇʟᴘ 🌹', callback_data='help'),
            InlineKeyboardButton('☣️ ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('🍃 ᴄʟᴏsᴇ', callback_data='close')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('ʜᴏᴍᴇ 🧸', callback_data='home'),
            InlineKeyboardButton('☣️ ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('🍃 ᴄʟᴏsᴇ', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('ʜᴏᴍᴇ 🧸', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ 🌹', callback_data='help'),
            InlineKeyboardButton('🍃 ᴄʟᴏsᴇ', callback_data='close')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_data(bot, message):
    
    if message.data == "home":
        await message.message.edit_text(
            text=START_TEXT.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    
    elif message.data == "help":
        await message.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    
    elif message.data == "about":
        await message.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    
    else:
        await message.message.delete()
    

@Bot.on_message(filters.private & filters.command(["start"]))
async def sed_start_message(bot, message):
    
    await message.reply_text(
        text=START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=START_BUTTONS
    )


@Bot.on_message(filters.private & filters.command(["help"]))
async def send_help(bot, message):
    
    await message.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=HELP_BUTTONS
    )


@Bot.on_message(filters.private & filters.command(["about"]))
async def send_about(bot, message):
    
    await message.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=ABOUT_BUTTONS
    )


@Bot.on_message(filters.command(["dict", "dictionary", "word"]))
async def cmd_filter_dictionary(_, message):
    m = await message.reply_text(
        text="Searching...",
        quote=True
    )
    if (len(message.text.split(" ")) == 1):
        if (message.reply_to_message) and (message.reply_to_message.text):
            word = message.reply_to_message.text
        else:
            await m.edit_text(
                text="Reply to a text message containing the word.",
                disable_web_page_preview=True
            )
            return
    else:
        word = message.text.split(" ", 1)[1]
    details = dictionary.dictionary(word)
    await m.edit_text(
        text=details,
        disable_web_page_preview=True
    )


@Bot.on_message(filters.private & filters.text)
async def send_dictionary_details(_, message):
    m = await message.reply_text(
        text="Searching...",
        quote=True
    )
    word = message.text
    details = dictionary.dictionary(word)
    await m.edit_text(
        text=details,
        disable_web_page_preview=True
    )


Bot.run()
