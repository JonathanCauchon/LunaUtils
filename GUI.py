from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import os
import tkinter.filedialog as filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from Luna import *

# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")
theme_color = "white" #"#073763"
button_color = "#0a70cf"
text_color = "white"

# style = Style()
# style.theme_use('alt')
# style.configure('TButton', background = button_color, foreground = text_color, borderwidth=1, focusthickness=3, focuscolor='none')
# style.map('TButton', background=[('active',"grey")])

"""
Acquired on 9/23/2020 at 13:25:38
Device Descriptor:  [none]
Number of Scan Averages:  4
Time Domain Window Resolution Bandwidth (pm):  56.212469
Filter Resolution Bandwidth (pm):  19.360054
Convolved Resolution Bandwidth (pm):  59.452951
Channel Width: 25.000 nm

"""


if 0:
    gui = Tk()
    gui.title("Luna Post-Processing Tool")


    label = Label(gui, text="Current file:").grid()
    def open():
        current_dir = os.getcwd()
        chosen_file = filedialog.askopenfile(parent=gui, initialdir=current_dir, title='Select a Luna Text File.')
        print(chosen_file.name)

    open_button = Button(gui,text="Open",command=open).grid()

    def save():
        pass

    save_button = Button (gui, text="Save", command=save).grid()
    fig = Figure(figsize=(7, 5), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
    fig.gca().set_facecolor(theme_color)
    fig.set_facecolor(theme_color)
    canvas = FigureCanvasTkAgg(fig, master=gui)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(column=1)
    # NavigationToolbar2TkAgg(canvas, gui).grid()

    toolbar_frame = Frame(gui)
    toolbar_frame.grid(column=1)
    toolbar = NavigationToolbar2Tk( canvas, toolbar_frame ) 


    # label.grid(column=0, row=0)

    # Dimensions of the window
    w = 950 # width for the Tk root
    h = 650 # height for the Tk root
    ws = gui.winfo_screenwidth() # width of the screen
    hs = gui.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    gui.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Library management
    # def Check1():
    #     if chk1State.get() == 1:
    #         txtlib1 = Entry(gui,width=10)
    #     else:
    #         txtlib1 = Entry(gui,width=10,state="disabled")
    #     txtlib1.grid(column=1,row=startRow+1)

    # def Check2():
    #     if chk2State.get() == 1:
    #         txtlib2 = Entry(gui,width=10)
    #     else:
    #         txtlib2 = Entry(gui,width=10,state="disabled")
    #     txtlib2.grid(column=1,row=startRow+2)

    # def Check3():
    #     if chk3State.get() == 1:
    #         txtlib3 = Entry(gui,width=10)
    #     else:
    #         txtlib3 = Entry(gui,width=10,state="disabled")
    #     txtlib3.grid(column=1,row=startRow+3)


    # startRow = 2
    # versionTxt = Label(gui, text="Version")
    # versionTxt.grid(column=1, row=startRow)

    # chk1State = BooleanVar()
    # chk1State.set(True)
    # Check1()
    # chk1 = Checkbutton(gui,text="SiEPIC-Tools",variable=chk1State,command=Check1,)
    # chk1.grid(column=0,row=startRow+1)
    # txtlib1 = Entry(gui,width=10)
    # txtlib1.grid(column=1,row=startRow+1)

    # chk2State = BooleanVar()
    # chk2State.set(True)
    # Check2()
    # chk2 = Checkbutton(gui,text="SiEPIC EBeam PDK",variable=chk2State,command=Check2)
    # chk2.grid(column=0, row=startRow+2)
    # txtlib2 = Entry(gui,width=10)
    # txtlib2.grid(column=1,row=startRow+2)

    # chk3State = BooleanVar()
    # chk3State.set(True)
    # Check3()
    # chk3 = Checkbutton(gui,text="Ulaval PDK",variable=chk3State, command=Check3)
    # chk3State.get()
    # chk3.grid(column=0, row=startRow+3)


    # # Users
    # # usrNum=3
    # def addUser():
    #     userList = np.ones(2,1)

    #     print(allUsrs)
    #     # frame.pack()
    #     newUsr = Entry(gui,width=15).grid(column=3,row=9)
    #     allUsrs.append(newUsr)
    #     return allUsrs


    # UsersTxt = Label(gui,text="Users").grid(column=3,row=startRow)
    # usr1 = Entry(gui,width=15).grid(column=3,row=startRow+1)
    # usr2 = Entry(gui,width=15).grid(column=3,row=startRow+2)
    # usr3 = Entry(gui,width=15).grid(column=3,row=startRow+3)
    # usr4 = Entry(gui,width=15).grid(column=3,row=startRow+4)
    # usr5 = Entry(gui,width=15).grid(column=3,row=startRow+5)
    # usr6 = Entry(gui,width=15).grid(column=3,row=startRow+6)





    # # Finalize buttons
    # def Create():
    #     gui.destroy()
    #     os.system("python ProjectCreator.py")
    #     successGui = Tk()
    #     successGui.title("Success")
    #     w = 200 # width for the Tk root
    #     h = 100 # height for the Tk root
    #     ws = successGui.winfo_screenwidth() # width of the screen
    #     hs = successGui.winfo_screenheight() # height of the screen
    #     x = (ws/2) - (w/2)
    #     y = (hs/2) - (h/2)
    #     successGui.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #     label = Label(successGui, text="Project successfully created.")
    #     label.grid(column=0, row=0)
    #     def SuccessOK():
    #         successGui.destroy()
    #     okBtn = Button(successGui, text=" OK ", width="6", bg="blue", fg="blue",command=SuccessOK)
    #     okBtn.grid(column=0,row=1)

    # ghost = Label(gui,text="    ").grid(column=2,row=9)

    # createBtn = Button(gui, text=" Create ", width="8", bg="blue", fg="blue",command=Create)
    # createBtn.grid(column=1,row=10)

    # def Cancel():
    #     gui.destroy()
    # cancelBtn = Button(gui,text=" Cancel ",width="8",  bg="blue", fg="blue",command=Cancel)
    # cancelBtn.grid(column=3,row=10)
    gui.configure(bg=theme_color)


class LunaGUI:

    accent_color = "orangered"

    def __init__(self, root):

        self.root = root
        self.root.title("Luna Post-Processing Tool")
        self.window_geometry()
        self.make_style()

        self.tools_frame = Frame(self.root)
        self.tools_frame.grid(pady=2)

        self.plot_frame = Frame(self.root)
        self.plot_frame.grid(row=0, column=1)

        self.current_file_label = Label(self.plot_frame, text="No file selected")
        self.current_file_label.grid(column=1)
        self.open_button = Button(self.tools_frame, text="Open", command=self.open_button).grid(pady=2, padx=5)
        self.save_button = Button(self.tools_frame, text="Save", command=self.save_button).grid(pady=2)
        self.file_info = Label(self.tools_frame, text="text \ntext \nsome more text motherfucker")
        self.file_info.grid(pady=2)
        
        self.place_plot()


    def open_button(self):
        current_dir = os.getcwd()
        chosen_file = filedialog.askopenfile(parent=self.root, initialdir=current_dir, title='Select a Luna Text File.')
        self.file = chosen_file.name
        self.current_file_label.configure(text="Current file: " + self.file)

        self.meas = LunaMeasurement(self.file)
        self.fig.gca().clear()
        self.fig.gca().plot(self.meas.wavelength, self.meas.insertion_loss)
        self.figure_canvas.draw()

        # update file info text
        # with open(self.file, "r") as f:
        #     self.file_header = [f.readline() for i in range(7)]
        
        # header = ""
        # for line in self.file_header:
        #     header = header + line 

        # self.file_info.configure(text=header)

    def update_plot(self, x, y):
        pass


    def place_plot(self):
        self.fig = Figure(figsize=(7, 5), dpi=100)
        t = np.arange(0, 3, .01)
        self.fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t), c=self.accent_color)
        self.fig.gca().set_facecolor("dimgrey")
        self.fig.set_facecolor("k")
        self.fig.gca().spines["bottom"].set_color("white")
        self.fig.gca().spines['top'].set_color('white')
        self.fig.gca().spines['right'].set_color('white')
        self.fig.gca().spines['left'].set_color('white')
        self.fig.gca().xaxis.label.set_color('white')
        self.fig.gca().grid()
        self.fig.gca().tick_params(axis='both', colors='white')
        self.fig.gca().yaxis.label.set_color('white')
        # self.fig.gca().tick_params(axis='x', colors='white')
        self.figure_canvas = FigureCanvasTkAgg(self.fig, master=root)  # A tk.DrawingArea.
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().grid(row=1, column=1, rowspan=9)
        # NavigationToolbar2TkAgg(canvas, gui).grid()

        self.toolbar_frame = Frame(self.root)
        self.toolbar_frame.grid(column=1)
        self.toolbar = NavigationToolbar2Tk( self.figure_canvas, self.toolbar_frame ) 


    def save_button(self):
        pass

    def make_style(self):
        """ define color and appearance of GUI """

        background_color = "black"
        button_color_1 = "grey26"
        button_color_2 = "grey70"
        text_color = "white"

        self.root.configure(bg=background_color) # background color

        self.style = Style()
        self.style.theme_use('alt')

        # Widget style definitions
        self.style.configure("TButton", background = button_color_1, 
            foreground = text_color, width=25, padding=20, relief="flat"
            , borderwidth=0, padx=5, pady=5)
        self.style.configure("TFrame", background=background_color)
        self.style.configure("TLabel", foreground="white", background="black")

        self.style.map('TButton', background=[('active', self.accent_color)])


    def window_geometry(self):
        w = 950 # width for the Tk root
        h = 650 # height for the Tk root
        ws = self.root.winfo_screenwidth() # width of the screen
        hs = self.root.winfo_screenheight() # height of the screen
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))


        # def open():
        #     current_dir = os.getcwd()
        #     chosen_file = filedialog.askopenfile(parent=gui, initialdir=current_dir, title='Select a Luna Text File.')
        #     print(chosen_file.name)

        # open_button = Button(gui,text="Open",command=open).grid()

        # def save():
        #     pass

        # save_button = Button (gui, text="Save", command=save).grid()
        # fig = Figure(figsize=(7, 5), dpi=100)
        # t = np.arange(0, 3, .01)
        # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        # fig.gca().set_facecolor(theme_color)
        # fig.set_facecolor(theme_color)
        # canvas = FigureCanvasTkAgg(fig, master=gui)  # A tk.DrawingArea.
        # canvas.draw()
        # canvas.get_tk_widget().grid(column=1)
        # # NavigationToolbar2TkAgg(canvas, gui).grid()

        # toolbar_frame = Frame(gui)
        # toolbar_frame.grid(column=1)
        # toolbar = NavigationToolbar2Tk( canvas, toolbar_frame ) 



        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.grid()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.grid()

    def greet(self):
        print("Greetings!")

root = Tk()
luna_gui = LunaGUI(root)
root.mainloop()                          

