import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = settings.tg_token
    chat_id = settings.tg_chat
    text = settings.tg_message
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'  # то что передаем в пути до вопросительного знака

    if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):  # ищем скобки и берем текст по срезу
        part_1 = text[:text.find('{')]  # Заявка с сайта:\nИмя:
        part_2 = text[text.find('}') + 1:text.rfind('{')]  # \nТелефон:
        text_slice = part_1 + tg_name + part_2 + tg_phone
    else:
        text_slice = text

    requests.post(method, data={  # с какими дополнительными данными  мы хотим отправить
        'chat_id': chat_id,
        'text': text_slice
    })


def send_telegram2(tg_name, tg_phone, tg_car_name, tg_color, tg_year):
    settings = TeleSettings.objects.get(pk=2)  # из нашей модели хотим получить данные по id1
    token = settings.tg_token
    chat_id = settings.tg_chat
    text = settings.tg_message
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'  # то что передаем в пути до вопросительного знака

    if text.find('{') and text.find('(') and text.find('[') and text.find('<') and text.find('}') and text.find(')') and text.find(']') and text.find('>'):   # ищем скобки и берем текст по срезу
        part_1 = text[:text.find('{')]                    # Заказ автомобиля: \n Имя:
        part_2 = text[text.find('}') + 1:text.find('(')]  # Телефон:
        part_3 = text[text.find(')') + 1:text.find('[')]  # Модель:
        part_4 = text[text.find(']') + 1:text.find('<')]  # Цвет:
        part_5 = text[text.find('>') + 1:text.rfind('{')]  # Год выпуска:
        text_slice = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_car_name + part_4 + tg_color + part_5 + tg_year
        # print('???', text_slice)
    else:
        text_slice = text
    requests.post(method, data={  # дополнительные данные с которыми мы хотим отправить
        'chat_id': chat_id,
        'text': text_slice
    })
