"""
from os import getenv


API_ID = int(getenv("API_ID", "26003553"))
API_HASH = getenv("API_HASH", "c1f27c622acecf9bf6e71d0d295e75f9")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "26003553"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "c1f27c622acecf9bf6e71d0d295e75f9")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", ",").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", ""))

