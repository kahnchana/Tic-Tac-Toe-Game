#interface for Tic Tac Toe

#initializing
import Tkinter
from Tkinter import*
import random

RealBoard=[0]*9 
ImaginaryBoard=[0]*9
window=Tk()
btn={}
resultOut= Label(window, text='Your Turn')
lastMove=10
specialCaseOne=0


#functions

def recordInput(x):
    global lastMove
    if RealBoard[x]==0:
        lastMove=x
        RealBoard[x]=1
        btn[x].configure(text='X')
        if checkIfWon():
            resultOut.configure(text='You have won!! :D')
            stop()
        elif not(0 in RealBoard):
            resultOut.configure(text='Game is draw :/')
            stop()
        else:
            a=nextMove()
            RealBoard[a]=4
            btn[a].configure(text='O')
            if checkIfWon():
                resultOut.configure(text='You  lost :(')
                stop()
            elif not(0 in RealBoard):
                resultOut.configure(text='Game is draw :/')
                stop()

def runInterface():
    
    window.geometry('240x250+200+100')

    label1= Label(window, text="Welcome to Tic Tac Toe! (single player)")
    label1.pack()
    Label(window,text='Made by Kanchana '+unichr(0x00A9)).pack()
            
    top= Frame(window)
    top.pack()
    mid= Frame (window)
    mid.pack()
    bot= Frame (window)
    bot.pack()

    for i in range(0,3):
        btn[i]= Button(window,text=' ',width=5,height=2, command=lambda num=i:recordInput(num))
        btn[i].pack(in_=top, side=LEFT)

    for i in range(3,6):
        btn[i]= Button(window,text=' ',width=5,height=2, command=lambda num=i:recordInput(num))
        btn[i].pack(in_=mid, side=LEFT)

    for i in range(6,9):
        btn[i]= Button(window,text=' ',width=5,height=2, command=lambda num=i:recordInput(num))
        btn[i].pack(in_=bot, side=LEFT)

    resultOut.pack()

    replay= Button(window, text='play again', command=restart)
    replay.pack()
    compFirst= Button(window, text='play with computer first',command=computerFirst)
    compFirst.pack()

    window.mainloop()

def checkIfWon():
    a=[0]*8
    a[1]=sum(RealBoard[i] for i in range(3))
    a[2]=sum(RealBoard[i] for i in range(3,6))
    a[3]=sum(RealBoard[i] for i in range(6,9))
    a[4]=sum(RealBoard[i] for i in range(0,7,3))
    a[5]=sum(RealBoard[i] for i in range(1,8,3))
    a[6]=sum(RealBoard[i] for i in range(2,9,3))
    a[7]=sum(RealBoard[i] for i in range(0,9,4))
    a[0]=sum(RealBoard[i] for i in range(2,7,2))

    for i in range(8):
        if a[i]==3 or a[i]==12:
            return True
    return False

def checkIfLost(): #checks same thing as above
    a=[0]*8
    a[1]=sum(ImaginaryBoard[i] for i in range(3))
    a[2]=sum(ImaginaryBoard[i] for i in range(3,6))
    a[3]=sum(ImaginaryBoard[i] for i in range(6,9))
    a[4]=sum(ImaginaryBoard[i] for i in range(0,7,3))
    a[5]=sum(ImaginaryBoard[i] for i in range(1,8,3))
    a[6]=sum(ImaginaryBoard[i] for i in range(2,9,3))
    a[7]=sum(ImaginaryBoard[i] for i in range(0,9,4))
    a[0]=sum(ImaginaryBoard[i] for i in range(2,7,2))

    for i in range(8):
        if a[i]==3 or a[i]==12:
            return True
    return False

def computerFirst():
    restart()
    a=random.randint(0,8)
    RealBoard[a]=4
    btn[a].configure(text='O')

def restart():
    global lastMove
    global specialCaseOne
    for i in range(9):
        RealBoard[i]=0
        ImaginaryBoard[i]=0
    for i in btn:
        btn[i].configure(text=' ')
    resultOut.configure(text='Your turn to play')
    lastMove=10
    specialCaseOne=0

    
def stop():
    for i in range(9):
        RealBoard[i]=1

def canWeWin():        
    for i in range(9):
        ImaginaryBoard[i]=RealBoard[i]
    for i in range(9):
        if RealBoard[i]==0:
            ImaginaryBoard[i]=4
            if checkIfLost():
                return i
            else:
                ImaginaryBoard[i]=0
    return -1

def canWeLose():
    for i in range(9):
        ImaginaryBoard[i]=RealBoard[i]
    for i in range(9):
        if RealBoard[i]==0:
            ImaginaryBoard[i]=1
            if checkIfLost():
                return i
            else:
                ImaginaryBoard[i]=0
    return -1    


def closestSquare():
    global lastMove
    if lastMove in [0,6]:
        if RealBoard[5]==0:
            return 3
        else:
            return lastMove+1

    if lastMove in [2,8]:
        if RealBoard[3]==0:
            return 5
        else:
            return lastMove-1

    if lastMove in [1,7]:
        if RealBoard[lastMove-1]==0:
            return lastMove-1
        else:
            return lastMove+1

    if lastMove in [3,5]:
        if RealBoard[lastMove-3]==0:
            return lastMove-3
        else:
            return lastMove+3

def nextMove():
    global specialCaseOne
    global lastMove

    b=canWeWin()
    if b!=-1:
        return b
    
    c=canWeLose()
    if c!=-1:
        return c

    if RealBoard[4]==0:
        return 4
    
    if specialCaseOne==1 and lastMove in [0,2,6,8]:
        for i in [0,2,6,8]:
            if RealBoard[i]==0:
                specialCaseOne=0
                return i

    if lastMove==4:
        specialCaseOne=1
        a=random.randint(0,4)
        if a==2:
            return 2
        else:
            return a*2
    
    d=closestSquare()
    if RealBoard[d]==0:
        return d
    else:
        if 0 in RealBoard:
            return RealBoard.index(0)
    
        
runInterface()
