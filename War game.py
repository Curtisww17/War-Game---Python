#   Wesley Curtis              _
 #   Adam Cramer            _ooOoo_
  #                        o8888888o
   #                       88" . "88
    #     War Game         (| -_- |)
     #                     O\  =  /O
      #                 ____/`---'\____
       #              .'  \\|     |//  `.
        #            /  \\|||  :  |||//  \   WESLEY IS A LOSERR
         #          /  _||||| -:- |||||_  \
        #           |   | \\\  -  /'| |   |
       #            | \_|  `\`---'//  |_/ | nIDiot
      #             \  .-\__ `-. -'__/-.  /
     #            ___`. .'  /--.--\  `. .'___
    #          ."" '<  `.___\_<|>_/___.' _> \"".
   #          | | :  `- \`. ;`. _/; .'/ /  .' ; |
  #           \  \ `-.   \_\_`. _.'_/_/  -' _.' /
 #  ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
#                           `=--=-'
#                  Buddah Bless The Code
import pygame, sys, random
from pygame.locals import *
#Note card image files are labeled by value from 1 to 13 and first letter of suit (jack of clubs is 11c)


def init():
    global textBox, textRect, hand, deck, window, font, back
    pygame.init()
    window = pygame.display.set_mode((800,600))
    pygame.display.set_caption('War!')
    font = pygame.font.SysFont('broadway', 38, True)
    back = pygame.image.load("back.png")
    back = pygame.transform.scale(back, (148,200))
    hand = Hand()
    deck = Deck()
    random.shuffle(deck.cards)
    window.fill((0,160,0))
    textBox = font.render('WAR!',True, (255,255,255))
    textRect = textBox.get_rect()
    textRect.center = (400,100)

def display():
    window.fill((0,160,0))
    window.blit(textBox,textRect)
    window.blit(hand.player[-1].img(), (126,200))
    window.blit(hand.comp[-1].img(), (526,200))



#This class creates a card object, each with a value and suit.
#Programmer can use the img() method to return the image of the card
class Card(object):
    def __init__(self, val, suit):
        self.value = val
        self.suit = suit
        self.cardname = str(self.value) + self.suit + ".png"
        #self.face = pygame.image.load("%s" % self.cardname) #two different ways to do the same thing
        self.face = pygame.image.load("{}".format(self.cardname))
        self.face = pygame.transform.scale(self.face, (148,200))

    def img(self): #retuns image of card

        return self.face



#The deck class creates a list of cards, which creates 52 cards (in construct())
#
class Deck(object):
    def __init__(self):
        self.cards = []
        self.construct()

    def construct(self):
        for suit in ['c','d','h','s']:
            for value in range(1,14):
                newcard = Card(value, suit)
                self.cards.append(newcard)

    def cut(self): #Totally unnessesary but here anyways (would split deck into 2 hands)
        Hand.player = self.cards[:len(self.cards)/2]
        Hand.comp = self.cards[len(self.cards)/2:]


class Hand(object):
    def __init__(self):
        self.player = [] # CHANGE THESE TO VARS
        self.comp = []

    def draw(self, var):
        if var == "player":
            self.player.append(deck.cards[-1]) #adds last card in list cards to list player
            deck.cards.pop()#Removes last card in list
        if var == "comp":
            self.comp.append(deck.cards[-1]) #adds last card in list cards to list comp
            deck.cards.pop()

class score(object): #Used to score the hand and store curent scores
    def __init__(self):
        self.pScore = 0
        self.cScore = 0

    def score(pCard, cCard): #accepts filename of player and computer cards
        pVal = int(pCard[0]) #takes the number from start of card name (suit doesnt matter)
        cVal = int(cCard[0])
        if pVal > cVal and cVal != 1: #checks for player win
            self.pScore += 1
        else if cVal > pVal and pVal != 1: #checks for computer win
            self.cScore += 1
        else if pVal == 1: #checks for player win by an ace
            self.pScore += 1
        else if cVal == 1:
            self.cScore += 1
        else if cVal == pVal:
            #need to call a WAR! class here



init() #starts E V E R Y T H I N G


while True:
    if len(hand.player) > 0 and len(hand.comp) > 0:
        display()

    if len(hand.player) < 26:
        window.blit(textBox,textRect)
        window.blit(back,(126,400))
        window.blit(back,(526,400))
    else:
        display()
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP: #run next turn
            hand.draw('comp')
            hand.draw('player')
            #mousex,mousey = event.pos
    pygame.display.update()
##
