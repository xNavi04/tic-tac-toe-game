from tkinter import *
import random


class Ticgame():
    def __init__(self):
        self.window = Tk()
        self.window.title("tic tac toe game")

        self.button_2 = [[0,0,0],
                         [0,0,0],
                         [0,0,0]]


        self.vins = StringVar()

        self.user = ["X", "O"]
        self.userr = random.choice(self.user)
        self.vins.set(str(self.userr) + "  turn")
        self.space = ""

        self.label = Label(self.window, textvariable=self.vins, font=("Arial", 60))
        self.label.grid(row=0, column=0)

        self.button_1 = Button(self.window, text="Restart game", font=("Arial", 20), command=self.new_game)
        self.button_1.grid(row=1, column=0)

        self.frame_1 = Frame(self.window)
        self.frame_1.grid(row=2, column=0)


        for row in range(3):
            for column in range(3):
                self.button_2[row][column] = Button(self.frame_1, width=30, height=15, text="", command=lambda row=row, column=column: self.game(row, column))
                self.button_2[row][column].grid(row=row, column=column)



        self.window.mainloop()


    def game(self, row, column):
        print(self.space)
        if self.button_2[row][column]['text'] == "" and self.check_vin() != True:
            self.button_2[row][column]['text'] = self.userr
            if self.userr == "X":
                self.userr = self.user[1]
                if self.check_vin() == "Tie":
                    self.vins.set("TIE!")
                elif self.check_vin() is False:
                    self.vins.set(str(self.user[1]) + "  turn")
                elif self.check_vin() is True:
                    self.vins.set(str(self.user[0]) + "  vin!")
            elif self.userr == "O":
                self.userr = self.user[0]
                if self.check_vin() == "Tie":
                    self.vins.set("TIE!")
                elif self.check_vin() is False:
                    self.vins.set(str(self.user[0]) + "  turn")
                elif self.check_vin() is True:
                    self.vins.set(str(self.user[1]) + "  vin!")


    def check_vin(self):
        for column in range(3):
            if self.button_2[0][column]['text'] == self.button_2[1][column]['text'] == self.button_2[2][column]['text'] != "":
                self.button_2[0][column].config(bg="blue")
                self.button_2[1][column].config(bg="blue")
                self.button_2[2][column].config(bg="blue")
                return True
        for row in range(3):
            if self.button_2[row][0]['text'] == self.button_2[row][1]['text'] == self.button_2[row][2]['text'] != "":
                self.button_2[row][0].config(bg="blue")
                self.button_2[row][1].config(bg="blue")
                self.button_2[row][2].config(bg="blue")
                return True
        if self.button_2[0][0]['text'] == self.button_2[1][1]['text'] == self.button_2[2][2]['text'] != "":
            self.button_2[0][0].config(bg="blue")
            self.button_2[1][1].config(bg="blue")
            self.button_2[2][2].config(bg="blue")
            return True
        self.space = 9
        for row in range(3):
            for column in range(3):
                if self.button_2[row][column]['text'] != "":
                    self.space-=1
        if self.space == 0:
            for row in range(3):
                for column in range(3):
                    self.button_2[row][column].config(bg="yellow")
            return "Tie"
        return False

    def new_game(self):
        for row in range(3):
            for column in range(3):
                self.button_2[row][column].config(text="", bg="white")

        self.userr = random.choice(self.user)
        self.vins.set(str(self.userr) + "  turn")


def main():
    ticgame = Ticgame()


if __name__ == "__main__":
    main()