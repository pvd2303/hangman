# Игра Интуиция
# по анологии с Глава 15. Практикум. ЧастьII

from random import shuffle

# КАРТЫ**********
# Этот класс моделирует набор карт
class Card:
    suits = ["белая",
             "черная"]

    def __init__(self, s):
        """ suit - целое число"""
        self.suit = s

    def __repr__(self):
        s = self.suits[self.suit]
        return s

# КОЛОДА**********
# Этот класс представляет колоду карт
class Deck:
    def __init__(self, numbers):
        self.numbers = numbers  # количество карт в колоде черных и белых
        self.cards = []
        for i in range(int(self.numbers / 2)):
            for j in range(2):
                self.cards.append(Card(j))
        shuffle(self.cards)     # Перемешивание колоды карт

    def rm_card(self):          # Изымаем одну карту из колоды
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# ИГРОК**********
"""
Этот класс для представления игрока,
чтобы отслеживать его карты и количество выигранных
им раундов
"""
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

# ИГРА**********
# Этот класс представляет игру
class Game:
    def __init__(self):
        name = input("Имя игрока: ")
        numbers = int(input("Введите общее количество карт черных и белых: "))
        self.deck = Deck(numbers)
        self.p = Player(name)

    def draw(self, phn, phc, pcc):
        d = "{} выбрал {}, а компьютер показал {}"
        d = d.format(phn, phc, pcc)
        print(d)

    def play_game(self):
        choice = 0          # Выбор карты
        numbers_card = 0    # Счетчик открытых карт компьютером
        cards = self.deck.cards
        print("Поехали!")
        phn = self.p.name
        m = "Нажмите X или x для выхода. " \
            "Нажмите любую другую клавишу для " \
            "начала игры."
        print(m)

        while len(cards) > 0:
            choice = input("Выберите цвет карты: 0 - белая, 1 - черная: ")

            if choice == 'X' or choice == 'x':
                break
            if choice != "0" and choice != "1":
                print("Введите правильный символ: 0, 1 , или Х или х")
                pass
            else:
                numbers_card += 1
                phc = Card(int(choice))
                pcc = self.deck.rm_card()
                self.draw(phn, phc, pcc)

                #print(phc, pcc)
                if phc.suit == pcc.suit:
                    self.p.wins += 1

        print("Игра окончена.{}{} угадал {} из {} карт.".\
              format("\n", self.p.name, self.p.wins, numbers_card))
        intuition = int(self.p.wins / numbers_card * 100)
        print("Интуиция {} %".format(intuition))

game = Game()
game.play_game()