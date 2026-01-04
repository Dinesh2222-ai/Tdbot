# -----------------------------------------------------------
#  Advanced Config File
#  Developer: @VJ_Bots
# -----------------------------------------------------------

import os
import sys

def critical(msg):
    print(f"[CRITICAL] {msg}")
    sys.exit(1)

# -----------------------------------------------------------
# LOGIN SYSTEM
# -----------------------------------------------------------
LOGIN_SYSTEM = os.environ.get("LOGIN_SYSTEM", "True").strip().lower() == "true"

if not LOGIN_SYSTEM:
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    if not STRING_SESSION:
        critical("❌ LOGIN_SYSTEM=False but STRING_SESSION is empty!")
else:
    STRING_SESSION = None  # Will generate session automatically

# -----------------------------------------------------------
# TELEGRAM BOT + USER API
# -----------------------------------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    critical("❌ BOT_TOKEN missing!")

try:
    API_ID = int(os.environ.get("API_ID"))
except:
    critical("❌ API_ID must be integer!")

API_HASH = os.environ.get("API_HASH")
if not API_HASH:
    critical("❌ API_HASH missing!")

# -----------------------------------------------------------
# ADMIN / OWNER
# -----------------------------------------------------------
ADMINS = os.environ.get("ADMINS", "").replace(" ", "").split(",")

if len(ADMINS) == 1 and ADMINS[0].isdigit():
    ADMINS = [int(ADMINS[0])]
else:
    ADMINS = [int(x) for x in ADMINS if x.isdigit()]

if not ADMINS:
    critical("❌ No valid admin ID(s) found in ADMINS variable!")

# -----------------------------------------------------------
# CHANNEL WHERE CONTENT WILL BE SAVED
# -----------------------------------------------------------
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
if CHANNEL_ID:
    try:
        CHANNEL_ID = int(CHANNEL_ID)
    except:
        critical("❌ Invalid CHANNEL_ID format! Must be integer.")
else:
    CHANNEL_ID = None  # Upload to user instead

# -----------------------------------------------------------
# DATABASE
# -----------------------------------------------------------
DB_URI = os.environ.get("DB_URI")
DB_NAME = os.environ.get("DB_NAME", "tdanimehub")

if not DB_URI:
    critical("❌ DB_URI missing!")

# -----------------------------------------------------------
# FLOOD CONTROL / SECURITY SYSTEM
# -----------------------------------------------------------
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10"))
MAX_CONCURRENT_DOWNLOADS = int(os.environ.get("MAX_CONCURRENT_DOWNLOADS", "3"))
MAX_FILE_SIZE_MB = int(os.environ.get("MAX_FILE_SIZE_MB", "2048"))
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", "5"))

# -----------------------------------------------------------
# LOGGING / DEBUG SETTINGS
# -----------------------------------------------------------
DEBUG_MODE = os.environ.get("DEBUG_MODE", "False").lower() == "true"
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"

# -----------------------------------------------------------
# OPTIONAL REDIS SUPPORT
# -----------------------------------------------------------
REDIS_URL = os.environ.get("REDIS_URL", None)
USE_REDIS = True if REDIS_URL else False

print("🔧 Advanced Config Loaded Successfully!")