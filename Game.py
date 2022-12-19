## install pygame with 'pip install pygame'

import random
import pygame

def colors():
    '''
    Returns
    dictionary of colors used for game board

    '''
    return {
        'red':(255, 0, 0),
        'yellow':(255, 255, 0),
        'green':(0, 255, 0),
        'blue':(0, 0, 255),
        'brown':(165, 42, 42),
        'cyan':(0, 120, 120),
        'pink':(255, 192, 203),
        'orange':(255, 165, 0),
        'black':(0, 0, 0),
        'white':(255, 255, 255)
        }

def initialise_board():
    '''
    Initialise the game board locations and ownerships
    Returns
    -------
    list of locations on game board and information as provided by game

    '''
    game_board = [
        ['Start', 'Go', 200],
        ['Property', 'Mediterranean Avenue', 'brown', 60, \
         [2, 10, 30, 90, 160, 250], 50, 'Bank', 0],
        ['Card', 'Community Chest'],
        ['Property', 'Baltic Avenue', 'brown', 60, \
         [4, 20, 60, 180, 320, 450], 50, 'Bank', 0],
        ['Tax', 'Income Tax', 200],
        ['Station', 'Reading Railroad', 200, 'Bank'],
        ['Property', 'Oriental Avenue', 'cyan', 100, \
         [6, 30, 90, 270, 400, 550], 50, 'Bank', 0],
        ['Card', 'Chance'],
        ['Property', 'Vermont Avenue', 'cyan', 100, \
         [6, 30, 90, 270, 400, 550], 50, 'Bank', 0],
        ['Property', 'Connecticut Avenue', 'cyan', 120, \
         [8, 40, 100, 300, 450, 600], 50, 'Bank', 0],
        ['Jail', 'Go to Jail/Just Visiting'],
        ['Property', 'St. Charles Place', 'pink', 140, \
         [10, 50, 150, 450, 625, 750], 100, 'Bank', 0],
        ['Utility', 'Electric Company', 150, 'Bank'],
        ['Property', 'States Avenue', 'pink', 140, \
         [10, 50, 150, 450, 625, 750], 100, 'Bank', 0],
        ['Property', 'Virginia Avenue', 'pink', 160, \
         [12, 60, 180, 500, 700, 900], 100, 'Bank', 0],
        ['Station', 'Pennsylvania Railroad', 200, 'Bank'],
        ['Property', 'St. James Place', 'orange', 180, \
         [14, 70, 200, 550, 750, 950], 100, 'Bank', 0],
        ['Card', 'Community Chest'],
        ['Property', 'Tennessee Avenue', 'orange', 180, \
         [14, 70, 200, 550, 750, 950], 100, 'Bank', 0],
        ['Property', 'New York Avenue', 'orange', 200, \
         [16, 80, 220, 600, 800, 1000], 100, 'Bank', 0],
        ['Stop', 'Free Parking'],
        ['Property', 'Kentucky Avenue', 'red', 220, \
         [18, 90, 250, 700, 875, 1050], 150, 'Bank'],
        ['Card', 'Chance'],
        ['Property', 'Indiana Avenue', 'red', 220, \
         [18, 90, 250, 700, 875, 1050], 150, 'Bank'],
        ['Property', 'Illinois Avenue', 'red', 240, \
         [20, 100, 300, 750, 925, 1100], 150, 'Bank'],
        ['Station', 'B & O Railroad', 200, 'Bank'],
        ['Property', 'Atlantic Avenue', 'yellow', 260, \
         [22, 110, 330, 800, 975, 1150], 150, 'Bank'],
        ['Property', 'Ventnor Avenue', 'yellow', 260, \
         [22, 110, 330, 800, 975, 1150], 150, 'Bank'],
        ['Utility', 'Water Works', 150, 'Bank'],
        ['Property', 'Marvin Gardens', 'yellow', 280, \
         [24, 120, 360, 850, 1025, 1200], 150, 'Bank'],
        ['Jail', 'Go to Jail'],
        ['Property', 'Pacific Avenue', 'green', 300, \
         [26, 130, 390, 900, 1100, 1275], 200, 'Bank'],
        ['Property', 'North Carolina Avenue', 'green', 300, \
         [26, 130, 390, 900, 1100, 1275], 200, 'Bank'],
        ['Card', 'Community Chest'],
        ['Property', 'Pennsylvania Avenue', 'green', 320, \
         [28, 150, 450, 1000, 1200, 1400], 200, 'Bank'],
        ['Station', 'Short Line', 200, 'Bank'],
        ['Card', 'Chance'],
        ['Property', 'Park Place', 'blue', 350, \
         [35, 175, 500, 1100, 1300, 1500], 200, 'Bank'],
        ['Tax', 'Luxury Tax', 100],
        ['Property', 'Boardwalk', 'blue', 400, \
         [50, 200, 600, 1400, 1700, 2000], 200, 'Bank']
        ]

    Comm_cards = [
        'Advance to Go (Collect $200)',
        'Bank error in your favor. Collect $200',
        'Doctor’s fee. Pay $50',
        'From sale of stock you get $50',
        'Get Out of Jail Free',
        'Go to Jail. Go directly to jail, do not pass Go, do not collect $200',
        'Holiday fund matures. Receive $100',
        'Income tax refund. Collect $20',
        'It is your birthday. Collect $10 from every player',
        'Life insurance matures. Collect $100',
        'Pay hospital fees of $100',
        'Pay school fees of $50',
        'Receive $25 consultancy fee',
        'You are assessed for street repair. $40 per house. $115 per hotel',
        'You have won second prize in a beauty contest. Collect $10',
        'You inherit $100'
        ]

    Chance_cards = [
        'Advance to Boardwalk',
        'Advance to Go (Collect $200)',
        'Advance to Illinois Avenue. If you pass Go, collect $200',
        'Advance to St. Charles Place. If you pass Go, collect $200',
        'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. \
        If owned, pay owner twice the rental to which they are otherwise entitled',
        'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. \
        If owned, pay owner twice the rental to which they are otherwise entitled',
        'Advance token to nearest Utility. If unowned, you may buy it from the Bank. \
        If owned, throw dice and pay owner a total ten times amount thrown.',
        'Bank pays you dividend of $50',
        'Get Out of Jail Free',
        'Go Back 3 Spaces',
        'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200',
        'Make general repairs on all your property. For each house pay $25. \
        For each hotel pay $100',
        'Speeding fine $15',
        'Take a trip to Reading Railroad. If you pass Go, collect $200',
        'You have been elected Chairman of the Board. Pay each player $50',
        'Your building loan matures. Collect $150'
        ]

    go = Title(game_board[0])
    med_ave = Title(game_board[1])
    # comm_chest = Cards(Comm_cards)
    baltic_ave = Title(game_board[3])
    income_tax = Title(game_board[4])
    reading_rr = Title(game_board[5])
    orient_ave = Title(game_board[6])
    # chance = Cards(game_board[7])
    vermont_ave = Title(game_board[8])
    conn_ave = Title(game_board[9])
    jail = Title(game_board[10])
    st_charles_place = Title(game_board[11])
    electric_company = Title(game_board[12])
    states_ave = Title(game_board[13])
    virginia_ave = Title(game_board[14])
    penn_rr = Title(game_board[15])
    st_james = Title(game_board[16])
    # comm_chest = Cards(game_board[17])
    ten_ave = Title(game_board[18])
    ny_ave = Title(game_board[19])
    free_parking = Title(game_board[20])
    kentucky_ave = Title(game_board[21])
    # chance = Cards(game_board[22])
    indiana_ave = Title(game_board[23])
    illinois_ave = Title(game_board[24])
    bno_rr = Title(game_board[25])
    atlantic_ave = Title(game_board[26])
    ventnor_ave = Title(game_board[27])
    water_works = Title(game_board[28])
    marvin_gardens = Title(game_board[29])
    go_to_jail = game_board[30]
    pacific_ave = Title(game_board[31])
    nc_ave = Title(game_board[32])
    # comm_chest = Cards(game_board[33])
    penn_ave = Title(game_board[34])
    short_rr = Title(game_board[35])
    # chance = Cards(game_board[36])
    park_place = Title(game_board[37])
    luxury_tax = Title(game_board[38])
    boardwalk = Title(game_board[39])

    chance = Cards(Chance_cards, 'Chance')
    comm_chest = Cards(Comm_cards, 'Community Chest')

    board = [
        go,
        med_ave,
        comm_chest,
        baltic_ave,
        income_tax,
        reading_rr,
        orient_ave,
        chance,
        vermont_ave,
        conn_ave,
        jail,
        st_charles_place,
        electric_company,
        states_ave,
        virginia_ave,
        penn_rr,
        st_james,
        comm_chest,
        ten_ave,
        ny_ave,
        free_parking,
        kentucky_ave,
        chance,
        indiana_ave,
        illinois_ave,
        bno_rr,
        atlantic_ave,
        ventnor_ave,
        water_works,
        marvin_gardens,
        go_to_jail,
        pacific_ave,
        nc_ave,
        comm_chest,
        penn_ave,
        short_rr,
        chance,
        park_place,
        luxury_tax,
        boardwalk
        ]

    return board

def CommunityCard():
    return [
        'Advance to Go (Collect $200)',
        'Bank error in your favor. Collect $200',
        'Doctor’s fee. Pay $50',
        'From sale of stock you get $50',
        'Get Out of Jail Free',
        'Go to Jail. Go directly to jail, do not pass Go, do not collect $200',
        'Holiday fund matures. Receive $100',
        'Income tax refund. Collect $20',
        'It is your birthday. Collect $10 from every player',
        'Life insurance matures. Collect $100',
        'Pay hospital fees of $100',
        'Pay school fees of $50',
        'Receive $25 consultancy fee',
        'You are assessed for street repair. $40 per house. $115 per hotel',
        'You have won second prize in a beauty contest. Collect $10',
        'You inherit $100'
        ]

def ChanceCard():
    return [
        'Advance to Boardwalk',
        'Advance to Go (Collect $200)',
        'Advance to Illinois Avenue. If you pass Go, collect $200',
        'Advance to St. Charles Place. If you pass Go, collect $200',
        'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. \
        If owned, pay owner twice the rental to which they are otherwise entitled',
        'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. \
        If owned, pay owner twice the rental to which they are otherwise entitled',
        'Advance token to nearest Utility. If unowned, you may buy it from the Bank. \
        If owned, throw dice and pay owner a total ten times amount thrown.',
        'Bank pays you dividend of $50',
        'Get Out of Jail Free',
        'Go Back 3 Spaces',
        'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200',
        'Make general repairs on all your property. For each house pay $25. \
        For each hotel pay $100',
        'Speeding fine $15',
        'Take a trip to Reading Railroad. If you pass Go, collect $200',
        'You have been elected Chairman of the Board. Pay each player $50',
        'Your building loan matures. Collect $150'
        ]


class Die(object):
    def __init__(self):
        self.roll_history = []

    def __str__(self):
        return f"Roll: {self.roll_history[-1]}"

    def roll(self):
        value = 0
        double = False

        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll1 == roll2:
            double = True
        value = roll1 + roll2
        # value = random.randint(1, 6)
        self.roll_history.append(value)

        return value, double

class Title(object):
    def __init__(self, location):
        self.type = location[0]
        self.name = location[1]
        # self.color = 'white'

        if self.type == 'Property':
            self.color = location[2]
            self.Title_cost = location[3]
            self.rents = location[4]
            self.house_cost = location[5]
            self.owner = location[6]
            self.house_level = 0
        if self.type == 'Station':
            self.Title_cost = location[2]
            self.owner = location[3]


    def buy(self, player):
        if self.Title_cost > player.bal:
            print('unaffordable')
        else:
            player.owned.append(self)
            player.take_money(self.Title_cost)
            self.owner = player
            if self.type == 'Station':
                player.railroad_own += 1
            if self.type == 'Utility':
                player.utility_own += 1

    def sell(self, player):
        self.owner = 'Bank'
        player.add_money(self.Title_cost)
        if self.type == 'Station':
            player.railroad_own -= 1
        if self.type == 'Utility':
            player.utility_own -= 1

    def build_house(self, player):
        if self.house_cost > player.bal:
            print('unaffordable')
        elif self.house_level == 5:
            self.max_houses = True
        else:
            self.house_level += 1


class Cards(object):
    def __init__(self, Cards, name):
        self.cards = Cards
        self.name = name
        self.holder = []
        self.deck = []

    def draw_card(self):
        if self.deck == []:
            self.deck = self.shuffle()
        card = self.deck.pop()
        self.read_card(card)
        return card

    def shuffle(self):
        for i in range(len(self.cards)):
            self.holder.append(i)
        self.deck = random.shuffle(self.holder)
        return self.deck

    def read_card(self, card):
        self.card_text = self.cards[card]
        return self.card_text

    def card_effect(self, card, player):
        if self.name == 'Chance':
            if card == 1:
                print(1)


class player(object):
    def __init__(self, playernumber, balance, property_owned, position):
        self.number = playernumber
        self.bal = balance
        self.Title_owned = property_owned
        self.railroad_own = 0
        self.utility_own = 0
        self.pos = position
        self.double_count = 0
        self.jail_free_card = 0
        self.turn_in_jail = 0
        self.bankrupt_flag = False
        self.jail_flag = False

    def move(self):
        steps, double = Die()
        
        if double == True:
            self.double_count += 1
            if self.double_count == 3:
                self.jail()
        self.pos += steps
        return self.pos

    def check_pos(self, board):
        self.pos = self.pos % 40
        locale = board[self.pos]
        return locale

    def add_money(self, amount):
        self.bal += amount
        return self.bal

    def take_money(self, amount):
        if self.bal < amount:
            if len(self.Title_owned) < 0:
                self.bankrupt_flag = True
                self.bankrupt()
            else:
                Title.sell(input, self)
        else:
            self.bal -= amount

    def jail(self):
        self.pos = 10
        self.double_count = 0
        self.jail_flag = True

    def jail_check(self):
        if self.turn_in_jail < 3:
            dice = Die()
            val, double = dice.roll()
            if double == True:
                self.jail_flag == False
                self.turn_in_jail = 0
                self.pos += val
            if self.jail_flag == True:
                 self.turn_in_jail += 1
        else:
            self.jail_flag == False
            self.turn_in_jail = 0

    def get_jail_free_card(self):
        self.jail_free_card += 1

    def use_jail_free_card(self):
        self.jail_free_card -= 1
        self.jail_flag = False
        self.turn_in_jail = 0

    def bankrupt(self):
        self.bal = 0
        if len(self.Title_owned) != 0:
            for Title in self.Title_owned:
                Title.owner = 'Bank'


class game_display(object):
    def __init__(self, screen, color, board):
        self.color = color
        self.screen = screen
        # pygame.draw.rect(screen, color['cyan'], [190,200,75,35])
        titlefont = pygame.font.SysFont('Corbel', 20)
        # text = smallfont.render('test', True, color['black'])
        # screen.blit(text, (200, 200))

    def draw_map(self):
        x = 90 # Width of corner square
        y = (720 - 2*x)//9 # Width of each box along the sides
        pygame.draw.lines(self.screen, 'black', True, \
                                        [(x, x), (720 - x, x), (720 - x, 720 - x), (x, 720 - x)])
        pygame.draw.lines(self.screen, 'black', True, \
                                        [(0, 0), (720, 0), (720, 720), (0, 720)])

        for i in range(10):
            pygame.draw.line(self.screen, 'black', (x, x + i*y), (x - x, x + i*y))
            pygame.draw.line(self.screen, 'black', (x + i*y, x), (x + i*y, x - x))
            pygame.draw.line(self.screen, 'black', (720 - x, x + i*y), (720 - x + x, x + i*y))
            pygame.draw.line(self.screen, 'black', (x + i*y, 720 - x), (x + i*y, 720 - x + x))




def Run():
    size = [1280, 720]
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Monopoly Board Game")
    running = True
    clock = pygame.time.Clock()
    color = colors()
    board = initialise_board()

    
    while running:
        clock.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # print("test",event.type)
                running = False
        screen.fill(color['white'])
        display = game_display(screen, color, board)
        display.draw_map()
        # pygame.display.flip()
        pygame.display.update()

    return


if __name__ == '__main__':
    pygame.init()
    Run()
    pygame.quit()
    print('test run')
