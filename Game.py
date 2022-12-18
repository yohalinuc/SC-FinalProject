## install pygame with 'pip install pygame'

import random
import pygame

def colors():
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

def board():
    return [
        ['Go', 200],
        ['Property', 'Mediterranean Avenue', 'brown', 60, \
         [2, 10, 30, 90, 160, 250], 50],
        ['Community Chest'],
        ['Property', 'Baltic Avenue', 'brown', 60, \
         [4, 20, 60, 180, 320, 450], 50],
        ['Tax', 'Income Tax', 200],
        ['Station', 'Reading Railroad', 200],
        ['Property', 'Oriental Avenue', 'cyan', 100, \
         [6, 30, 90, 270, 400, 550], 50],
        ['Chance'],
        ['Property', 'Vermont Avenue', 'cyan', 100, \
         [6, 30, 90, 270, 400, 550], 50],
        ['Property', 'Connecticut Avenue', 'cyan', 120, \
         [8, 40, 100, 300, 450, 600], 50],
        ['Go to Jail/Just Visiting'],
        ['Property', 'St. Charles Place', 'pink', 140, \
         [10, 50, 150, 450, 625, 750], 100],
        ['Utility', 'Electric Company', 150],
        ['Property', 'States Avenue', 'pink', 140, \
         [10, 50, 150, 450, 625, 750], 100],
        ['Property', 'Virginia Avenue', 'pink', 160, \
         [12, 60, 180, 500, 700, 900], 100],
        ['Station', 'Pennsylvania Railroad', 200],
        ['Property', 'St. James Place', 'orange', 180, \
         [14, 70, 200, 550, 750, 950], 100],
        ['Community Chest'],
        ['Property', 'Tennessee Avenue', 'orange', 180, \
         [14, 70, 200, 550, 750, 950], 100],
        ['Property', 'New York Avenue', 'orange', 200, \
         [16, 80, 220, 600, 800, 1000], 100],
        ['Free Parking'],
        ['Property', 'Kentucky Avenue', 'red', 220, \
         [18, 90, 250, 700, 875, 1050], 150],
        ['Chance'],
        ['Property', 'Indiana Avenue', 'red', 220, \
         [18, 90, 250, 700, 875, 1050], 150],
        ['Property', 'Illinois Avenue', 'red', 240, \
         [20, 100, 300, 750, 925, 1100], 150],
        ['Station', 'B & O Railroad', 200],
        ['Property', 'Atlantic Avenue', 'yellow', 260, \
         [22, 110, 330, 800, 975, 1150], 150],
        ['Property', 'Ventnor Avenue', 'yellow', 260, \
         [22, 110, 330, 800, 975, 1150], 150]
        ['Utility', 'Water Works', 150],
        ['Property', 'Marvin Gardens', 'yellow', 280, \
         [24, 120, 360, 850, 1025, 1200], 150],
        ['Go to Jail'],
        ['Property', 'Pacific Avenue', 'green', 300, \
         [26, 130, 390, 900, 1100, 1275], 200],
        ['Property', 'North Carolina Avenue', 'green', 300, \
         [26, 130, 390, 900, 1100, 1275], 200],
        ['Community Chest'],
        ['Property', 'Pennsylvania Avenue', 'green', 320, \
         [28, 150, 450, 1000, 1200, 1400], 200],
        ['Station', 'Short Line', 200],
        ['Chance'],
        ['Property', 'Park Place', 'blue', 350, \
         [35, 175, 500, 1100, 1300, 1500], 200],
        ['Tax', 'Luxury Tax', 100],
        ['Property', 'Boardwalk', 'blue', 400, \
         [50, 200, 600, 1400, 1700, 2000], 200]
        ]

def CommunityCard():
    return [
        ['Advance to Go (Collect $200)', 200],
        ['Bank error in your favor. Collect $200', 200],
        ['Doctor’s fee. Pay $50', 50],
        ['From sale of stock you get $50', 50],
        ['Get Out of Jail Free'],
        ['Go to Jail. Go directly to jail, do not pass Go, do not collect $200'],
        ['Holiday fund matures. Receive $100', 100],
        ['Income tax refund. Collect $20', 20],
        ['It is your birthday. Collect $10 from every player', 10],
        ['Life insurance matures. Collect $100', 100],
        ['Pay hospital fees of $100', -100],
        ['Pay school fees of $50', -50],
        ['Receive $25 consultancy fee', 25],
        ['You are assessed for street repair. $40 per house. $115 per hotel', 40, 115],
        ['You have won second prize in a beauty contest. Collect $10', 10],
        ['You inherit $100', 100]
        ]

def ChanceCard():
    return [
        ['Advance to Boardwalk'],
        ['Advance to Go (Collect $200)', 200]
        ['Advance to Illinois Avenue. If you pass Go, collect $200', 200]
        ['Advance to St. Charles Place. If you pass Go, collect $200', 200]
        ['Advance to the nearest Railroad. If unowned, you may buy it from the Bank. \
        If owned, pay wonder twice the rental to which they are otherwise entitled'],
        ['Advance to the nearest Railroad. If unowned, you may buy it from the Bank. \
        If owned, pay wonder twice the rental to which they are otherwise entitled'],
        ['Advance token to nearest Utility. If unowned, you may buy it from the Bank. \
        If owned, throw dice and pay owner a total ten times amount thrown.'],
        ['Bank pays you dividend of $50', 50]
        ['Get Out of Jail Free'],
        ['Go Back 3 Spaces'],
        ['Go to Jail. Go directly to Jail, do not pass Go, do not collect $200',]
        ['Make general repairs on all your property. For each house pay $25. \
        For each hotel pay $100', 25, 100]
        ['Speeding fine $15', 15]
        ['Take a trip to Reading Railroad. If you pass Go, collect $200', 200]
        ['You have been elected Chairman of the Board. Pay each player $50', 50]
        ['Your building loan matures. Collect $150', 150]
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

class Deed(object):
    def __init__(self, name, color, cost, rent, house_cost, owner):




class Player(object):
    def __init__(self, playernumber, balance, property_owned, position):
        self.number = playernumber
        self.balance = balance
        self.owned = property_owned
        self.pos = position

    def move(self):
        steps, double = Die()
        self.pos += steps
        return self.pos

    def check_pos(self, board):
        self.pos = self.pos % 40
        locale = board[self.pos]

# class Button(object):
#     def __init__(self, screen, color):
#         pygame.draw.rect(screen, color['cyan'], [190,200,75,35])
#         smallfont = pygame.font.SysFont('Times New Roman',35)
#         text = smallfont.render('test', True, color['black'])
#         screen.blit(text, (200, 200))

def Run():
    size = [1280, 720]
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Monopoly Board Game")
    running = True
    clock = pygame.time.Clock()
    color = colors()

    
    while running:
        clock.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("test",event.type)
                running = False
        screen.fill(color['white'])
        Button(screen, color)
        pygame.display.flip()

    return


if __name__ == '__main__':
    pygame.init()
    Run()
    pygame.quit()

