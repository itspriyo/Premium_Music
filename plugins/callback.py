"""
Music Player V5 By Priyo
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import MessageNotModified
from pyrogram import Client, emoji
from utils import mp, playlist
from config import Config

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


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.from_user.id not in Config.ADMINS and query.data != "help":
        await query.answer(
            "Wʜʏ Bʀᴜʜ?, Nɪᴊᴇ Eᴋᴛᴀ Bᴏᴛ Bᴀɴɪʏᴇ Tᴀʀᴘᴏʀ Sᴋɪᴘ Kᴏʀᴇɴ 🙂",
            show_alert=True
            )
        return
    else:
        await query.answer()
    if query.data == "replay":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"{emoji.NO_ENTRY} Empty Playlist"
        else:
            pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n   🎵**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(
                f"{pl}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="pause"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data == "pause":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n   🎵**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="resume"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    
    elif query.data == "resume":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n   🎵**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄", callback_data="replay"),
                            InlineKeyboardButton("⏯", callback_data="pause"),
                            InlineKeyboardButton("⏩", callback_data="skip")
                            
                        ],
                    ]
                )
            )

    elif query.data=="skip":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n" + "\n".join([
                f"**{i}**. **{x[1]}**\n   🎵**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Skipped\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄", callback_data="replay"),
                        InlineKeyboardButton("⏯", callback_data="pause"),
                        InlineKeyboardButton("⏩", callback_data="skip")
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url='https://github.com/PriyoKhan777/Premium_Music'),
            ],
            [
               InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url='https://t.me/premiumappsaccountfree'),
               InlineKeyboardButton('Aᴅᴅᴀ Gʀᴏᴜᴘ', url='https://t.me/unknownfriends1'),
            ],
            [
               InlineKeyboardButton('', url='https://github.com/itspriyo'),
        
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            HELP,
            reply_markup=reply_markup

        )

