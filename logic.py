import datetime
from datetime import timedelta
from random import randint
import requests

class Pokemon:
    pokemons = {}  # { username : pokemon}
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(30, 60)
        self.hp = randint(200, 400)
        self.last_feed_time = datetime.datetime.now() # Добавление атрибута
        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]['official-artwork']["front_default"])
        else:
            return "https://static.wikia.nocookie.net/anime-characters-fight/images/7/77/Pikachu.png/revision/latest/scale-to-width-down/700?cb=20181021155144&path-prefix=ru"

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def info(self):
        return f"""Your pokemon name: {self.name}
Strength: {self.power}
Heal points: {self.hp}"""

    def show_img(self):
        return self.img

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return "Pokemon-wizard used shield!"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"""Fighter 1 @{self.pokemon_trainer} FIghter 2 @{enemy.pokemon_trainer}
heal points @{enemy.pokemon_trainer} is now {enemy.hp}"""
        else:
            enemy.hp = 0
            return f"Winner: @{self.pokemon_trainer} Loser: @{enemy.pokemon_trainer}! "


class Wizard(Pokemon):
    def feed(self, feed_interval=12, hp_increase=15): # Переопределение метода feed
        return super().feed(feed_interval, hp_increase)


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nPokemon used heavy attack!:{super_power} "

    def feed(self, feed_interval=8, hp_increase=20): # Переопределение метода feed
        return super().feed(feed_interval, hp_increase)