## install pygame with 'pip install pygame'

import random
import pygame

def colors():
    '''
    **Returns**
        colors_map: *dict, int, tuple*
            dictionary of colors used for drawing game board
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

    Parameters
    ----------
        game_board: *list, str, int*
            list of list of information provided by the game
        Comm_cards: *list*
            list of str for community cards
        Chance_cards: *list*
            list of str for chance cards
        

    Return
    ------
        board: *list*
            list of objects representing locations on game board
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
        ['Property', 'St.Charles Place', 'pink', 140, \
         [10, 50, 150, 450, 625, 750], 100, 'Bank', 0],
        ['Utility', 'Electric Company', 150, 'Bank'],
        ['Property', 'States Avenue', 'pink', 140, \
         [10, 50, 150, 450, 625, 750], 100, 'Bank', 0],
        ['Property', 'Virginia Avenue', 'pink', 160, \
         [12, 60, 180, 500, 700, 900], 100, 'Bank', 0],
        ['Station', 'Pennsylvania Railroad', 200, 'Bank'],
        ['Property', 'St.James Place', 'orange', 180, \
         [14, 70, 200, 550, 750, 950], 100, 'Bank', 0],
        ['Card', 'Community Chest'],
        ['Property', 'Tennessee Avenue', 'orange', 180, \
         [14, 70, 200, 550, 750, 950], 100, 'Bank', 0],
        ['Property', 'NewYork Avenue', 'orange', 200, \
         [16, 80, 220, 600, 800, 1000], 100, 'Bank', 0],
        ['Stop', 'Free Parking'],
        ['Property', 'Kentucky Avenue', 'red', 220, \
         [18, 90, 250, 700, 875, 1050], 150, 'Bank'],
        ['Card', 'Chance'],
        ['Property', 'Indiana Avenue', 'red', 220, \
         [18, 90, 250, 700, 875, 1050], 150, 'Bank'],
        ['Property', 'Illinois Avenue', 'red', 240, \
         [20, 100, 300, 750, 925, 1100], 150, 'Bank'],
        ['Station', 'B&O Railroad', 200, 'Bank'],
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
        'Doctor???s fee. Pay $50',
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
    baltic_ave = Title(game_board[3])
    income_tax = Title(game_board[4])
    reading_rr = Title(game_board[5])
    orient_ave = Title(game_board[6])
    vermont_ave = Title(game_board[8])
    conn_ave = Title(game_board[9])
    jail = Title(game_board[10])
    st_charles_place = Title(game_board[11])
    electric_company = Title(game_board[12])
    states_ave = Title(game_board[13])
    virginia_ave = Title(game_board[14])
    penn_rr = Title(game_board[15])
    st_james = Title(game_board[16])
    ten_ave = Title(game_board[18])
    ny_ave = Title(game_board[19])
    free_parking = Title(game_board[20])
    kentucky_ave = Title(game_board[21])
    indiana_ave = Title(game_board[23])
    illinois_ave = Title(game_board[24])
    bno_rr = Title(game_board[25])
    atlantic_ave = Title(game_board[26])
    ventnor_ave = Title(game_board[27])
    water_works = Title(game_board[28])
    marvin_gardens = Title(game_board[29])
    go_to_jail = Title(game_board[30])
    pacific_ave = Title(game_board[31])
    nc_ave = Title(game_board[32])
    penn_ave = Title(game_board[34])
    short_rr = Title(game_board[35])
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


class Die(object):
    def __init__(self):
        '''
        This function simulates rolling of 2 dice
        Parameters
        ----------
        roll_history: *list*
            Stores values rolled as list
        '''
        self.roll_history = []

    def roll(self):
        '''
        This function generates values from rolling 2 dices
        Parameters
        ----------
        value: *int*
            For holding total rolled value
        double: *bool*
            boolean for if both dice rolled the same value
        roll1: *int*
            first dice roll number
        roll2: *int*
            second dice roll number

        Return
        ------
        value: *int*
            Total rolled value
        double : *bool*
            True if if both dice rolled the same value
        '''
        value = 0
        double = False

        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll1 == roll2:
            double = True
        value = roll1 + roll2
        self.roll_history.append(value)

        return value, double

class Title(object):
    def __init__(self, location):
        '''
        Generate a object for locations on game board

        Parameters
        ----------
        location : *list, str, int*
            Stores base information from game board
        
        type: *str*
            Type of location on the board
        name: *str*
            Name of location on the board
        color: *str*
            color of property
        Title_cost: *int*
            cost of location
        rents: *list, int*
            rent of property depending on house built from lowest to highest
        owner: *str, object*
            owner of property. Bank *str* owns by default, players are object class
        house_level: *int*
            number of houses built, 5 = hotel in game

        Returns
        -------
        None.

        '''
        self.type = location[0]
        self.name = location[1]
        self.color = 'white'

        if self.type == 'Property':
            self.color = location[2]
            self.Title_cost = location[3]
            self.rents = location[4]
            self.house_cost = location[5]
            self.owner = location[6]
            self.house_level = 0
        if self.type == 'Station' or self.type == 'Utility':
            self.Title_cost = location[2]
            self.owner = location[3]


    def buy(self, player):
        '''
        Function changes owner and reduce player money

        Parameters
        ----------
        None

        '''
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
        '''
        Function returns owner to default and increase player money

        Parameters
        ----------
        None


        '''
        self.owner = 'Bank'
        player.add_money(self.Title_cost)
        if self.type == 'Station':
            player.railroad_own -= 1
        if self.type == 'Utility':
            player.utility_own -= 1

    def build_house(self, player):
        '''
        Function increase house_level in exchange for player money

        Parameters
        ----------


        '''

        if self.house_cost > player.bal:
            print('unaffordable')
        elif self.house_level == 5:
            self.max_houses = True
        else:
            self.house_level += 1
            player.take_money(self.house_cost)


class Cards(object):
    def __init__(self, Cards, name):
        '''
        Function simulate a deck of cards

        Parameters
        ----------
        Cards: *list, str*
            list of cards
        name: *str*
            Name of the deck of card ie 'Chance' or 'Community Chest'
        type: *str*
            type of location on the board

        Returns
        -------
        None

        '''
        self.type = name
        self.cards = Cards
        self.name = name
        self.holder = []
        self.deck = []

    def draw_card(self):
        '''
        Picks a value refering to a card in the deck 

        Returns
        -------
        card : *int*
            number representing the card in the list of cards

        '''
        if self.deck == []:
            self.deck = self.shuffle()
        card = self.deck.pop()
        self.read_card(card)
        return card

    def shuffle(self):
        '''
        Creates a representation of a list of card and shuffles it

        Returns
        -------
        deck : *list, int*
            list of numbers to refer to the deck of cards

        '''
        for i in range(len(self.cards)):
            self.holder.append(i)
        self.deck = random.shuffle(self.holder)
        return self.deck

    def read_card(self, card):
        '''
        Takes the card drawn and reads the card

        Returns
        -------
        card_text: *str*
            description of card

        '''
        self.card_text = self.cards[card]
        return self.card_text

    def card_effect(self, card, player):
        '''
        Function to implement effect of card drawn *Incomplete

        '''
        if self.name == 'Chance':
            if card == 1:
                print(1)


class player(object):
    def __init__(self, playername):
        '''
        

        Parameters
        ----------
        bal : *int*
            balance of player
        Title_owned: *list*
            list of titles owned
        railroad_owned: *int*
            number of railroads owned
        utility_own: *int*
            number of utility own
        pos: *int*
            current position on board
        double_count: *int*
            counting how many consequtive double rolls
        jail_free_card: *int*
            number of jail free card
        bankrupt_flag: *bool*
            bankrupt status
        jail_flag: *bool*
            jail status


        Returns
        -------

        '''
        self.name = playername
        self.bal = 1500
        self.Title_owned = []
        self.railroad_own = 0
        self.utility_own = 0
        self.pos = 0
        self.double_count = 0
        self.jail_free_card = 0
        self.turn_in_jail = 0
        self.bankrupt_flag = False
        self.jail_flag = False
        self.turn = 0

    def move(self):
        '''
        Changes player position by dice roll

        Returns
        -------


        '''

        steps, double = Die.roll()
        if double == True:
            self.double_count += 1
            if self.double_count == 3:
                self.jail()
        self.pos += steps
        self.turn += 1


    def check_pos(self, board):
        '''
        Check player position for location effects

        Returns
        -------
        None.

        '''
        self.pos = self.pos % 40
        locale = board[self.pos]
        if locale.type == 'Property':
            if locale.owner == 'Bank':
                locale.buy()
            else:
                self.take_money(locale.rent[locale.house_level])
                locale.owner.add_money(locale.rent[locale.house_level])

    def add_money(self, amount):
        '''
        Adds player balance 

        Returns
        -------


        '''
        self.bal += amount

    def take_money(self, amount):
        '''
        Reduce player balance 

        Returns
        -------


        '''
        if self.bal < amount:
            if len(self.Title_owned) < 0:
                self.bankrupt_flag = True
                self.bankrupt()
            else:
                Title.sell(input, self)
        else:
            self.bal -= amount

    def to_jail(self):
        '''
        Moves player to jail and set jail status
        '''
        self.pos = 10
        self.double_count = 0
        self.jail_flag = True

    def jail_check(self):
        '''
        Checks jail status

        Returns
        -------

        '''
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
        '''
        add jail free card
        '''
        self.jail_free_card += 1

    def use_jail_free_card(self):
        '''
        Escapes jail using card

        Returns
        -------
        None.

        '''
        self.jail_free_card -= 1
        self.jail_flag = False
        self.turn_in_jail = 0

    def bankrupt(self):
        '''
        banrupt player
        '''
        self.bal = 0
        self.bankrupt_flag = True
        if len(self.Title_owned) != 0:
            for Title in self.Title_owned:
                Title.owner = 'Bank'


class game_display(object):
    def __init__(self, screen, color, board):
        '''
        Function drawns the GUI for the game
        '''
        self.color = color
        self.screen = screen
        self.board = board
        self.titlefont = pygame.font.SysFont('Corbel', 10)
        self.Statfont = pygame.font.SysFont('Times New Roman', 20)
        self.GameStart = False

    def StartGame(self):
        self.GameStart = True
        print(self.GameStart)
        return self.GameStart

    def EndGame(self):
        return True

    def draw_map(self):
        x = 90 # Width of corner square
        y = (720 - 2*x)//9 # Width of each box along the sides
        pygame.draw.lines(self.screen, 'black', True, \
                                        [(x, x), (720 - x, x), (720 - x, 720 - x), (x, 720 - x)])
        pygame.draw.lines(self.screen, 'black', True, \
                                        [(0, 0), (720, 0), (720, 720), (0, 720)])
        pygame.draw.rect(self.screen, 'yellow', pygame.Rect(721, 0, 560, 720))
        pygame.draw.lines(self.screen, 'red', False, \
                                        [(700, 700), (650, 700), (670, 690), (650, 700), (670, 710)], 3)
        for i in range(10):
            pygame.draw.line(self.screen, 'black', (x, x + i*y), (x - x, x + i*y))
            pygame.draw.line(self.screen, 'black', (x + i*y, x), (x + i*y, x - x))
            pygame.draw.line(self.screen, 'black', (720 - x, x + i*y), (720 - x + x, x + i*y))
            pygame.draw.line(self.screen, 'black', (x + i*y, 720 - x), (x + i*y, 720 - x + x))

            

            if i == 0:
                text1 = self.titlefont.render(self.board[0].name, True, self.color['black'])
                text1_rect = text1.get_rect(center = (720 - x//2, (720 -x//2)))
                text2 = self.titlefont.render(self.board[10].name, True, self.color['black'])
                text2_rect = text2.get_rect(center = (x//2, (720 -x//2)))
                text3 = self.titlefont.render(self.board[20].name, True, self.color['black'])
                text3_rect = text3.get_rect(center = (x//2, x//2))
                text4 = self.titlefont.render(self.board[30].name, True, self.color['black'])
                text4_rect = text4.get_rect(center = (720 - x//2, x//2))

                self.screen.blit(text1, text1_rect)
                self.screen.blit(text2, text2_rect)
                self.screen.blit(text3, text3_rect)
                self.screen.blit(text4, text4_rect)

            else:
                words1 = self.board[0 + i].name.split(' ')
                words2 = self.board[10 + i].name.split(' ')
                words3 = self.board[20 + i].name.split(' ')
                words4 = self.board[30 + i].name.split(' ')

                for k in range(len(words1)):
                    text = self.titlefont.render(words1[k], True, self.color['black'])
                    text_rect = text.get_rect(center = ((720 - x - y//2) - (i - 1)*y, (720 - x//2) + k * 10))
                    self.screen.blit(text, text_rect)

                for k in range(len(words2)):
                    text = self.titlefont.render(words2[k], True, self.color['black'])
                    text_rect = text.get_rect(center = ((x//2), (720 - x - y//2) - (i - 1) * y + k * 10))
                    self.screen.blit(text, text_rect)

                for k in range(len(words3)):
                    text = self.titlefont.render(words3[k], True, self.color['black'])
                    text_rect = text.get_rect(center = ((720 - x - y//2) - (i - 1)*y, (x//2) + k * 10))
                    self.screen.blit(text, text_rect)

                for k in range(len(words4)):
                    text = self.titlefont.render(words4[k], True, self.color['black'])
                    text_rect = text.get_rect(center = ((720 - x//2) , (x + y//2) + (i - 1) * y + k * 10))
                    self.screen.blit(text, text_rect)

            if self.board[i].type == 'Property':
                pygame.draw.rect(self.screen, self.board[i].color, \
                                 pygame.Rect((720 - x - y + 1) - (i - 1) * y, (720 - x + 1) , y - 1, x // 5 ))
            if self.board[10 + i].type == 'Property':
                pygame.draw.rect(self.screen, self.board[10 + i].color, \
                                 pygame.Rect((x - x//5), (720 - x - y +1) - (i - 1) * y, x//5, y - 1))
            if self.board[20 + i].type == 'Property':
                pygame.draw.rect(self.screen, self.board[20 + i].color, \
                                 pygame.Rect(x + 1 + (i - 1) * y, x * 4/5 , y - 1, x // 5 ))
            if self.board[30 + i].type == 'Property':
                pygame.draw.rect(self.screen, self.board[30 + i].color, \
                                 pygame.Rect((720 - x + 1), (x + 1) + (i - 1) * y, x//5, y - 1))

    def player_display(self, player, n):
        for i in range(n):
            pygame.draw.rect(self.screen, 'white', pygame.Rect(800, 120 + i * 40, 400, 30))
            pygame.draw.rect(self.screen, 'black', pygame.Rect(800, 120 + i * 40, 400, 30), 2)
            text = "Player: " + player[i].name
            name = self.Statfont.render(text, True, 'black')
            text = '   $' + str(player[i].bal)
            balance = self.Statfont.render(text, True, 'black')
            self.screen.blit(name, (805, 126 + i * 40))
            name_width = name.get_width()
            self.screen.blit(balance, (805 + name_width, 126 + i * 40))

            if player[i].jail_flag == True:
                text = self.Statfont.render('In Jail', True, 'red')
                self.screen.blit(text, (1100, 126 + i * 40))

            if player[i].bankrupt_flag == True:
                text = self.Statfont.render('Bankrupt!', True, 'red')
                self.screen.blit(text, (1100, 126 + i * 40))

    def player_piece(self, player):
        None

    def addimage(self, link, x, y):
         img = pygame.image.load(link)
         self.screen.blit(img, [x,y])

    def Text(self, x, y, text, Font = 'Times New Roman', size = 30, alpha = 255, color = 'black'):
        font = pygame.font.SysFont(Font, size)
        msg = font.render(text, True, color)
        msg.set_alpha(alpha)
        self.screen.blit(msg, (x, y - size))

class button(object):
    def __init__(self, screen, x, y, title, Font = 'Times New Roman', size = 30, color = 'cyan', playernum = 0):
        # global display
        self.screen = screen
        self.x = x
        self.y = y
        self.title = title
        self.Buttonfont = pygame.font.SysFont(Font, size)
        self.text = self.Buttonfont.render(title, True, 'black')
        self.color = color
        self.button_width = self.text.get_width()
        self.button_height = self.text.get_height()

    def show(self):
        pygame.draw.rect(self.screen, self.color, \
                         pygame.Rect(self.x - 5, self.y, self.button_width + 10, self.button_height))
        pygame.draw.rect(self.screen, 'black', \
                         pygame.Rect(self.x - 5, self.y, self.button_width + 10, self.button_height), 1)
        self.rect = pygame.Rect(self.x, self.y, self.button_width, self.button_height)

        self.screen.blit(self.text, (self.x, self.y))

    def click(self, event, time = 0):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if self.title == 'Start Game':
                        if len(players) == 0:
                            display.Text(x, y, 'Add a player!', 'Arial', color = 'red')
                        else:
                            display.StartGame()
    
                    if self.title == 'Roll Dice':
                        player.move(player[self.playernum])
    
                    if self.title == 'End Turn':
                        player.turn += 1
    
                    if self.title == 'Add Player':
                        players.append(player(str(len(players) + 1)))
                        if time > 0:
                            display.Text(self.x, self.y, '+ 1 Player')
                            time -= 1

def load_dice_img():
    img = []
    img.append(pygame.image.load('img/dice1.png'))
    img.append(pygame.image.load('img/dice1.png'))
    img.append(pygame.image.load('img/dice1.png'))
    img.append(pygame.image.load('img/dice1.png'))
    img.append(pygame.image.load('img/dice1.png'))
    img.append(pygame.image.load('img/dice1.png'))
    return img

def Run():
    size = [1280, 720]
    global display, players, turn

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Monopoly Board Game")
    running = True
    clock = pygame.time.Clock()
    color = colors()
    board = initialise_board()

    players = []
    turn = 0
    display = game_display(screen, color, board)

    while running:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color['white'])

        display.draw_map()

        if display.GameStart == True:
            Move_Turn = button(screen, 200, 200, 'Roll Dice')
            Move_Turn.show()

            End_Turn = button(screen, 400, 200, 'End Turn')
            End_Turn.show()


            End_Game = button(screen, 300, 500, 'End Game')
            End_Game.show()


            display.player_display(players, len(players))

            Move_Turn.click(event)
            End_Turn.click(event)
            End_Game.click(event)


        else:
            Start_button = button(screen, 300, 360, 'Start Game')
            Start_button.show()
            Start_button.click(event)

            if len(players) < 4:
                display.Text(800, 300, 'Number of players: ' + str(len(players)))
                Add_Player = button(screen, 800, 300, 'Add Player', size = 50)
                Add_Player.show()
                Add_Player.click(event, time = 90)
            else:
                display.Text(800, 300, 'Max number of players: 4')

        pygame.display.update()

    return


if __name__ == '__main__':
    pygame.init()
    Run()
    pygame.quit()

