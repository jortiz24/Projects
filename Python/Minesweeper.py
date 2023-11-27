##529 Leetcode, Minesweeper solver
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

                m = len(board)
                n  = len(board[0])
                self.board = board
                self.click = click
                x = click[0]
                y = click[1]

                #print(self.board[x][y])

                ##print([self.board[x+2][2:5] for x in range(2)])
                
                if self.board[x][y] == 'E':
                       
                        bombs = 0
                        for a in range(x-1,x+2):
                                for b in range(y-1,y+2):
                                        if a >=0 and a <= m - 1 and b>= 0 and b <= n - 1:
                                        
                                                if self.board[a][b] == "M":
                                                        bombs += 1
                        print(bombs)
                        if bombs == 0:
                                self.board[x][y] = "B"
                                for a in range(x-1,x+2):
                                        for b in range(y-1,y+2):
                                                if a >=0 and a <= m - 1 and b>= 0 and b <= n - 1:
                                                        if self.board[a][b] == "E":
                                                                self.board[a][b] = (self.updateBoard(self.board,[a,b]))[a][b]
                        else:
                                
                                self.board[x][y] = "{}".format(bombs)


                if self.board[x][y] == 'M':
                        self.board[x][y] = 'X'
                        return self.board
                        
                return self.board
                                      
