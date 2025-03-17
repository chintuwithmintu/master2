import os

class Config(object):
    BOT_TOKEN = os.environ.get("7483233103:AAEh_3Ah_eml3pbBOZk1YXqJlTM7ARbU5Kw")
    API_ID = int(os.environ.get("29940750"))
    API_HASH = os.environ.get("33412ad3b366ca991309d1bcbb472c32")
    AUTH_USER = os.environ.get('AUTH_USERS', '7618270428').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " OREO 𝘽𝙊𝙏𝙎"
