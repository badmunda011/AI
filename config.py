import os
API_ID :int = int(os.environ.get("API_ID", 25742938))
API_HASH :str = os.environ.get("API_HASH", "b35b715fe8dc0a58e8048988286fc5b6")
BOT_TOKEN :str= os.environ.get("BOT_TOKEN", "7201253389:AAG4qdCWAFprgCafSK5fwLC0zQrfvRts0gA")
UPDATE_CHNL :str = os.environ.get("UPDATE_CHNL", "mr_sukkun")
SUPPORT_GRP :str = os.environ.get("SUPPORT_GRP", "the_support_chat")
START_IMG :str = os.environ.get(
    "START_IMG", "https://graph.org/file/d4412c7b411ca8da9e177.jpg"
)

MONGO_DB_URI :str = os.environ.get(
    "MONGO_DB_URI",
    "mongodb+srv://Badmunda_13:badmunda50@cluster0.9oyzqux.mongodb.net/?retryWrites=true&w=majority",
)
OWNER_ID :int= os.environ.get("OWNER_ID", 6728038801)

