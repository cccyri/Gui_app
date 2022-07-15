import tkinter as tk
import os
import time
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.filedialog import *
from random import randrange

#setting up the splash screen separately from the main class
__thisWidth = 450
__thisHeight = 650

splash_root = Tk()
splash_root.configure(background='#6A6AC2')

background_image=tk.PhotoImage(file = "i used a gameboy pic :D")
background_label = tk.Label(splash_root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def exit_program():
   splash_root.destroy()

screenWidth = splash_root.winfo_screenwidth()
screenHeight = splash_root.winfo_screenheight()

# For left-align
left = (screenWidth / 2) - (__thisWidth / 2)

# For right-align
top = (screenHeight / 2) - (__thisHeight / 2)

splash_root.geometry('%dx%d+%d+%d' % (__thisWidth,
                                      __thisHeight- 50,
                                      left, top))  # this expression centers the main window + resizes it

#splash_root.eval('tk::PlaceWindow . center') is another way

splash_root.overrideredirect(True) # to remove the unneeded buttons

c1 = tk.Canvas(splash_root, width=__thisWidth - 10, height=__thisHeight - 10, bg = '#6A6AF6')
c1.grid(row=1, column=0, padx=5, pady=5)
x1, y1, x2, y2 = 50, 50, __thisWidth + 10, __thisHeight + 10
gap = 25

#Add a Label widget in the Canvas
label = Label(c1, text= "  Welcome to the Notepad   ", font= ('Helvetica 17 bold'))
label.pack(pady= 80)

#Create a button in canvas widget
ttk.Button(c1, text= "Click to Continue", command= exit_program).pack()
c1.pack(pady = 60)

def my_draw():
    global x1, y1, x2, y2
    color_c = '#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))
    c1.create_oval(x1, y1, x2, y2, fill=color_c)
    x1, y1, x2, y2 = x1 + gap, y1 + gap, x2 - gap, y2 - gap

    if (x1 < (__thisWidth / 2)):
        c1.after(50, my_draw)

    else:
        restart()
        return


my_draw()


def restart():
    global x1, y1, x2, y2
    x1, y1, x2, y2 = 5, 5, __thisWidth - 5, __thisHeight - 5

    my_draw()

splash_root.mainloop()

class Notepad:
    __root = tk.Tk() #initializing the instance

    __thisWidth = 700
    __thisHeight = 500

    __thisTextArea = Text(__root, bg = "#7A706E", cursor = "cross", highlightcolor= "#7A709E") #text widget with the parent window "__root"
    __thisMenuBar = Menu(__root)

    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)


    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("Untitled - Notepad (cccyri)")

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)


        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top)) #this expression centers the main window + resizes it

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)

        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    # exit()

    def __showAbout(self):
        showinfo("Notepad", "This tool can view and edit your files."
                            "\nMade with Tkinter.")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.__root.mainloop()


# Run main application
notepad = Notepad(width=800, height=500) #passing this to the constructor in the class
notepad.run()
