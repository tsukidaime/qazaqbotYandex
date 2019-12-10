import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler, Updater
import logging
import translate as tsl
from latin import changetolatin
import os
TOKEN='518602096:AAEkYXE1WEf64FtgfLQydtq7DhGZGCWLfI0'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
cur_users = []
bot = telegram.Bot(token=TOKEN)

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def inline_aydary(bot, update):
    user = update.inline_query.from_user
    if user in cur_users:
        return
    else:
        query = update.inline_query.query
        if not query:
            return
        cur_users.append(user)
        results = [
            InlineQueryResultArticle(
                id=query.upper()+"Cyrillic",
                title='Cyrillic',
                input_message_content=InputTextMessageContent(tsl.Translate(query))
            ),
            InlineQueryResultArticle(
                id=query.upper()+"Latin",
                title='Latin',
                input_message_content=InputTextMessageContent(changetolatin(tsl.Translate(query)))
            )
        ]
        update.inline_query.answer(results, cache_time=6000)
        cur_users.remove(user)


updater = Updater(token=TOKEN)
PORT = int(os.environ.get('PORT', '8443'))
dp = updater.dispatcher
dp.add_handler(InlineQueryHandler(inline_aydary))
dp.add_error_handler(error)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://qazaqbot.herokuapp.com/" + TOKEN)
updater.idle()