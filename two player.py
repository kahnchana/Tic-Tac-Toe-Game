#interface for Tic Tac Toe

#initializing
from Tkinter import*

RealBoard=[0]*9 

window=Tk()
btn={}
resultOut= Label(window, text='player 1\'s turn')
player1=1
#functions

def recordInput(x):
    global player1
    if RealBoard[x]==0:
        if player1==1:
            RealBoard[x]=1
            btn[x].configure(text='X')
            resultOut.configure(text='player 2\'s turn')
            if checkIfWon():
                resultOut.configure(text='Player 1 has won!!')
                stop()
            elif not(0 in RealBoard):
                resultOut.configure(text='Game is draw :/')
                stop()
            player1=0
        else:
            RealBoard[x]=4
            btn[x].configure(text='O')
            resultOut.configure(text='player 1\'s turn')
            if checkIfWon():
                resultOut.configure(text='Player 2 has won!!')
                stop()
            elif not(0 in RealBoard):
                resultOut.configure(text='Game is draw :/')                
            player1=1

def runInterface():
    
    window.geometry('220x230+200+100')

    label1= Label(window, text="Welcome to Tic Tac Toe!")
    label1.pack()
    Label(window,text=' ').pack()
            
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

    Label(window,text='(two player version)').pack()

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

def restart():
    global player1
    for i in range(9):
        RealBoard[i]=0
    for i in btn:
        btn[i].configure(text=' ')
    resultOut.configure(text='player 1\'s turn')
    player1=1
    
def stop():
    for i in range(9):
        RealBoard[i]=1


runInterface()

