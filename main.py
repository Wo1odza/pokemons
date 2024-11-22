import telebot
from config import token
from logic import Pokemon, pokemons

bot = telebot.TeleBot(token) # <--- Переместили эту строку

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in pokemons:
        pokemon = Pokemon(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

bot.infinity_polling(none_stop=True)