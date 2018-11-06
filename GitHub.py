from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    chat_id = update.message.from_user.id
    custom_keyboard = [['Начать', 'Помощь']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup)
    update.message.reply_text('Добрый день.Вас приветствует GitLab бот\n'
                              'C помощью него вы облегчите работу на GitLab\n')


def help(bot, update):
    update.message.reply_text('echoBot-взять эхо бота\n'
                              'echoBot2-другой шаблон эхо бота\n'
                              'conversationbot-взять бота опросника\n'
                              'conversationbot2-взять другой шаблон бота опросника\n'
                              'inlinebot-взять инлайн бота\n'
                              'passportbot-взять паспорт бота\n'
                              'persistentconversationbot-взять более продвинутого бота опросника\n'
                              'timerbot-часовой бот \n')


def poish_reposiroriya(bot, update):
    pass


def News_bot(bot, update):
    pass

def echobot2(bot, update):
    update.message.reply_text("Вероятно, это база для большинства ботов,"
                              "созданных с помощью python-telegram-bot. "
                              "Он просто отвечает на каждое текстовое сообщение сообщением, содержащим тот же текст")
    update.message.reply_text("Ссылка на скачивание:")


def timerbot(bot, update):
    update.message.reply_text("Этот бот использует класс JobQueue для отправки сообщений со временем."
                              "Пользователь устанавливает таймер с помощью команды / set с определенным временем, например / set 30. "
                              "Затем бот устанавливает задание для отправки сообщения этому пользователю через 30 секунд. "
                              "Пользователь также может отменить таймер, отправив / отключив. "
                              "Чтобы узнать больше о JobQueue, прочитайте эту статью в вики")


def conv_bot(bot, update):
    update.message.reply_text("Общей задачей для бота является запрос информации от пользователя.\n "
                              "В v5.0 этой библиотеки мы ввели эту задачу для этой цели.\n "
                              "В этом примере используется для извлечения пользовательской информации в стиле, подобном разговору.\n"
                              "Чтобы получить лучшее понимание, взгляните на диаграмму состояния.\n")


def conv_bot2(bot, update):
    update.message.reply_text("Более сложный пример бота, который использует ConversationHandler."
                              "Это также более запутанно. Хорошо, что для этого тоже есть диаграмма фигурного состояния!")


def inlinebot(bot, update):
    update.message.reply_text(
        "• Основной пример встроенного бота. Не забудьте включить встроенный режим с помощью @BotFather.")


def persistentconversationbot(bot, update):
    update.message.reply_text("Основной пример состояния сеанса хранения бота и user_data по нескольким перезапускам.")





def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater("TOKEN")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("echobot2", echobot2))
    dp.add_handler(CommandHandler("conversationbot", conv_bot))
    dp.add_handler(CommandHandler("conversationbot2", conv_bot2))
    dp.add_handler(CommandHandler("inlinebot", inlinebot))
    dp.add_handler(CommandHandler("timerbot", timerbot))

    dp.add_handler(MessageHandler(Filters.text))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
