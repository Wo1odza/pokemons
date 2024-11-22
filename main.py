import telebot
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons.keys():  #Изменено: сравниваем с общим словарем класса
        pokemon = Pokemon(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)