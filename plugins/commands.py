"""
Music Player V5 By Priyo
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Hᴇʏ Dᴇᴀʀ, [{}](tg://user?id={})\n\nI Cᴀɴ Pʟᴀʏ Yᴏᴜʀ Fᴀᴠᴏʀɪᴛᴇ Mᴜsɪᴄ Aɴʏᴛɪᴍᴇ.\n\nHɪᴛs /help Fᴏʀ Mᴏʀᴇ Iɴғᴏ...</b>"
HELP = """
**Mᴇᴍʙᴇʀ Cᴏᴍᴍᴀɴᴅs:**
⚡/play **[sᴏɴɢ ɴᴀᴍᴇ]/[ʏᴛ ʟɪɴᴋ]**: Rᴇᴘʟᴀʏ Tᴏ Aɴ Aᴜᴅɪᴏ Fɪʟᴇ.
⚡/dplay **[sᴏɴɢ ɴᴀᴍᴇ]:** Pʟᴀʏ Fʀᴏᴍ Dᴇᴇᴢᴇʀ .
⚡/player:  Cᴜʀʀᴇɴᴛ Sᴏɴɢ Sᴛᴀᴛᴜs.
⚡/upload: Dᴏᴡɴʟᴏᴀᴅ Cᴜʀʀᴇɴᴛ Sᴏɴɢ Wʜᴀᴛ Pʟᴀʏɪɴɢ.
⚡/help: Hᴇʟᴘ Cᴏᴍᴍᴀɴᴅ Fᴏʀ Nᴏᴏʙ.
⚡/playlist: Vɪᴇᴡ Pʟᴀʏʟɪsᴛ.

**Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅ:**
⚡/skip: Sᴋɪᴘ Cᴜʀʀᴇɴᴛ Sᴏɴɢ
⚡/cplay: Pʟᴀʏ Mᴜsɪᴄ Fᴏʀ Cʜᴀɴɴᴇʟ.
⚡/yplay: Pʟᴀʏ Mᴜsɪᴄ Fʀᴏᴍ YT Pʟᴀʏʟɪsᴛ.
⚡/join: Jᴏɪɴ Vᴏɪᴄᴇ Cʜᴀᴛ Nᴏᴏʙ.
⚡/leave: Kɪᴄᴋ Fʀᴏᴍ Vᴏɪᴄᴇ Cʜᴀᴛ.
⚡/shuffle: Rᴀɴᴅᴏᴍ Pʟᴀʏʟɪsᴛ.
⚡/vc: Cʜᴇᴄᴋ Usᴇʀʙᴏᴛ Sᴛᴀᴛᴜs.
⚡/stop: Sᴛᴏᴘ Mᴜsɪᴄ.
⚡/radio: Sᴛᴀʀᴛ Rᴀᴅɪᴏ.
⚡/stopradio: Sᴛᴏᴘ Rᴀᴅɪᴏ.
⚡/clearplaylist: Cʟᴇᴀʀ Pʟᴀʏʟɪsᴛ.
⚡/export: Exᴘᴏʀᴛ Cᴜʀʀᴇɴᴛ Pʟᴀʏʟɪsᴛ.
⚡/import: Iᴍᴘᴏʀᴛ Pʀᴇᴠɪᴏᴜs Pʟᴀʏʟɪsᴛ.
⚡/replay: Pʟᴀʏ Aɢᴀɪɴ.
⚡/clean: Rᴇᴍᴏᴠᴇ Uɴᴜsᴇᴅ Fɪʟᴇs.
⚡/pause: Pᴀᴜsᴇ Pʟᴀʏɪɴɢ.
⚡/resume: Rᴇsᴜᴍᴇ Pʟᴀʏɪɴɢ.
⚡/volume: Cʜᴀɴɢᴇ Mᴏᴏᴅ(0-200).
⚡/mute: Mᴜᴛᴇ VᴏɪᴄᴇCʜᴀᴛ.
⚡/unmute: Uɴᴍᴜᴛᴇ VᴏɪᴄᴇCʜᴀᴛ.
⚡/restart: Rᴇsᴛᴀʀᴛ Bᴏᴛ.
"""



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url='https://github.com/itspriyo/Premium_Music'),
    ],
    [
        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url='https://t.me/premiumappsaccountfree'),
        InlineKeyboardButton('Aᴅᴅᴀ Gʀᴏᴜᴘ', url='https://t.me/joinchat/v5mRLN2TTohlNzFl'),
    ],
    [
        InlineKeyboardButton('Hᴏᴡ Tᴏ Usᴇ', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
        InlineKeyboardButton("Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url='https://github.com/itspriyo/Premium_Music'),
    ],
    [
        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url='https://t.me/premiumappsaccountfree'),
        InlineKeyboardButton('Aᴅᴅᴀ Gʀᴏᴜᴘ', url='https://t.me/joinchat/v5mRLN2TTohlNzFl'),
    ],
    [
        InlineKeyboardButton('Hᴏᴡ Tᴏ Usᴇ', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{U}"]) & filters.user(Config.ADMINS))
async def restart(client, message):
    await message.reply_text("Rᴇsᴛᴀʀᴛɪɴɢ, Wᴀɪᴛ Dᴇᴀʀ...")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
    os.execl(sys.executable, sys.executable, *sys.argv)

