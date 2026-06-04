
import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#BeingMarsa on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8128218557,8168286524")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002807868892,-1002882691726")) #Your db channel Id
OWNER = os.environ.get("OWNER", "deluluxd09") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7812855403")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/MarsaAdminContactBot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/241d576b065d6d814edc0-c613ebf4eab7a157d8.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/241d576b065d6d814edc0-c613ebf4eab7a157d8.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>This is a File Store Bot working for @MarsaNetwork\n\n❏ User Commands\n├/start : Starts the Bot\n├/about : Know about Marsa Network\n└/help : Get help related to Bot\n\n Working For <a href=https://t.me/MarsaNetwork>ᴍᴀʀsᴀ ɴᴇᴛᴡᴏʀᴋ</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>♕ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/MarsaAdminContactBot>ᴍᴀʀsᴀ ʙᴏɪ...</a>\n⌬ ᴏᴡɴᴇʀ ᴏғ : <a href=https://t.me/MarsaNetwork>ᴍᴀʀsᴀ ɴᴇᴛᴡᴏʀᴋ</a>\n⌬ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Anime_Marsa>ᴀɴɪᴍᴇ ᴍᴀʀsᴀ</a>\n⌬ sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Series_Marsa>sᴇʀɪᴇs ᴍᴀʀsᴀ</a>\n⌬ ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Movie_Marsa>ᴍᴏᴠɪᴇ ᴍᴀʀsᴀ</a>\n♕ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/MarsaAdminContactBot>ᴍᴀʀsᴀ ʙᴏɪ...</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\n<blockquote>I'm a File Store Bot working for <a href=https://t.me/MarsaNetwork>Marsa Network</a></blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Sorry! {first}\n\n<b>You have to join our channels to get your requested files. Join the channel and then try again.</b>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "You aren't my owner😕!!"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
