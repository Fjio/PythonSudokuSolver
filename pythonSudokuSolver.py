# no OOP for now
# test grid per lines
"""
Input Sudoku testing grid
"""
testingGrid = [
[0,0,7,8,0,0,4,0,0],
[0,0,4,0,9,3,0,8,0],
[3,5,0,0,1,4,0,0,9],
[0,6,0,3,0,0,0,0,8],
[4,7,0,0,8,0,0,6,3],
[8,0,0,0,0,9,0,5,0],
[1,0,0,9,2,0,0,7,5],
[0,3,0,5,7,0,8,0,0],
[0,0,5,0,0,6,9,0,0]
]

def testValue(grid:list,i:int,j:int) -> list:
  """
  takes a grid and coordinates to find already used numbers
  """
  lFilled = [0,0,0,0,0,0,0,0,0,0]
  for lineInd in range(9):
    lFilled[grid[i][lineInd]]=1
  for rowInd in range(9):
      lFilled[grid[rowInd][j]]=1
  #squares of 3x3 hereafter
  rowStart,lineStart = i//3*3,j//3*3
  for lineInd in range(lineStart,lineStart + 3):
    for rowInd in range(rowStart,rowStart + 3):
      lFilled[grid[rowInd][lineInd]]=1
  return(lFilled)

def finalAlgorithm(grid) -> list:
  """
  runs testValue until everything is filled, with loop on whole matrix

  not at all optimal but pretty easy to implement
  """
  countZero=1
  while countZero!=0:  
    countBis=0
    for i in range(9):
      for j in range(9):
        if grid[i][j]==0:
          intList = testValue(grid,i,j)
          countBis+=intList[0]
          if sum(intList[1:])==8:
            grid[i][j]=intList[1:].index(0) + 1
    countZero=countBis
  return(grid)

"""
Running the algorithm and extracting the filled Sudoku

I'll create later an option to input a to-be-filled Sudoku Grid

For now the use directly in IDE is the most optimal way I found 

(Inputing the 81 values one by one sounds boring and not at all error-forgiving !)
"""
testingGridFilled = finalAlgorithm(testingGrid)
for i in range(9):
  print(testingGridFilled[i])