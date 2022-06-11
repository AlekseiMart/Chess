from tkinter import *
from PIL import Image,ImageTk

class Piece():
    def __init__(self,color,name,location):
        self.color = color
        self.name = name
        self.photo = ''
        self.location = location
        self.possible_moves = []
    def __str__(self):
        return "Color: " + self.color + " name: " + self.name + " photo: " + self.photo + " location: " + self.location

    def draw(self):
        if self.name == 'pawn': 
            self.photo = 'images/' + self.color + 'pawn.png'
        elif self.name == 'knight': 
            self.photo = 'images/' + self.color + 'knight.png'
        elif self.name == 'rook': 
            self.photo = 'images/' + self.color + 'rook.png'
        elif self.name == 'bishop': 
            self.photo = 'images/' + self.color + 'bishop.png'
        elif self.name == 'queen': 
            self.photo = 'images/' + self.color + 'queen.png'
        elif self.name == 'king': 
            self.photo = 'images/' + self.color + 'king.png'
        else:
            return "Error: Could not find photo"
        print(self.photo)
    
    def possibleMoves(self, checker_board):
        v = -1
        if(self.color == 'w'):
            v = 1
        if self.name == 'pawn': 
            print(a)
        elif self.name == 'knight': 
            # two forward one left
            loc = str(int(self.location[0])+2) + chr(ord(self.location[1])-1)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])+2) + chr(ord(self.location[1])-1))
            # two forward one right
            loc = str(int(self.location[0])+2) + chr(ord(self.location[1])+1)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])+2) + chr(ord(self.location[1])+1))
            # two backward one left
            loc = str(int(self.location[0])-2) + chr(ord(self.location[1])-1)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])-2) + chr(ord(self.location[1])-1))
            # two backward one right
            loc = str(int(self.location[0])-2) + chr(ord(self.location[1])+1)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])-2) + chr(ord(self.location[1])+1))
            # two left one forward
            loc = str(int(self.location[0])+1) + chr(ord(self.location[1])-2)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])+1) + chr(ord(self.location[1])-2))
            # two left one backward
            loc = str(int(self.location[0])-1) + chr(ord(self.location[1])-2)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])-1) + chr(ord(self.location[1])-2))
            # two right one forward
            loc = str(int(self.location[0])+1) + chr(ord(self.location[1])+2)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])+1) + chr(ord(self.location[1])+2))
            # two right one backward
            loc = str(int(self.location[0])-2) + chr(ord(self.location[1])+2)
            if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        return
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
            #self.possible_moves.append(str(int(self.location[0])-2) + chr(ord(self.location[1])+2))
            
        elif self.name == 'rook': 
            #forward moves
            for i in range(1,7):
                loc = self.location[0] + chr(ord(self.location[1])+i)
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            #backward moves
            for i in range(1,7):
                loc = self.location[0] + chr(ord(self.location[1])-i)
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            #left moves
            for i in range(1,7):
                loc = str(int(self.location[0])-i) + self.location[1]
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            #right moves
            for i in range(1,7):
                loc = str(int(self.location[0])+i) + self.location[1]
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            
        elif self.name == 'bishop': 
            #upright moves
            for i in range(1, 7):
                loc = str(int(self.location[0])+1) + chr(ord(self.location[1])+1)
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            #upleft moves
            for i in range(1, 7):
                loc = str(int(self.location[0])+1) + chr(ord(self.location[1])-1)
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            #downright moves
            for i in range(1, 7):
                loc = str(int(self.location[0])-1) + chr(ord(self.location[1])+1)
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            #downleft moves
            for i in range(1, 7):
                loc = str(int(self.location[0])-1) + chr(ord(self.location[1])-1)
                if loc in checker_board:
                    if(checker_board[loc] == "NONE"):
                        self.possible_moves.append(loc)
                    elif(checker_board[loc].color == self.color):
                        break
                    elif(checker_board[loc].color != self.color):
                        self.possible_moves.append(loc)
                        break
            
        elif self.name == 'queen': 
            self.photo = 'image/' + self.color + 'queen.png'
        elif self.name == 'king': 
            self.photo = 'image/' + self.color + 'king.png'
    
    



class Chess():
    def __init__(self):
        self.window = Tk()
        self.checkers = {}
        self.white_pieces = []
        self.black_pieces = []
        
    def createCheckerBoard(self):
        self.window.title("Chess")
        self.window.resizable(width=False, height=False)
        checker_size = 90
        width = checker_size * 10
        height = checker_size * 8
        w = Canvas(self.window, width=width, height=height)
        for i in range(0,8):
            for j in range(0,8):
                if (i + j) % 2  == 0:
                    w.create_rectangle(i*checker_size, j*checker_size, (i+1)*checker_size, (j+1)*checker_size, fill="tan")
                else:
                    w.create_rectangle(i*checker_size, j*checker_size, (i+1)*checker_size, (j+1)*checker_size, fill="grey")
                self.checkers[str(i+1)+chr(j+97)] = 'NONE'
        self.createPieces()
        j = 0
        imgs = []
        for i in self.checkers:
            if(self.checkers[i] != 'NONE'):
                imgs.append(ImageTk.PhotoImage(Image.open(self.checkers[i].photo).resize((80,80))))
                x = (ord(self.checkers[i].location[1])-97)
                y = int(self.checkers[i].location[0])-1
                w.create_image(x*90+5,y*90+5,anchor=NW,image=imgs[j])
                j +=1
        w.pack()       
        w.mainloop()

    def createPieces(self):
        self.white_pieces.append(Piece('b','pawn', '2a'))
        self.white_pieces.append(Piece('b','pawn', '2b'))
        self.white_pieces.append(Piece('b','pawn', '2c'))
        self.white_pieces.append(Piece('b','pawn', '2d'))
        self.white_pieces.append(Piece('b','pawn', '2e'))
        self.white_pieces.append(Piece('b','pawn', '2f'))
        self.white_pieces.append(Piece('b','pawn', '2g'))
        self.white_pieces.append(Piece('b','pawn', '2h'))

        self.black_pieces.append(Piece('w','pawn', '7a'))
        self.black_pieces.append(Piece('w','pawn', '7b'))
        self.black_pieces.append(Piece('w','pawn', '7c'))
        self.black_pieces.append(Piece('w','pawn', '7d'))
        self.black_pieces.append(Piece('w','pawn', '7e'))
        self.black_pieces.append(Piece('w','pawn', '7f'))
        self.black_pieces.append(Piece('w','pawn', '7g'))
        self.black_pieces.append(Piece('w','pawn', '7h'))

        self.white_pieces.append(Piece('b','rook', '1a'))
        self.white_pieces.append(Piece('b','rook', '1h'))
        self.white_pieces.append(Piece('b','bishop', '1c'))
        self.white_pieces.append(Piece('b','bishop', '1f'))
        self.white_pieces.append(Piece('b','knight', '1b'))
        self.white_pieces.append(Piece('b','knight', '1g'))
        self.white_pieces.append(Piece('b','king', '1e'))
        self.white_pieces.append(Piece('b','queen', '1d'))

        self.black_pieces.append(Piece('w','rook', '8a'))
        self.black_pieces.append(Piece('w','rook', '8h'))
        self.black_pieces.append(Piece('w','bishop', '8c'))
        self.black_pieces.append(Piece('w','bishop', '8f'))
        self.black_pieces.append(Piece('w','knight', '8b'))
        self.black_pieces.append(Piece('w','knight', '8g'))
        self.black_pieces.append(Piece('w','king', '8e'))
        self.black_pieces.append(Piece('w','queen', '8d'))
        for i in self.white_pieces:
            self.checkers[i.location] = i
            i.draw()
        for i in self.black_pieces:
            self.checkers[i.location] = i
            i.draw()
    
    def calcMoves(self):
        self.black_pieces[8].possibleMoves(self.checkers)
        print(self.black_pieces[8])
        move_list = self.black_pieces[8].possible_moves
        #removes all possible moves outside the boundary
        move_list = [x for x in move_list if int(x[:-1]) < 9 and int(x[:-1]) > 0 and ord(x[-1]) > 96 and ord(x[-1]) < 105]
        print(move_list)


        




def main():
    chess = Chess()
    chess.createCheckerBoard()
    chess.calcMoves()


if __name__ == '__main__':
    main()