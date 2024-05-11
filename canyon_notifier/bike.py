import logging

import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


class Bike:
    def __init__(self, name, link, size="L"):
        self.name = name
        self.link = link
        self.size = size
        self.avail = False
        logger.info(f'{name} is created')

    def update(self):
        new_avail = self.parse_url()
        changed = self.avail != new_avail
        self.avail = new_avail
        logger.info(
            f'{self.name} status is {("NOT changed","changed")[changed]}')
        return changed

    def parse_url(self):
        req = requests.get(self.link)
        soup = BeautifulSoup(req.text, "html.parser")

        selector = f".productConfiguration__optionListItem .productConfiguration__selectVariant[data-product-size='{self.size}']"

        desired_element = soup.select_one(selector)
        if desired_element:
            inner_html = desired_element.decode_contents()
            logger.info(f'{inner_html}')

            is_bike_available_to_buy = 'productConfiguration__selectVariant--purchasable' in desired_element.get('class', [])
            if is_bike_available_to_buy:
                print(f'{self.name} is available in size {self.size}')
                return True
            logger.info(f'{self.name} is NOT available in size {self.size}')
        else:
            inner_html = 'Element not found'
            logger.error('Bike size not found on the page')
        return False
