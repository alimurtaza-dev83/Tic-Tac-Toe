import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Standard():
    def __init__(self):
        self.title = 'TIC TAC TOE'
        self.checkarray = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        self.colorarr = ['red', 'blue']
        self.count = 0
        self.red = 0
        self.blue = 0
        self.color = self.colorarr[self.count%2]
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.resizable(False,False)
        self.root.configure(bg = 'white')
        self.buttonarray = [[],[],[]]
        self.styles()
        for ro in range(3):
            for colum in range(3):
                btn = ttk.Button(self.root, text = None, command = lambda r = ro, c = colum: self.disabler(r, c), style = 'stan.TButton', padding = 0, width = 2)
                btn.grid(row=(ro + 1), column=(colum + 1), ipadx=0, ipady=0)
                self.buttonarray[ro].append(btn)
        self.start()
    def disabler(self, ro, col):
        tex = 'O'
        if self.color == 'red':
            tex = 'X'
        self.buttonarray[ro][col].config(text = tex, state = 'disabled', style = self.color + '.TButton')
        self.count += 1
        self.checkarray[ro][col] = 2
        if self.color == 'red':
            self.checkarray[ro][col] = 1
        self.color = self.colorarr[self.count%2]
        self.style.map('stan.TButton', background = [('active', self.color)])
        self.wincheck()
    def wincheck(self):
        end = False
        winner = 0
        temparr = ['Draw! ', 'Red Wins! ', 'Blue Wins! ']
        
        for i in range(3):
            if (self.checkarray[i][0] == self.checkarray[i][1] == self.checkarray[i][2] != 0):
                end = True
                winner = self.checkarray[i][0]
            if (self.checkarray[0][i] == self.checkarray[1][i] == self.checkarray[2][i] != 0): 
                end = True
                winner = self.checkarray[0][i]
        if (self.checkarray[0][0] == self.checkarray[1][1] == self.checkarray[2][2] != 0):
            end = True
            winner = self.checkarray[1][1]
        if (self.checkarray[0][2] == self.checkarray[1][1] == self.checkarray[2][0] != 0):
            end = True
            winner = self.checkarray[2][0]
        if self.count == 9 and not end:
            end = True
            winner = 0
        if end == True:
            if winner == 1:
                self.red += 1
            if winner == 2:
                self.blue += 1
            result = messagebox.askyesno('Restart', temparr[winner] + 'Play again?')
            if result:
                self.reset()
            else:
                self.root.destroy()
    def reset(self):
        self.styles()
        for ro in range(3):
            for colum in range(3):
                self.buttonarray[ro][colum].config(text = '', state = 'normal')
        self.count = 0
        self.color = 'red'
        self.redlabel.config(text = str(self.red))
        self.bluelabel.config(text = str(self.blue))
        self.checkarray = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    def styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam') 
        self.style.configure('red.TLabel', font = ('Times New Roman', 50), foreground = 'red', background = 'white')
        self.style.configure('blue.TLabel', font = ('Times New Roman', 50), foreground = 'blue', background = 'white')
        self.style.configure('Turn.TLabel', font = ('Times New Roman', 50), foreground = self.color, background = 'white')
        self.style.configure('stan.TButton', font = ('Times New Roman', 50), background = 'yellow')
        self.style.map('stan.TButton', background = [('active', 'red'), ('disabled', 'white')])
        self.style.configure('blue.TButton', font = ('Times New Roman', 50), background = 'yellow')
        self.style.map('blue.TButton', foreground = [('disabled', 'blue')], background = [('disabled', 'white')])
        self.style.configure('red.TButton', font = ('Times New Roman', 50), background = 'yellow')
        self.style.map('red.TButton', foreground = [('disabled', 'red')], background = [('disabled', 'white')])
    def start(self):
        self.root.rowconfigure(0, weight = 1)
        self.root.rowconfigure(6, weight = 1)
        self.root.columnconfigure(0, weight = 1)
        self.root.columnconfigure(4, weight = 1)
        self.redlabel = ttk.Label(self.root, text = '0', style = 'red.TLabel')
        self.redlabel.grid(row = 2,column = 0)
        self.bluelabel = ttk.Label(self.root, text = '0', style = 'blue.TLabel')
        self.bluelabel.grid(row = 2,column = 4)
        self.root.mainloop()
a = Standard()
