from attr import attrs
from telethon import TelegramClient, events, sync
import time
from telethon.tl.types import RecentMeUrlUnknown
from termcolor import colored
import colorama

api_id = "YOUR ID"  # Ваш API ID
api_hash = 'YOUR HASH' # Ваш API HASH

client = TelegramClient('session_name', api_id, api_hash)
client.start()

print()

colorama.init() # cmd текст

print(colored("''Влад'' for vlad123", color='blue'))

# Сохраненные контакты
def reciever(nickname = input('Введите nickname(Telegram) кого позвать: ')): 
        if nickname == "Влад":                                                  
            return 'vlad123' 
        else:
            return nickname

reciever = reciever()

# Предложение
client.send_message(f'{reciever}', '🔥 **Будете чай?** __(Да/Нет)__')


time_waiting = 60 # in seconds

while time_waiting:
    for message in client.iter_messages(f'{reciever}',from_user = f'{reciever}',limit = 1):
        message = ('{}'.format(message.message))
        if "Да" in message:
            client.send_message(f'{reciever}', '😇 Отлично! 😇')
            client.send_message(f'{reciever}', file = '***') # *** - URL to your image
            time_waiting = 2
        elif "Нет" in message:
            client.send_message(f'{reciever}', '😢 Ничего,в следующий раз! 😢')
            client.send_message(f'{reciever}', file = '***') # *** - URL to your image
            time_waiting = 2
        else:
            client.send_message(f'{reciever}','**Напиши -** Да/Нет ')
            continue
    else:
        print(colored('Waiting...', attrs = ['underline']),end ='  - ')
        time.sleep(1)
        time_waiting -= 1
        print(colored(f"{time_waiting} seconds left",color = 'green',attrs = ['bold']),end ='\r')
       

