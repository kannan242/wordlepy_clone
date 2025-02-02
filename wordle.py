import random, pygame, sys
from pygame.locals import *
pygame.init()

white = (255,255,255)
yellow = (255,255,102)
green =(0,255,0)
grey = (211,211,211)
black = (0,0,0)
green = (0,255,0)
lightGreen = (153,255,204)

font = pygame.font.SysFont("Helvetica neue",35)
bigFont = pygame.font.SysFont("Helvetica neue",50)

youWin = bigFont.render("You won, mate!",  True, lightGreen)
youLose = bigFont.render("Sorry You lose!, Try Again.",  True, lightGreen)
playAgain = bigFont.render("Can you Play Again?",  True, lightGreen)

def checkGuess(turns, word, userGuess, window):
    renderList =["","","","",""]
    space = 0
    guessColourCode = [grey,grey,grey,grey,grey]

    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = yellow

        if word[x] == userGuess[x]:
            guessColourCode[x] = green

    list(userGuess)

    for x in range(0,5):
        print(renderList[x])
        renderList[x] = font.render(userGuess[x], True, black)
        pygame.draw.rect(window, guessColourCode[x], pygame.Rect(60 +space, 50+ (turns*80), 50, 50))
        window.blit(renderList[x], (70 + space, 50 + (turns*80)))
        space+=80

    if guessColourCode == [green,green,green,green,green]:
        return True


def main():
    file = open("5-letters-w-purushoth.txt","r")
    wordList = file.readlines()
    word = wordList[random.randint(0, len(wordList)-1)].upper()
    height = 600
    width = 500
    FPS = 30
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""
    print(word)

    for x in range(0,5):
        for y in range(0,5):
            pygame.draw.rect(window, grey, pygame.Rect(60+(x*80), 50+(y*80), 50, 50),2)

    pygame.display.set_caption("WORDLE_CLONE -for edu purpose!")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                guess+=event.unicode.upper()

                if event.key == K_RETURN and  win == 6:
                    main()

                if event.key == K_RETURN and  turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]

                if event.key == K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, word, guess, window)
                    turns+=1
                    guess = ""
                    window.fill(black,(0,500,500,200))

        window.fill(black,(0,500,500,200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.blit(youWin,(90, 200))
            window.blit(playAgain,(60, 300))

        if turns == 6 and win != True:
            window.blit(youLose,(90, 200))
            window.blit(playAgain,(60, 300))
        pygame.display.update()
        clock.tick(FPS)
main()
             
    

    
