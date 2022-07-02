import requests
from auth_data import token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import translators as ts
from googletrans import Translator





bot = Bot(token = token)
dp = Dispatcher(bot)

@dp.message_handler()
async def start_script(message: types.Message):
    translator = Translator()
    lang = translator.detect(message.text)
    if lang.lang == 'ru':
        await start_transcript(message)
    else:
        translate_to_ru = ts.google(message.text , to_language = 'ru')
        await message.reply(translate_to_ru)

    
async def start_transcript(message):

    translate_to_de = ts.google(message.text , to_language = 'de')
    url = "https://www.artlebedev.ru/tools/transcriptor/ajax.html"

    data = {
        "lang":"deu",
        "text": translate_to_de
    }
    
    
    s = requests.Session()

    response = s.post(url, data=data)
    responceDict = response.json()
    restText = responceDict['text']
    await message.reply(f'''
    {message.text}
    -{restText}
    -{translate_to_de}
    ''')

if __name__ == '__main__':
    executor.start_polling(dp)

