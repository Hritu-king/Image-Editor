# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6130457410:AAG8jDlWwyFQv1-u8XYnpDhtXaliPo3YrEY")

    APP_ID = int(os.environ.get("APP_ID", 29616312))

    API_HASH = os.environ.get("API_HASH", "dd1a05ab4c47a5a037cc067cf4bded27")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "sFvSnp6KmgGi7pWDNp4sfn5P")
