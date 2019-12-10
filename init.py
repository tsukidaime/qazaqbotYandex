import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler, Updater
from telegram.ext.dispatcher import run_async
import logging
import translate as tsl
from uuid import uuid4
import os
TOKEN='954490538:AAE6NFtZ8ldWU9_tnGytbb6O03FgpoAl9kg'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
cur_users = []
bot = telegram.Bot(token=TOKEN)


def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


@run_async
def inline_aydary(update, context):
    query = update.inline_query.query
    tslText = tsl.Translate(query)
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Translate\n{}\n{}".format(query, tslText),
            input_message_content=InputTextMessageContent(tslText)
        )
    ]
    update.inline_query.answer(results, cache_time=6000)


updater = Updater(token=TOKEN, use_context=True)
PORT = int(os.environ.get('PORT', '8443'))
dp = updater.dispatcher
dp.add_handler(InlineQueryHandler(inline_aydary))
dp.add_error_handler(error_callback)
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://qazaqbot.herokuapp.com/" + TOKEN)
# updater.start_polling()
updater.idle()