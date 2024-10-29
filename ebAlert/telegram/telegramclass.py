import requests

from ebAlert.core.config import settings
from ebAlert.ebayscrapping.ebayclass import EbayItem
from urllib.parse import urlencode


def send_message(message):
    ntfy_url = settings.NTFY_URL
    headers = {
            "Authorization": f"Bearer {settings.NTFY_TOKEN}"
        }
    response = requests.post(ntfy_url, data=message.encode("utf-8"), headers=headers)
    return response.status_code == 200 



class SendingClass:

    def send_message(self, message):
        ntfy_url = settings.NTFY_URL
        headers = {
            "Authorization": f"Bearer {settings.NTFY_TOKEN}"
        }
        response = requests.post(ntfy_url, data=message.encode("utf-8"), headers=headers)

        if response.status_code == 200:
            return True
        return False

    def send_formated_message(self, item: EbayItem):
        message = f"{item.title}\n\n{item.price} ({item.city})\n\n {item.description} \n\n {item.link}"
        self.send_message(message)


telegram = SendingClass()

