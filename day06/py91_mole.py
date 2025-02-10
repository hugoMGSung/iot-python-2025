from tkinter import *
from random import *

NUM_MOLES=3


root = Tk()
root.title('두더쥐 게임 v1.0')

moleFrame=Frame(root)
moleFrame.grid(row=0,column=0)

statusFrame=Frame(root)
statusFrame.grid(row=0,column=1)

hitsLabel=Label(statusFrame,text="0 히트")
hitsLabel.pack()
missedLabel=Label(statusFrame, text="0 놓침")
missedLabel.pack()

mole_image = PhotoImage(file='./day06/a-mole.png', master=root)
hole_image = PhotoImage(file='./day06/a-hole.png', master=root)
hit_image = PhotoImage(file='./day06/whack-a-mole.png', master=root)

numHits = 0
numMiss = 0
moleList = []

def mole_hit(c):
    global numHits, numMiss, moleList, missedLabel, hitsLabel
    if moleList[c]['text'] == 'mole':
        numHits += 1
        hitsLabel['text'] = f'{numHits} 히트'

    else:
        numMiss += 1
        missedLabel['text'] = f'{numMiss} 미스'


def init():
    count = 0
    for r in range(NUM_MOLES):
        for c in range(NUM_MOLES):
            button = Button(moleFrame, command=lambda c=count: mole_hit(c))
            button['image'] = hole_image
            button['text'] = 'hole'
            button.grid(row=r, column=c)
            moleList.append(button)
            count += 1

def update():
    global moleList

    for i in range(NUM_MOLES * NUM_MOLES):
        button = moleList[i]
        button['text'] = 'hole'
        button['image'] = hole_image

        x = randint(0, NUM_MOLES * NUM_MOLES - 1)
        moleList[x]['image'] = mole_image
        moleList[x]['text'] = 'mole'
    
    root.after(1000, update)

init()
update()
root.mainloop()