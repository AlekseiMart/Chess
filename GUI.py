import tkinter as tk

class Chess():
    def __init__(self, window):
        self.window = window
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
        w.pack()
        




def main():

    window = tk.Tk()
    window.title("Chess")
    window.resizable(width=False, height=False)
    Chess(window)
    window.mainloop()


if __name__ == '__main__':
    main()
