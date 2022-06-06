import tkinter as tk

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
            self.photo = 'image/' + self.color + 'pawn.png'
        elif self.name == 'knight': 
            self.photo = 'image/' + self.color + 'knight.png'
        elif self.name == 'rook': 
            self.photo = 'image/' + self.color + 'rook.png'
        elif self.name == 'bishop': 
            self.photo = 'image/' + self.color + 'bishop.png'
        elif self.name == 'queen': 
            self.photo = 'image/' + self.color + 'queen.png'
        elif self.name == 'king': 
            self.photo = 'image/' + self.color + 'king.png'
        else:
            return "Error: Could not find photo"
        print(self.photo)
    
    def possibleMoves(self):
        v = -1
        if(self.color == 'w'):
            v = 1
        if self.name == 'pawn': 
            self.possible_moves = []
        elif self.name == 'knight': 
            self.photo = 'image/' + self.color + 'knight.png'
        elif self.name == 'rook': 
            self.photo = 'image/' + self.color + 'rook.png'
        elif self.name == 'bishop': 
            self.photo = 'image/' + self.color + 'bishop.png'
        elif self.name == 'queen': 
            self.photo = 'image/' + self.color + 'queen.png'
        elif self.name == 'king': 
            self.photo = 'image/' + self.color + 'king.png'
    
    



class Chess():
    def __init__(self, window):
        self.window = window
        self.checkers = {}
        self.white_pieces = []
        self.black_pieces = []
        
    def createCheckerBoard(self):
        checker_size = 90
        width = checker_size * 10
        height = checker_size * 8
        w = tk.Canvas(self.window, width=width, height=height)
        for i in range(0,8):
            for j in range(0,8):
                if (i + j) % 2  == 0:
                    w.create_rectangle(i*checker_size, j*checker_size, (i+1)*checker_size, (j+1)*checker_size, fill="tan")
                else:
                    w.create_rectangle(i*checker_size, j*checker_size, (i+1)*checker_size, (j+1)*checker_size, fill="black")
                self.checkers[str(i+1)+chr(j+97)] = 'NONE'
        w.pack()


    def createPieces(self):
        self.white_pieces.append(Piece('w','pawn', '2a'))
        self.white_pieces.append(Piece('w','pawn', '2b'))
        self.white_pieces.append(Piece('w','pawn', '2c'))
        self.white_pieces.append(Piece('w','pawn', '2d'))
        self.white_pieces.append(Piece('w','pawn', '2e'))
        self.white_pieces.append(Piece('w','pawn', '2f'))
        self.white_pieces.append(Piece('w','pawn', '2g'))
        self.white_pieces.append(Piece('w','pawn', '2h'))

        self.black_pieces.append(Piece('b','pawn', '7a'))
        self.black_pieces.append(Piece('b','pawn', '7b'))
        self.black_pieces.append(Piece('b','pawn', '7c'))
        self.black_pieces.append(Piece('b','pawn', '7d'))
        self.black_pieces.append(Piece('b','pawn', '7e'))
        self.black_pieces.append(Piece('b','pawn', '7f'))
        self.black_pieces.append(Piece('b','pawn', '7g'))
        self.black_pieces.append(Piece('b','pawn', '7h'))

        self.white_pieces.append(Piece('w','rook', '1a'))
        self.white_pieces.append(Piece('w','rook', '1h'))
        self.white_pieces.append(Piece('w','bishop', '1c'))
        self.white_pieces.append(Piece('w','bishop', '1f'))
        self.white_pieces.append(Piece('w','knight', '1b'))
        self.white_pieces.append(Piece('w','knight', '1g'))
        self.white_pieces.append(Piece('w','king', '1e'))
        self.white_pieces.append(Piece('w','queen', '1d'))

        self.black_pieces.append(Piece('b','rook', '8a'))
        self.black_pieces.append(Piece('b','rook', '8h'))
        self.black_pieces.append(Piece('b','bishop', '8c'))
        self.black_pieces.append(Piece('b','bishop', '8f'))
        self.black_pieces.append(Piece('b','knight', '8b'))
        self.black_pieces.append(Piece('b','knight', '8g'))
        self.black_pieces.append(Piece('b','king', '8e'))
        self.black_pieces.append(Piece('b','queen', '8d'))
        for i in self.white_pieces:
            self.checkers[i.location] = i
            i.draw()
        for i in self.black_pieces:
            self.checkers[i.location] = i
            i.draw()
    
    def calcMoves(self):
        move_list = []


        




def main():

    window = tk.Tk()
    window.title("Chess")
    window.resizable(width=False, height=False)
    chess = Chess(window)
    chess.createCheckerBoard()
    chess.createPieces()
    for i in chess.checkers:
        print(chess.checkers[i])
    window.mainloop()


if __name__ == '__main__':
    main()
