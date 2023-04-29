# main.py
import random
import math
from time import sleep


class TreeNode:
  #X goes first
  def __init__(self,board,player):
    self.board=board
    self.player=player
    self.children=[]
    self.score = 0
    self.best_child = None
    
  def addChild(self,child):
    self.children.append(child)
  
  def printBoard(self):
    print('\033c')

    for i in range(3):
      for j in range(3):
        state=self.board[i][j]
        if state==False:
          state=' '
        if j==2:
          print(' '+state,end='')
        else:
          print(' '+state+' |',end='')
      if i==2:
        pass
      else:
        print('\n---+---+---')
    print()
  
  def checkWin(self):
    #Win check
    for i in range(len(self.board)):
    #Verical Win
      if self.board[0][i]==self.board[1][i]==self.board[2][i] and self.board[0][i]!=False:
        return(self.board[0][i],True)
    #Horizontal Win
      if self.board[i][0]==self.board[i][1]==self.board[i][2] and self.board[i][0] != False:
        return(self.board[i][0],True)
    #diagonal win
      if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][0]!=False:
        return(self.board[0][0],True)
      elif self.board[2][0]==self.board[1][1]==self.board[0][2] and self.board[2][0]!=False:
        return(self.board[2][0],True)
  
    for i in self.board:
      for j in i:
        if j==False:
          #none
          return('none',False)
    #draw
    return('draw',True)
    
  #return (none,False), (X,True), (draw,True), and (O,True)  




  def set_bestchild(self):
    player,over=self.checkWin()
    if over and player=='O':
      self.score=1
      self.best_child=None
      return
    elif over and player=='X':
      self.score=-1
      self.best_child=None
      return
    elif over and player=='draw':
      self.score=0
      self.best_child=None
      return
      
    for n in self.children:
      n.set_bestchild()

    bestChild=None
    if self.player=='X':
      best=math.inf
      for n in self.children:
        if n.score < best:
          best=n.score
          bestChild=n
    elif self.player=='O':
      best=-math.inf
      for n in self.children:
        if n.score > best:
          best=n.score
          bestChild=n
          
    self.best_child=bestChild
    self.score=best

        
class Tree:
  def __init__(self,root):
    self.root=root
    self.buildTree(root)
    root.set_bestchild()
  def copyBoard(self,board):
    boardCopy=[]
  
    for row in board:
      lst=[]
      for item in row:
        lst.append(item)
      boardCopy.append(lst)
    return(boardCopy)

  

  def buildTree(self,node):
    if node.checkWin()[1]:
      return()
        
    childPlayer=''
    if node.player=='X':
      childPlayer='O'
    else:
      childPlayer='X'
      
    for i in range(len(node.board)):
      for j in range(len(node.board[i])):
        if not node.board[i][j]:
          boardCopy=self.copyBoard(node.board)
          boardCopy[i][j]=node.player
          treeNode=TreeNode(boardCopy,childPlayer)
          node.addChild(treeNode)

    for n in node.children:
      self.buildTree(n)
          
    
    

  
  def playGame(self):
    turn=True#True is player, False is computer
    print('Welcome to Tic-Tac-Toe.')
    node=self.root
    node.printBoard()
    while True:
      if turn:
        while True:
          row=int(input('Row: '))
          column=int(input('Column: '))
          if row>2 or row<0 or column>2 or column<0 or node.board[row][column]!=False:
            print('Enter a valid row and column')
          else:
            break
        for n in node.children:
          if n.board[row][column]==node.player:
            node=n
            break
      else:
        node=node.best_child
      print()
      node.printBoard()

      winner,over=node.checkWin()
      if over:
        break

      turn = not turn

    if winner=='X':
      print('X won')
    elif winner=='O':
      print('O won')
    else:
      print('Tie')
    '''
    1.Welcome player
    2.Make root
    3.Print board
    4.User input
      4a.Validate input
      4b.Place input
      4c.Change to matching child
      4d.Check win
    5.AI input
      5a.Random
      5b-5d.Same as user input
    '''

    


root=TreeNode([[False,False,False],[False,False,False],[False,False,False]],'X')
game=Tree(root)
while True:
  game.playGame()
  sleep(5)
