import requests
import config
from lxml import etree
from winotify import Notification, audio


def wie_ist_der_preis():
    response_url = requests.get(url=config.URL)

    if response_url.status_code == 200:
        content_tree = response_url.text


    tree = etree.HTML(content_tree)

    my_price = tree.xpath(config.MY_PRICE)[0][2].text
    The_price = my_price.split()[0].replace(",",".")

    if float(The_price) < 60.00:
        toast = Notification(app_id="Gold Now!",
                            title="The Gold Price",
                            msg=f"The Price now is {The_price} EUR",
                            duration="long",
                            icon=r"D:\PYthon\Notification_win\gold-96.png")
        toast.show()

if __name__ == "__main__":
    wie_ist_der_preis()