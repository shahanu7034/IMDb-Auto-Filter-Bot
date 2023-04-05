import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['1242353'])
API_HASH = environ['b3a18ad8cab67c73ee21881c5b76a7e1']
BOT_TOKEN = environ['5782966530:AAGLQn0NMWTifwLWHM85Z6eywjlOS62MQsM']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ[''].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['-1001477344273'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('391342978', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1001678913761')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("-1001873599227", "").split()]

# MongoDB information
DATABASE_URI = environ['mongodb+srv://Shahanaz786:Shahanaz786@shahanaz.b6wywgj.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['Shahanaz']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# start Pics
PICS = (environ.get('PICS', 'https://telegra.ph/A2-04-16')).split()

# Messages
default_start_msg = """
**Hᴇʟʟᴏ 👋   I'ᴍ ABU 😊  Exᴄʟᴜꜱɪᴠᴇʟʏ Mᴀᴅᴇ Tʜɪꜱ Bᴏᴛ Fᴏʀ @A2Movies_Group ..!! 💫**
.
"""
START_MSG = environ.get('Hᴇʟʟᴏ 👋   I'ᴍ Zack Night 😊  Exᴄʟᴜꜱɪᴠᴇʟʏ Mᴀᴅᴇ Tʜɪꜱ Bᴏᴛ Fᴏʀ @A2Movies_Group ..!! 💫', default_start_msg)

FILE_CAPTION = environ.get("{file_name} 

<b>JOIN :</b>  [A2MOVIES](https://t.me/A2movies_group)", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
CUSTOM_FILE_CAPTION = None if FILE_CAPTION.strip() == "" else FILE_CAPTION
API_KEY = None if OMDB_API_KEY.strip() == "" else OMDB_API_KEY
