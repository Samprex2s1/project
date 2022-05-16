import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import rutermextract
from rutermextract import TermExtractor

# --
from commander.commander import Commander
from vk_bot import VkBot
from vk_bot import VKan
# --


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})



# API-ключ созданный ранее
token = "a24bc935e68c79744e42287174b846af653705c7fd3e966a41eba193c7fe0e5dfd91964891e0635b57daa"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

commander = Commander()
print("Server started")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print(f'New message from {event.user_id}', end='')

            bot = VkBot(event.user_id)
            vkanb = VKan(event.user_id)

            if event.text[0] == "/":
                write_msg(event.user_id, commander.do(event.text[1::]))
            elif event.text == 'анализ':
                        write_msg(event.user_id, vkanb.analiz(event.text))
            elif event.text != 'анализ':
                write_msg(event.user_id, vkanb.analiz(event.text))



            else:
                write_msg(event.user_id, bot.new_message(event.text))


            print('Text: ', event.text)
            print("-------------------")



