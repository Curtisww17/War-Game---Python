#   Wesley Curtis              _
 #   Adam Cramer            _ooOoo_
  #                        o8888888o
   #                       88" . "88
    #     War Game         (| -_- |)
     #                     O\  =  /O
      #                 ____/`---'\____
       #              .'  \\|     |//  `.
        #            /  \\|||  :  |||//  \
         #          /  _||||| -:- |||||_  \
        #           |   | \\\  -  /'| |   |
       #            | \_|  `\`---'//  |_/ |
      #             \  .-\__ `-. -'__/-.  /
     #            ___`. .'  /--.--\  `. .'___
    #          ."" '<  `.___\_<|>_/___.' _> \"".
   #          | | :  `- \`. ;`. _/; .'/ /  .' ; |
  #           \  \ `-.   \_\_`. _.'_/_/  -' _.' /
 #  ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
#                           `=--=-'
#                  Buddah Bless The Code
import pygame, sys, random, time, math
from pygame.locals import *
#Note card image files are labeled by value from 1 to 13 and first letter of suit (jack of clubs is 11c)


def init():
    global textBox, textRect, hand, deck, window, font, back, score, counter, counter2, warchecker
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
    score = score()
    counter = 0
    counter2 = 0
    warchecker = False



def display():
        window.fill((0,160,0))
        window.blit(textBox,textRect)
        if hand.player != None and hand.comp != None:
            window.blit(hand.player.img(), (126,200))
            window.blit(hand.comp.img(), (526,200))



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
        self.player = None # CHANGE THESE TO VARS
        self.comp = None

    def draw(self, var):
        if var == "player":
            self.player = deck.cards[-1] #adds last card in list cards to list player
            deck.cards.pop()#Removes last card in list
        if var == "comp":
            self.comp = deck.cards[-1] #adds last card in list cards to list comp
            deck.cards.pop()

class score(object): #Used to score the hand and store curent scores
    def __init__(self):
        self.pScore = 0
        self.cScore = 0

    def score(self, pCard, cCard, inc): #accepts the player's and computer's cards as well a the amount
                                        #of points it is scoring for, to account for a war
        if hand.player != None and hand.comp != None:
            if hand.player.value > hand.comp.value and hand.comp.value != 1: #checks for player win
                self.pScore += inc
            elif hand.comp.value > hand.player.value and hand.player.value != 1: #checks for computer win
                self.cScore += inc
            elif hand.player.value == 1 and hand.comp.value != 1: #checks for player win by an ace
                self.pScore += inc
            elif hand.comp.value == 1 and hand.player.value != 1:
                self.cScore += inc
            elif hand.comp.value == hand.player.value:
                if len(deck.cards) > 0:
                    war()


def end():
    pass

def war():
    warchecker = True
    if len(deck.cards) >= 8:
        upper = 7
    else:
        upper = len(deck.cards)-1
        
    for i in range(1, math.ceil(upper/2)):
        deck.cards.pop(-i)
        deck.cards.pop(-(i+1))
        
        window.blit(back, (126, 250 + (50* i)))
        window.blit(back, (526, 250 + (50* i)))
        time.sleep(.5)
        pygame.display.update()

    hand.draw('comp')
    hand.draw('player')
    window.blit(hand.player.img(), (126,300 + (50* i)))
    window.blit(hand.comp.img(), (526,300 + (50 * i)))
    time.sleep(.5)
    pygame.display.update()
    score.score(hand.player,hand.comp,6)
    time.sleep(1)
    
    



init()#starts EVERYTHING
while True:
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP: #run next turn

            if len(deck.cards) > 0:
                hand.draw('comp')
                hand.draw('player')
                counter += 1
                counter2 = 0
            else:
                end()
    if warchecker == False:
        display()
    
    if counter == counter2:
        score.score(hand.player,hand.comp,1)
        warchecker = False
        print(score.pScore, score.cScore) #debug for score() class
        print(len(deck.cards))
    pygame.display.update()
    counter2 += 1
