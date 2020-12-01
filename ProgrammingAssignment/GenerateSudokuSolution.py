import random

SUDOKU_NUMBERS = [1,2,3,4,5,6,7,8,9]
BOX_INDEX_GRID = [[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]],
                  [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]],
                  [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]],
                  [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]],
                  [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]],
                  [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]],
                  [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]],
                  [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]],
                  [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]]
class Square():
    def __init__(self, indexVal, number = 0, startingSquare = False):
        self.number = number
        self.startingSquare = startingSquare #do later
        
    def findBox(self, row, column):
        if row in [0, 1, 2]:
            whichBox = [0, 1, 2]
        elif row in [3, 4, 5]:
            whichBox = [3, 4, 5]
        else:
            whichBox = [6, 7, 8]

        if column in [0, 1, 2]:
            del(whichBox[1])
            del(whichBox[1])
        elif column in [3, 4, 5]:
            del(whichBox[0])
            del(whichBox[1])
        else:
            del(whichBox[0])
            del(whichBox[0])
        return whichBox[0]
    
    def fillSquare(self, row, column, gameGrid):
        self.number = 0
        availableNumbers = SUDOKU_NUMBERS[:]
        currentBox = BOX_INDEX_GRID[self.findBox(row, column)]
        for num in gameGrid[row]:
            num = num.number
            if num in availableNumbers:
                availableNumbers.remove(num)
        for gridRow in gameGrid:
            if gridRow[column].number in availableNumbers:
                availableNumbers.remove(gridRow[column].number)
        for i in range(len(currentBox)):
            if gameGrid[currentBox[i][0]][currentBox[i][1]].number in availableNumbers:
                availableNumbers.remove(gameGrid[currentBox[i][0]][currentBox[i][1]].number)
        self.number = availableNumbers[random.randint(0, len(availableNumbers) - 1)]
        

class Grid():
    def generateGrid(self):
        while True:
            try:
                gameGrid = []
                for i in range(9):
                    gameGrid.append([])
                    for j in range(9):
                        gameGrid[i].append(Square(j))
                for row in range(9):
                    for column in range(9):
                        gameGrid[row][column].fillSquare(row, column, gameGrid)
            except:
                continue
            break
        return gameGrid


