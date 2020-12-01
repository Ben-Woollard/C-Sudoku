import pygame
import random
from GenerateSudokuSolution import Grid as Grid
import GenerateSudokuSolution
pygame.init()
displayHeight = 700
displayWidth = 1360
displayGame = pygame.display.set_mode((displayWidth, displayHeight))
grey = (195,195,195)
FONT = pygame.font.Font(None, 78)
grid = pygame.image.load('grid.png')
newGameButton = pygame.image.load('NewGameButton.png')
checkGridButton = pygame.image.load('CheckGridButton.png')
correctText = pygame.image.load('Correct.png')
incorrectText = pygame.image.load('Incorrect.png')
colourInactive = (0,0,0)
colourActive = pygame.Color('dodgerblue2')
NUMBERS = ['1','2','3','4','5','6','7','8','9']
class InputBox():#Change because copied

    def __init__(self, xPos, yPos, width, height, startingSquare, text=''):
        self.rect = pygame.Rect(xPos, yPos, width, height)
        self.colour = colourInactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.colour)
        self.active = False
        self.lineWidth = 2
        self.startingSquare = startingSquare
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                if self.startingSquare:
                    print("Yay")
            else:
                self.active = False
            # Change the current colour of the input box.
            self.colour = colourActive if self.active else colourInactive
            self.lineWidth = 6 if self.active else 2
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.text == '' and event.unicode in NUMBERS:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, (0,0,0), "center")

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, self.lineWidth)
def generateBlankPuzzle(gameGrid):
    newGameGrid = gameGrid[:]
    for i in range(9):
        numbersLeft = random.randint(3, 5)
        for j in range(9):
            showNumber = random.randint(0,1)
            if j > 0:
                if newGameGrid[i][j - 1].startingSquare == True:
                    showNumber = random.randint(0,1)
                elif j > 1 and newGameGrid[i][j - 2].startingSquare == True:
                    showNumber = 1
            if showNumber == 1 and numbersLeft > 0:
                newGameGrid[i][j].startingSquare = True
                numbersLeft -= 1
    return newGameGrid

def setupGame():
    inputBoxes = []
    griddy = Grid()
    gameGrid = griddy.generateGrid()
    newGameGrid = generateBlankPuzzle(gameGrid)
    for i in range(9):
        for j in range(9):
            if newGameGrid[i][j].startingSquare == True:
                text = str(newGameGrid[i][j].number)
            else:
                text = ''
                colour = (1,1,1)
            inputBoxes.append(InputBox(350 + (j*71.9), 20 + (i*71.9), 72.5, 72.5, newGameGrid[i][j].startingSquare, text))
    checked = False
    return inputBoxes, newGameGrid, checked

def checkGame(inputBoxes, gameGrid):
    indexCounter = 0
    checkCounter = 0
    print(len(inputBoxes))
    for i in range(9):
        for j in range(9):
            if inputBoxes[indexCounter].text == str(gameGrid[i][j].number):
                checkCounter += 1
            indexCounter += 1
            print(indexCounter)
    print(checkCounter)
    if checkCounter == 81:
        return True
    else:
        return False
    
def main():
    clock = pygame.time.Clock()
    inputBoxes, gameGrid, checked = setupGame()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and 177 > mouse[0] > 10 and 73 > mouse[1] > 30:
                inputBoxes, gameGrid, checked = setupGame()
            elif event.type == pygame.MOUSEBUTTONDOWN and 177 > mouse[0] > 10 and 133 > mouse[1] > 90:
                wonGame = checkGame(inputBoxes, gameGrid)
                checked = True
            else:
                for box in inputBoxes:
                    if box.startingSquare == False:
                        box.handle_event(event)
        displayGame.fill(grey)
        if checked:
            if wonGame:
                displayGame.blit(correctText, (10,140))
            else:
                displayGame.blit(incorrectText, (10,140))
        displayGame.blit(grid, (350, 20))
        displayGame.blit(newGameButton, (10, 30))
        displayGame.blit(checkGridButton, (10, 90))
        mouse = pygame.mouse.get_pos()
        for box in inputBoxes:
            box.draw(displayGame)
        
        pygame.display.update()
        clock.tick(60)
if __name__ == '__main__':
    main()
    pygame.quit()
