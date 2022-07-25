import tkinter as tk
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

window = tk.Tk()
window.title('Calculator')

class Calculator:
    def __init__(self, win):
        self.equationStrVar = tk.StringVar()
        self.expressionStr = ''
        self.calcKeyboard = [
            ['7', '8', '9', '+'],
            ['4','5','6','-'],
            ['1', '2', '3','*'],
            ['0','Clear', '=', '/']
        ]
        self.prepareGui(win)
    
    def prepareGui(self, win):
        win.geometry('260x130')
        self.expressionField = tk.Entry(win, textvariable=self.equationStrVar)
        self.expressionField.grid(columnspan=4, ipadx=60)

        rowInd=0
        while rowInd < len(self.calcKeyboard):
            calcRow=self.calcKeyboard[rowInd]

            columnInd=0
            while columnInd<len(calcRow):
                buttonText=calcRow[columnInd]
                button = tk.Button(win, text=buttonText, height=1, width=8, fg='black', bg='silver',
                            command= lambda v=buttonText: self.buttonPressed(v))
                button.grid(row = rowInd+1, column = columnInd)
                columnInd+=1

            rowInd+=1
        
    def buttonPressed(self, value):

        if value== 'Clear':
            self.expressionStr = ''
            self.equationStrVar.set('')
            return
        
        if value== '=':
            result = str(eval(self.expressionStr))
            self.expressionStr = result
            self.equationStrVar.set(result)
            return

        self.expressionStr += str(value)
        self.equationStrVar.set(self.expressionStr)

    
calc = Calculator(window)

window.mainloop()
