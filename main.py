# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import RollDice


import random
from tkinter import *
from tkinter import messagebox, Spinbox
# from tkinter.font import font as tkFont
from tkinter.font import Font

#List of Skill Results
SkillResults1 = []
SkillResults2 = []


#Dictionary used for labelling radio buttons to pick
# dice types. Also gives top of range when die rolled
_DiceRanges = {"D3":3,
               "D4":4,
               "D6":6,
               "D8":8,
               "D10":10,
               "D12":12,
               "D14":14,
               "D16":16,
               "D20":20
               }


_DiceResults ={"PA1":"",
               "PA2":"",
               "SK1_Type":"",
               "SK1_Count":0,
               "SK2_Type":"",
                }
#LIst of Dice types
#Used to define lists of Dice types in Radio button controls
DiceTypes = (('D2'),
             ('D3'),
             ('D4'),
             ('D6'),
             ('D8'),
             ('D10'),
             ('D12'),
             ('D14'),
             ('D16'),
             ('D18'),
             ('D20'))

#This function sets up 2 lists, one for each skill die, then reads the spinbox results into SkillResults1 and SkilResults2
#Lists  After that it iterates through the lists and puts the number and type of dice into a dictionary _DiceResults and
#return it.
def getSkillCounts():
    SkillResults1 = []
    SkillResults1.append(DSpin1_2.get())
    SkillResults1.append(DSpin1_3.get())
    SkillResults1.append(DSpin1_4.get())
    SkillResults1.append(DSpin1_6.get())
    SkillResults1.append(DSpin1_8.get())
    SkillResults1.append(DSpin1_10.get())
    SkillResults1.append(DSpin1_12.get())
    SkillResults1.append(DSpin1_14.get())
    SkillResults1.append(DSpin1_16.get())
    SkillResults1.append(DSpin1_18.get())
    SkillResults1.append(DSpin1_20.get())

# Build the list for the second skill die type
    SkillResults2 = []
    SkillResults2.append(DSpin2_2.get())
    SkillResults2.append(DSpin2_3.get())
    SkillResults2.append(DSpin2_4.get())
    SkillResults2.append(DSpin2_6.get())
    SkillResults2.append(DSpin2_8.get())
    SkillResults2.append(DSpin2_10.get())
    SkillResults2.append(DSpin2_12.get())
    SkillResults2.append(DSpin2_14.get())
    SkillResults2.append(DSpin2_16.get())
    SkillResults2.append(DSpin2_18.get())
    SkillResults2.append(DSpin2_20.get())

    # step through the resonse for each spinbox stored ind SkillResults1 and SkillResults2
    _DiceResults["SK1_Type"] =""
    _DiceResults["SK1_Count"]="0"
    for i in range(0,len(SkillResults1)):
        if SkillResults1[i] != "0":
            _DiceResults["SK1_Type"]=DiceTypes[i]
            _DiceResults["SK1_Count"]=SkillResults1[i]

    _DiceResults["SK2_Type"] = ""
    _DiceResults["SK2_Count"] = "0"
    for i in range(0,len(SkillResults2)):
        if SkillResults2[i] != "0":
            _DiceResults["SK2_Type"]=DiceTypes[i]
            _DiceResults["SK2_Count"]=SkillResults2[i]


    return _DiceResults


# Declare Base Tkinter instance
root = Tk()

#Tkinter variables for PA dice choice
_PA1 = StringVar()
_PA2 = StringVar()
_PA1.set("D6")
_PA2.set("D6")


#Variables the number of each skill dice type for the skill dice spin boxes
_SP1_2 =IntVar().set("0")
_SP1_3 =IntVar().set("0")
_SP1_4 =IntVar().set("0")
_SP1_6 =IntVar().set("0")
_SP1_8 =IntVar().set("0")
_SP1_10 =IntVar().set("0")
_SP1_12 =IntVar().set("0")
_SP1_14 =IntVar().set("0")
_SP1_16 =IntVar().set("0")
_SP1_18 =IntVar().set("0")
_SP1_20 =IntVar().set("0")
_SP2_2 =IntVar().set("0")
_SP2_3 =IntVar().set("0")
_SP2_4 =IntVar().set("0")
_SP2_6 =IntVar().set("0")
_SP2_8 =IntVar().set("0")
_SP2_10 =IntVar().set("0")
_SP2_12 =IntVar().set("0")
_SP2_14 =IntVar().set("0")
_SP2_16 =IntVar().set("0")
_SP2_18 =IntVar().set("0")
_SP2_20 =IntVar().set("0")



# Radio button variable for number of skill dice chosen/set
_DieCount1 = IntVar().set(0)
_DieCount2 = IntVar().set(0)


# Root Window and Geometry
root.title("Dice Tales Dice Roller")
root.geometry('600x600')
root.resizable(1,1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.iconbitmap('C:/Users/Dan91/PycharmProjects/DiceRoller/dicetales2.ico')
root.title("Dice Tales Dice Roller")
btnExit=Button(root,text="Exit", font= ('None,12,normal'),command=quit).place(height=35, width=75,relx= .95,rely=.95,anchor=SE)

#General Purpose center  a window on the screen function
def CenterWindow(_winname,_width,_height):
    screen_width=_winname.winfo_screenwidth()
    screen_height=_winname.winfo_screenheight()
    center_x = int(screen_width/2-_width/2)
    center_y = int(screen_height/2-_height/2)
    _winname.geometry(f'{_width}x{_height}+{center_x}+{center_y}')

#Frame for PA dice choice and objects in frame1
frame1=LabelFrame(root,padx=5,pady=5)
frame1.grid(column = 0,row=0,padx=15,pady=15)

#Frame for Skill dice choice in frame2
frame2=LabelFrame(root,padx=5,pady=5)
frame2.grid(row=0,column=1,padx=15,pady=15,sticky=N)

#Geometry for PA dice choice objects in frame1
lbl_frame1= Label(frame1,text = "PA Dice Types                ")
lbl_frame1.grid(row=0,column=1)

#Geometry for PA dice choice objects in frame1
lbl_frame2= Label(frame2,text = "         Skill Dice")
lbl_frame2.grid(row=0,column=2, columnspan=2)

# Build PA die 1 Radio Button in Frame1
PArow = 1
for PADie1 in DiceTypes:
    b1 = Radiobutton(
    frame1,
    text=PADie1,
    variable=_PA1,value=PADie1,font=(None, 12)).grid(row=PArow,column=0,sticky=W)
    PArow=PArow + 1

# Build PA die 2 Radio Button in Frame1
PA2row = 1
for PADie2 in DiceTypes:
    b2 = Radiobutton(
    frame1,
    text=PADie2,
    variable=_PA2,value=PADie2,font=(None, 12)).grid(row=PA2row,column=1,padx=25,sticky=W)
    PA2row=PA2row + 1

# Build the Radio Buttons for Skill Die Type 1
DSpin1_2 = Spinbox(frame2, from_=0,to=5,width=5,font=Font(size=14),increment=1,textvariable=_SP1_2)
DSpin1_2.grid(row=1,column=2,pady=5,sticky=W)
DSpin1_3 = Spinbox(frame2, from_=0,to=5,width=5,font=Font(size=14),increment=1,textvariable=_SP1_3)
DSpin1_3.grid(row=2,column=2,pady=5,sticky=W)
DSpin1_4 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_4)
DSpin1_4.grid(row=3,column=2,pady=5,sticky=W)
DSpin1_6 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_6)
DSpin1_6.grid(row=4,column=2,pady=5,sticky=W)
DSpin1_8 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_8)
DSpin1_8.grid(row=5,column=2,pady=5,sticky=W)
DSpin1_10 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_10)
DSpin1_10.grid(row=6,column=2,pady=5,sticky=W)
DSpin1_12 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_12)
DSpin1_12.grid(row=7,column=2,pady=5,sticky=W)
DSpin1_14 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_14)
DSpin1_14.grid(row=8,column=2,pady=5,sticky=W)
DSpin1_16 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_16)
DSpin1_16.grid(row=9,column=2,pady=5,sticky=W)
DSpin1_18 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_18)
DSpin1_18.grid(row=10,column=2,pady=5,sticky=W)
DSpin1_20 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14),increment=1,textvariable=_SP1_20)
DSpin1_20.grid(row=11,column=2,pady=5,sticky=W)

# Build the Radio Buttons for Skill Die Type 2
DSpin2_2 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_2)
DSpin2_2.grid(row=1,column=4,sticky=E)
DSpin2_3 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_3)
DSpin2_3.grid(row=2,column=4,sticky=E)
DSpin2_4 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_4)
DSpin2_4.grid(row=3,column=4,sticky=E)
DSpin2_6 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_6)
DSpin2_6.grid(row=4,column=4,sticky=E)
DSpin2_8 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_8)
DSpin2_8.grid(row=5,column=4,sticky=E)
DSpin2_10 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_10)
DSpin2_10.grid(row=6,column=4,sticky=E)
DSpin2_12 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_12)
DSpin2_12.grid(row=7,column=4,sticky=E)
DSpin2_14 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_14)
DSpin2_14.grid(row=8,column=4,sticky=E)
DSpin2_16 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_16)
DSpin2_16.grid(row=9,column=4,sticky=E)
DSpin2_18 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_18)
DSpin2_18.grid(row=10,column=4,sticky=E)
DSpin2_20 = Spinbox(frame2, from_=0,to=5,width=5, font=Font(size=14), increment=1,textvariable=_SP2_20)
DSpin2_20.grid(row=11,column=4,sticky=E)

#Build the labels for the dice types in Frame 2
Dlbl_D2_1 = Label(frame2,text="D2").grid(row=1,column=1,sticky=W,padx=10)
Dlbl_D2_2 = Label(frame2,text="D2").grid(row=1,column=3,sticky=W,padx=10)
Dlbl_D3_1 = Label(frame2,text="D3").grid(row=2,column=1,sticky=W,padx=10)
Dlbl_D3_2 = Label(frame2,text="D3").grid(row=2,column=3,sticky=W,padx=10)
Dlbl_D4_1 = Label(frame2,text="D4").grid(row=3,column=1,sticky=W,padx=10)
Dlbl_D4_2 = Label(frame2,text="D4").grid(row=3,column=3,sticky=W,padx=10)
Dlbl_D6_1 = Label(frame2,text="D6").grid(row=4,column=1,sticky=W,padx=10)
Dlbl_D6_2 = Label(frame2,text="D6").grid(row=4,column=3,sticky=W,padx=10)
Dlbl_D8_1 = Label(frame2,text="D8").grid(row=5,column=1,sticky=W,padx=10)
Dlbl_D8_2 = Label(frame2,text="D8").grid(row=5,column=3,sticky=W,padx=10)
Dlbl_D10_1 = Label(frame2,text="D10").grid(row=6,column=1,sticky=W,padx=10)
Dlbl_D10_2 = Label(frame2,text="D10").grid(row=6,column=3,sticky=W,padx=10)
Dlbl_D12_1 = Label(frame2,text="D12").grid(row=7,column=1,sticky=W,padx=10)
Dlbl_D12_2 = Label(frame2,text="D12").grid(row=7,column=3,sticky=W,padx=10)
Dlbl_D14_1 = Label(frame2,text="D14").grid(row=8,column=1,sticky=W,padx=10)
Dlbl_D14_2 = Label(frame2,text="D14").grid(row=8,column=3,sticky=W,padx=10)
Dlbl_D16_1 = Label(frame2,text="D16").grid(row=9,column=1,sticky=W,padx=10)
Dlbl_D16_2 = Label(frame2,text="D16").grid(row=9,column=3,sticky=W,padx=10)
Dlbl_D18_1 = Label(frame2,text="D18").grid(row=10,column=1,sticky=W,padx=10)
Dlbl_D18_2 = Label(frame2,text="D18").grid(row=10,column=3,sticky=W,padx=10)
Dlbl_D20_1 = Label(frame2,text="D20").grid(row=11,column=1,sticky=W,padx=10)
Dlbl_D20_2 = Label(frame2,text="D20").grid(row=11,column=3,sticky=W,padx=10)




#Function to detect and display Skill dice selected. Triggered by btnPAOK click
def DiceSelected ():
    _DiceResults["PA1"]=_PA1.get()
    _DiceResults["PA2"]=_PA2.get()
    getSkillCounts()
    #print(getSkillCounts())
    # messagebox.showinfo("Dice Selected","PA Dice are " + str(PAchoice1) + "/" + str(PAchoice2))


#Button to read and display PA dice choice
btnPAOK=Button(root,text="Accept",font= ('None,8,normal'), command=DiceSelected).place(height=35, width=75,relx= .05,rely=.95,anchor=SW)

#Function to exit application
def quit(self):
    self.root.destroy()


# Main Loop
if __name__ == '__main__':
    random.seed()
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        # myset = cDice()
        # myset = cDice.get_dice_set(myset)
        # cDice.roll(myset)
        # cDice.print(myset)
        root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

