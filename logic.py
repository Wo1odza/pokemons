from random import randint, choices
import requests

pokemons = {} # Глобальный словарь

class Pokemon:
    rarities = ["обычный", "необычный", "редкий", "эпический", "легендарный", "чемпион"]
    rarity_weights = [50, 30, 15, 4, 0.9, 0.1]

    def __init__(self, pokemon_trainer):
        pokemons[pokemon_trainer] = self # Сохраняем в глобальном словаре
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.rarity = choices(self.rarities, weights=self.rarity_weights)[0]
        self.pokemons = {} # Словарь создается для каждого объекта
        self.pokemons[pokemon_trainer] = self

        # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"

    
    # sigma, Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покемона: {self.name}\nРедкость: {self.rarity}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img




