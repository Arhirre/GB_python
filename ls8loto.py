# _author_ = Nikita_Savchenko
import random
import sys
import copy


class Barrels:
    def __init__(self, amount):
        self.amount = amount
        self.gen = self.bar_take()

    def bar_take(self):
        taken = []
        b_list = [x for x in range(1, self.amount + 1)]
        random.shuffle(b_list)
        for i, y in enumerate(b_list):
            taken.append(y)
            print('already taken barrels: {} '.format(taken))
            print('Current Barrel: {}! (Remain barrels: {})'.format(y, self.amount - (i + 1)))
            yield y


class Game_loto:
    def __init__(self, cards_amm):
        row = 3
        self.all_rows = row * cards_amm
        self.__set_card()

    def __set_card(self):
        num = set()
        while len(num) < self.all_rows * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_rows != 0:
            cards.append('None')
        self.all_rows = int(len(cards) / self.all_rows)
        cards = [cards[i: i + self.all_rows] for i in range(0, len(cards), self.all_rows)]

        for i in range(len(cards)):
            cards[i].sort()

        # add spaces in random places
        cards_d = copy.deepcopy(cards)
        for line in cards_d:
                for space in ' ' * 4:
                        line.insert(random.randint(0, len(line) - 1), space)

        self.card_user = cards_d[:3]
        self.card_comp = cards_d[3:]

    def get_card(self, card_player):
        print('{:-^25}'.format(self.name))
        #print(card_player)
        print('{0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]}  '.format(card_player[0]))
        print('{0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]}  '.format(card_player[1]))
        print('{0[0]} {0[1]} {0[2]} {0[3]} {0[4]} {0[5]} {0[6]} {0[7]} {0[8]}  '.format(card_player[2]))
        print('{:-^25}'.format('-'))

    def barrel_check(self, card_player, num_bar):
        for i, n in enumerate(card_player):
            if num_bar in n:
                card_player[i][n.index(num_bar)] = '-'
                return True
        return False


class Player(Game_loto):

    def __init__(self, name):
        self.name = name


def play_game():
    game = Game_loto(2)
    barrel = Barrels(90)
    player1 = Player(input("Player 1, Enter your name!"))
    player2 = Player("PC")
    print("Welcome to Loto Game!\nPlease only enter 'y' or 'n' when game will ask you for!\nOtherwise game will close cos you are cheating!")

    while True:
        num_bar = next(barrel.gen)
        player1.get_card(game.card_user)
        player2.get_card(game.card_comp)

        user_in = input('Remove num? (y/n)')
        if user_in == 'y':
            if player1.barrel_check(game.card_user, num_bar):
                continue
            else:
                print('There is no num, Game Over!')
                sys.exit(1)
        if user_in == 'n':
            if player1.barrel_check(game.card_user, num_bar):
                print('You missed num, Game Over!')
                sys.exit(1)
            elif player2.barrel_check(game.card_comp, num_bar):
                continue

        if user_in != 'n' and user_in != 'y':
            print('GAME OVER! Please only enter Y or N next time!')
            sys.exit(1)



play_game()