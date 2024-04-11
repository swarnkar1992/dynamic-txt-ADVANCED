import os

API_ID = API_ID = 24416885

API_HASH = os.environ.get("API_HASH", "7295275efa29826d8a69024439bac981")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6658002692:AAF5Tup-eQbfn9sJ9VIQmFch9xOr1ds7uzA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5651951148))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5651951148").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


