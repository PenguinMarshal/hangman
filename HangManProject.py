# Import the necessary libraries
import pygame, sys, random
from pygame.locals import *

# Set the Frames Per Second (FPS) to 30
fps = 30
# Initialize Pygame
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
# Create a clock object to control the FPS
clock = pygame.time.Clock()

# Set the width and height of the game window
width = 800
height = 600

# Define various colors used in the game
orange = (255, 165, 0)
black = (0,0,0)
white = (255,255,255)
grey= (128,128,128)
darkgrey = (128,128,128)
lightblue = (126,178,255)
darklightblue = (42, 129, 255)
lightgrey = (192, 192, 192)

# Define variables related to text box positioning
textBoxSpace = 5
textBoxNumber = 0

# Set the initial score to 0
score = 0

# Function to display the current score on the game screen
def draw_score():
    # Set the font and size
    font = pygame.font.Font("freesansbold.ttf", 20)
    # Render the score text
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    # Draw the score text on the screen
    screen.blit(score_text, (10, 10))

# Function to start the hangman game with 'animal' category
def Animals():
    # Set the list of words for 'animal' category
    animal = ['cow','dog','cat','pig','zebra','bird','giraffe','lion','tiger','penguin','hamster','fox','panda','bear','cheetah','ostrich','meerkat','whale','shark','horse','monkey','octopus','kitten','kangaroo','chicken','fish','rabbit','sheep']
    # Print 'animal' to the console (This line seems unnecessary for the game and can be removed)
    print("animal")
    title = "Animals"
    # Start the hangman game with 'animal' category
    hangmanGame(animal,title)

def Vehicles():
    vehicle = ['car','bus','train','airplane','plane','ship','jet','boat','lorry','tractor','bike','motorbike','tram','van','ambulance','fire engine','rocket','taxi','caravan','coach','lorry','scooter','sleigh','tank','wagon','spaceship']
    print("vehicle")
    title = "Vehicles"
    hangmanGame(vehicle,title)

def Foods():
    food = ['apple','banana','orange','peach','pizza','donut','chips','sandwich','cookie','cucumber','carrot','sweetcorn','ice cream','pancake','bread','potato','tomato','nuts','yogurt','pasta','rice','cheese','soup','fish','egg','meat','ham','sausage']
    print("food")
    title = "Foods"
    hangmanGame(food,title)

def Sports():
    sport = ['rugby','football','netball','basketball','swimming','hockey','curling','running','golf','tennis','badminton','archery','volleyball','bowling','dancing','gym','skating','baseball','rounders','boxing','climbing','canoe','cycling','fencing','karate','shooting','cricket']
    print("sport")
    title = "Sports"
    hangmanGame(sport,title)

def button(word, x, y, w, h, ic, ac, action=None):
    # Get the current mouse position
    mouse = pygame.mouse.get_pos()
    # Get the current mouse button state
    click = pygame.mouse.get_pressed()

    # Check if the mouse is within the button's boundaries
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # Draw the button in the active color
        pygame.draw.rect(screen, ac, (x, y, w, h))
        # Check if the button is clicked and perform the specified action
        if click[0] == 1 and action is not None:
            action()
    else:
        # Draw the button in the inactive color
        pygame.draw.rect(screen, ic, (x, y, w, h))

    # Render the button text
    buttonText = pygame.font.Font("freesansbold.ttf", 15)
    buttonTextSurf = buttonText.render(word, True, white)
    buttonTextRect = buttonTextSurf.get_rect()
    buttonTextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(buttonTextSurf, buttonTextRect)

def endGame():
    # Declare the global variables to modify them
    global textBoxSpace, textBoxNumber
    textBoxSpace = 5
    textBoxNumber = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)  # Fill the screen with white to remove previous contents

        # Render "Final Score"
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf = largeText.render("Final Score: %s" % score, True, darkgrey)
        TextRect = TextSurf.get_rect()
        TextRect.center = (width / 2, height / 2 - 50)
        screen.blit(TextSurf, TextRect)

        # Render "Would you like to play again?"
        largeText = pygame.font.SysFont("comicsansms", 50)
        TextSurf = largeText.render("Would you like to play again?", True, darkgrey)
        TextRect = TextSurf.get_rect()
        TextRect.center = (width / 2, height / 2)
        screen.blit(TextSurf, TextRect)

        # Increase the width and height of the buttons
        buttonWidth = 100
        buttonHeight = 50
        button("Yes",width/2-buttonWidth-50,height/2+100,buttonWidth,buttonHeight,darkgrey,grey,hangman)
        button("No",width/2+50,height/2+100,buttonWidth,buttonHeight,darkgrey,grey,quitGame)

        pygame.display.update()

def game_over_screen(pick):
    # Set a new background color
    screen.fill(lightblue)

    # Render "Incorrect word."
    largeText = pygame.font.SysFont("comicsansms", 50)
    TextSurf = largeText.render("Incorrect word.", True, black)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((width / 2), (height / 2 - 50))
    screen.blit(TextSurf, TextRect)

    # Render the correct word
    revealText = pygame.font.SysFont("comicsansms", 30)
    revealSurf = revealText.render(f"The correct word was: {pick}", True, black)
    revealRect = revealSurf.get_rect()
    revealRect.center = ((width / 2), (height / 2 + 30))
    screen.blit(revealSurf, revealRect)

    pygame.display.update()
    pygame.time.wait(3000)

# Function to exit the game
def quitGame():
    pygame.quit()
    sys.exit()

# Function to unpause the game
def unpause():
    global pause
    pause = False

# Function to create text objects for Pygame
def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Main function to start the game
def main():
    global  screen, play
    play = True
    screen = pygame.display.set_mode((width, height))
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Welcome to Hangman Game!")
    while True:
        hangman()

# Function to place guessed letter on the screen
def placeLetter(letter):
    global pick, pickSplit
    space = 10
    wordSpace = 0
    while wordSpace < len(pick):
        text = pygame.font.Font('freesansbold.ttf',40)
        if letter in pickSplit[wordSpace]:
            textSurf = text.render(letter,True,black)
            textRect = textSurf.get_rect()
            textRect.center = (((150)+space),(200))
            screen.blit(textSurf, textRect)
        wordSpace += 1
        space += 60
    pygame.display.update()

# Function to display guessed letters in a text box
def textBoxLetter(letter):
    global textBoxSpace, textBoxNumber
    if textBoxNumber <= 5:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(350))
        screen.blit(textSurf, textRect)
    elif textBoxNumber <= 10:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(400))
        screen.blit(textSurf, textRect)
    pygame.display.update()

# Function for the hangman game loop
def hangman():
    global textBoxSpace, textBoxNumber
    textBoxSpace = 5
    textBoxNumber = 0
    light_green = (144, 238, 144)  # Define light green color

    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
        screen.fill(light_green)  # Change the fill color to light green
        space = 10
        textBoxSpace = 5
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render("Select a category",True,black)
        textRect = textSurf.get_rect()
        textRect.center = ((width/2),(height/2))
        screen.blit(textSurf, textRect)
        button("Animals",150,450,150,100,orange,lightgrey,Animals)
        button("Vehicles",550,450,150,100,orange,lightgrey,Vehicles)
        button("Food",150,50,150,100,orange,lightgrey,Foods)
        button("Sports",550,50,150,100,orange,lightgrey,Sports)             
        pygame.display.update()

# Function to create buttons
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

# Function to create text objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Function for the game introduction screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Hangman", largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,lightblue,darklightblue,game_loop)
        button("Quit",550,450,100,50,grey,darkgrey,quitGame)

        pygame.display.update()
        clock.tick(15)

# Function for the main game loop
def game_loop():
    global play
    play = True
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
        screen.fill(white)
        hangman()

# Function for the main Hangman game logic
def hangmanGame(catagory,title):
    global score, pause, pick, pickSplit, textBoxSpace, textBoxNumber, start
    chances = 10
    pick = random.choice(catagory)
    pickSplit = [pick[i:i+1] for i in range(0, len(pick), 1)]
    screen.fill(white)
    draw_score()  # Draw the score at the beginning of each game
    wordSpace = 0
    space = 10
    while wordSpace < len(pick):
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf1 = text.render("_",True,black)
        textRect1 = textSurf1.get_rect()
        textRect1.center = (((150)+space),(200))
        screen.blit(textSurf1, textRect1)
        space = space + 60
        wordSpace += 1
    guesses = ''
    gamePlay = True
    while gamePlay == True:
        guessLett = ''

        if textBoxNumber == 5:
            textBoxSpace = 5
        if textBoxNumber == 10:
            textBoxSpace = 5
        if textBoxNumber == 15:
            textBoxSpace = 5

        pygame.draw.rect(screen, white, [550,20,200,20])
        text = pygame.font.Font("freesansbold.ttf",20)
        textSurf = text.render(("Chances: %s" % chances),False,black)
        textRect = textSurf.get_rect()
        textRect.topright = (700,20)
        screen.blit(textSurf, textRect)
        textTitle = pygame.font.Font("freesansbold.ttf",40)
        textTitleSurf = textTitle.render(title,True,black)
        textTitleRect = textTitleSurf.get_rect()
        textTitleRect.center = ((width/2),50)
        screen.blit(textTitleSurf, textTitleRect)
        pygame.draw.rect(screen, black, [100,300,250,250],2)
        if chances == 10: #base line
            pygame.draw.line(screen,black,[405,545],[650,545],10)
        elif chances == 9: #vertical line (big)
            pygame.draw.line(screen,black,[425,300],[425,545],10)
        elif chances == 8: #horizontal line
            pygame.draw.line(screen,black,[421,295],[550,295],10)
        elif chances == 7: #vertical line (small)
            pygame.draw.rect(screen,black,[550,291,10,60])
        elif chances == 6: #head
            pygame.draw.circle(screen,black,[555,380],30)
        elif chances == 5: #body
            pygame.draw.rect(screen,black,[550,410,10,80])
        elif chances == 4: #right arm
            pygame.draw.line(screen,black,[555,425],[570,455],10)
        elif chances == 3: #left arm
            pygame.draw.line(screen,black,[540,455],[555,425],10)
        elif chances == 2: #left leg
            pygame.draw.line(screen,black,[540,520],[553,490],10)
        elif chances == 1: #right leg
            pygame.draw.line(screen,black,[555,490],[570,520],10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()              
            if event.type == pygame.KEYDOWN:
                failed = 0
                print("Failed",failed)
                print("Chance", chances)        
                if event.key == pygame.K_SPACE:
                    pause()          
                if event.key == pygame.K_ESCAPE:
                    gamePlay = False           
                if event.key in range(97, 123):
                    guessLett = chr(event.key)
                    guesses += guessLett
                    print(f"Letter {guessLett} guessed")
                    print("")
                # check if letter is in word
                for char in pick:
                    if char in guesses:
                        print(char, end=" ")
                    else:
                        print("_", end=" ")
                        failed += 1
                print("")
                if guessLett in pick:
                    placeLetter(guessLett)                             
                if failed == 0:
                    print("You got the word")
                    print(pick)
                    score += 1 # Increase the score by 1
                    draw_score()  # Draw the updated score
                    endGame()
                if guessLett not in pick:
                    textBoxSpace += 40
                    textBoxNumber += 1
                    chances = chances - 1
                    print("")
                    print(textBoxNumber)
                    print("")
                    print("That letter is not in the word")
                    textBoxLetter(guessLett)
                if chances == 0:
                    game_over_screen(pick)
                    endGame()
                    pygame.display.update()
                    pygame.time.wait(3000)
                    
        pygame.display.update()
    pygame.display.update()

if __name__ == '__main__':
    main()