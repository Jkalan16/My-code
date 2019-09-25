from tkinter import *

main = Tk()

NameList = []
counter = 0


def PrintText():

    #Globalising first and last name so that they can be used in other subroutines
    global name, counter, NameLabel

    #Defining the .get() function as something else to make it easier
    name = name_entry.get()

    NameList.append(name)
    NameLabel = Label(main, text=(NameList[0+counter]))
    NameLabel.grid(row=(counter+3))
    counter += 1

def DeleteText():

    global NameLabel, counter

    NameLabel.destroy()
    counter -= 1
    del NameList[counter]

def Name():
    #Globalising the labels and buttons so that they can be deleted later on
    global first_name_label, first_quit, next_button
    #
    name_label = Label(main, text="Name:")
    name_label.grid(row=0, column=0)
    #
    PrintTextButton = Button(main, text="Print Text", width=8, command=PrintText, bg="light blue")
    PrintTextButton.grid(row=2, column=0)
    DeleteTextButton = Button(main, text="Delete Text", width=8, command=DeleteText, bg="light blue")
    DeleteTextButton.grid(row=2, column=1)


name_entry = Entry(main)
name_entry.grid(row=0, column=1, columnspan=4)

errorName = StringVar()
Name()
