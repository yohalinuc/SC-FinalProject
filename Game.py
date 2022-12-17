## May need to install pygame using pip install pygame

import random
import pygame

def colors():
    return {
        'red':(255, 0, 0), #1
        'yellow':(255, 255, 0), #2
        'green':(0, 255, 0), #3
        'blue':(0, 0, 255), #4
        'brown':(165, 42, 42), #5
        'cyan':(0, 120, 120), #6
        'pink':(255, 192, 203), #7
        'orange':(255, 165, 0), #8
        'black':(0, 0, 0), #9
        'white':(255, 255, 255) #10
        }

def locations():
    return {
        '0': ['Go', 200],
        '1': ['Mediterranean Avenue', 60],
        '2': ['Community Chest'],
        '3': ['Baltic Avenue', 60],
        '4': ['Income Tax', 200],
        '5': ['Reading Railroad', 200],
        '6': ['Oriental Avenue', 100],
        '7': ['Chance'],
        '8': ['Vermont Avenue', 100],
        '9': ['Connecticut Avenue', 120],
        '10': ['Go to Jail/Just Visiting'],
        '11': ['St. Charles Place', 140],
        '12': ['Electric Company', 150],
        '13': ['States Avenue', 140],
        '14': ['Virginia Avenue', 160],
        '15': ['Pennsylvania Railroad', 200],
        '16': ['St. James Place', 180],
        '17': ['Community Chest'],
        '18': ['Tennessee Avenue', 180],
        '19': ['New York Avenue', 200],
        '20': ['Free Parking'],
        '21': ['Kentucky Avenue', 220],
        '22': ['Chance'],
        '23': ['Indiana Avenue', 220],
        '24': ['Illinois Avenue', 240],
        '25': ['B & O Railroad', 200],
        '26': ['Atlantic Avenue', 260],
        '27': ['Ventnor Avenue', 260],
        '28': ['Water Works', 150],
        '29': ['Marvin Gardens', 280],
        '30': ['Go to Jail'],
        '31': ['Pacific Avenue', 300],
        '32': ['North Carolina Avenue', 300],
        '33': ['Community Chest'],
        '34': ['Pennsylvania Avenue', 320],
        '35': ['Short Line', 200],
        '36': ['Chance'],
        '37': ['Park Place', 350],
        '38': ['Luxury Tax', 100],
        '39': ['Boardwalk', 400]
        }

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
        If owned, pay wonder twice the rental to which they are otherwise entitled',
        'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. \
        If owned, pay wonder twice the rental to which they are otherwise entitled',
        'Advance token to nearest Utility. If unowned, you may buy it from the Bank. \
        If owned, throw dice and pay owner a total ten times amount thrown.',
        'Bank pays you dividend of $50',
        'Get Out of Jail Free',
        'Go Back 3 Spaces',
        'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200',
        'Make general repairs on all your property. For each house pay $25. For each hotel pay $100',
        'Speeding fine $15',
        'Take a trip to Reading Railroad. If you pass Go, collect $200',
        'You have been elected Chairman of the Board. Pay each player $50',
        'Your building loan matures. Collect $150'
        ]


# class map(object):
#     row = 10
#     sides = 4
#     def __init__(self, colors):
#         self.

class Die(object):
    def __init__(self):
        self.roll_history = []

    def __str__(self):
        return f"Roll: {self.roll_history[-1]}"

    def roll(self, n = 2):
        value = 0
        for i in range(n):
            roll = random.randint(1, 6)
            value += roll
        # value = random.randint(1, 6)
        self.roll_history.append(value)

        return value

# class

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
                running = False
        screen.fill(color['white'])
        pygame.display.flip()

    return


if __name__ == '__main__':
    # pygame.init()
    # Run()
    # pygame.quit()
    dice = Die()
    for i in range(9):
        print(dice.roll())
