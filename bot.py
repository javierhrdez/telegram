import telegram
import io
import time
import picamera

TELEGRAM_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TELEGRAM_CHAT_ID = 12345

bot = telegram.Bot(token=TELEGRAM_TOKEN)
#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets


bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="Prueba1\nPrueba2")
emoji = u'\U0001f44d'
bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=emoji)
bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='<b>Negrita</b> <i>italic</i> <a href="http://google.com">link</a>.', parse_mode=telegram.ParseMode.HTML)

#time.sleep(5)

# Create an in-memory stream
my_stream = io.BytesIO()
my_stream.name = 'image.jpeg'
with picamera.PiCamera() as camera:
    camera.start_preview()
    # Camera warm-up time
    time.sleep(5)
    camera.capture(my_stream, 'jpeg')

my_stream.seek(0)


bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=my_stream)

