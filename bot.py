from telegram import Update
   from telegram.ext import Updater, CommandHandler, CallbackContext
   import requests

   # Вставьте свой токен
   TOKEN = 'YOUR_BOT_TOKEN'

   def start(update: Update, context: CallbackContext) -> None:
       update.message.reply_text('Привет! Я бот, который взаимодействует с вашим сайтом.')

   def get_data_from_site(update: Update, context: CallbackContext) -> None:
       # Пример запроса к вашему сайту
       response = requests.get('https://yourwebsite.com/api/data')
       data = response.json()  # Предполагаем, что сайт возвращает JSON

       # Отправка данных пользователю
       update.message.reply_text(str(data))

   def main() -> None:
       updater = Updater(TOKEN)
       updater.dispatcher.add_handler(CommandHandler("start", start))
       updater.dispatcher.add_handler(CommandHandler("getdata", get_data_from_site))

       updater.start_polling()
       updater.idle()

   if __name__ == '__main__':
       main()