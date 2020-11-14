from django.core.management.base import BaseCommand
from phones.models import Phone
import requests
from bs4 import BeautifulSoup
import time

link_list = [
        'https://www.citilink.ru/catalog/mobile/cell_phones/1413646/',
        'https://www.citilink.ru/catalog/mobile/cell_phones/1427362/',
        'https://www.citilink.ru/catalog/mobile/cell_phones/1385250/'
    ]

phone_list = []


def phone_info():
    for link in link_list:
        while True:
            headers = requests.utils.default_headers()
            headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/69.0'})
            time.sleep(1)
            resp = requests.get(f'{link}', headers)
            time.sleep(1)
            print(resp)
            soup = BeautifulSoup(resp.content, "html.parser")
            item_list = []
            try:
                name = soup.find('div', {'class': "ProductCartFixedBlock__title"}).text
                phone = ((name.split(','))[0]).strip('\n ').split(' ')
                phone.pop()
                phone.pop(0)
                print(' '.join(phone))
                item_list.append(' '.join(phone))
                price = (soup.find('span', {'class': 'ProductCardForKits__price-block_current-price'}).text).strip('\n ')
                print(price)
                item_list.append(f'{price} руб.')
                properties = soup.find('div', {'id': 'content'})
                # property_name = properties.find_all('div', {'class': "Specifications__column Specifications__column_name"})
                property_value = properties.find_all('div', {'class': "Specifications__column Specifications__column_value"})
                # for k, v in zip(property_name, property_value):
                #     dict[(k.text).strip('\n ')] = (v.text).strip('\n ')
                for item in property_value:
                    item_list.append((item.text).strip('\n '))
                phone_list.append(item_list)
                break
            except AttributeError:
                continue
    return phone_list

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        phone_properties = phone_info()
        for property in phone_properties:
            phone_info_to_db = Phone.objects.create(name=property[0], price=property[1], os=property[2],
                                                    display=property[3], resolution=property[4], processor=property[5],
                                                    ram=property[6], built_in_memory=property[7])
            phone_info_to_db.save()
