"""
# Licensed to MSOE
# This file is owned and copyrighted by Jorge Jurado-Garcia
#  Author: Jorge Jesus Jurado-Garcia
#  Title: ECK GUI engineer
#
#  Date of Creation: 12/29/2021
#  Rev:

import all classes/method
from the tkinter module

as of 2/7/2022 the Tkinter main frame was finished and created
further development is being implemented with adding a menus to the program for:
        File---
            Read me
            Exit
        Read Me--
            About the Author
            About Filters
            About ECK's
        GitHub--
            GitHUB
        SCOPE Capture--
            Check Box for png location
"""
import threading
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk, Menu
from tkinter.messagebox import showerror, showinfo
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Imports import text_imports
from random import randint
from plyer import notification

"""
I Am a bit dumb and don't know how to use python tkinter modules with threading so i just ended up 
using the two functions called run new_graph in order to be able to take care making this work
works fine just a bit confusing on how and why it works.
"""
name = "None"
date = "None"
filepath = "None"
x_axis = []

def store_values(_name, _date, file_path):
    global name
    name = _name
    global date
    date = _date
    global filepath
    filepath = file_path


def data_points():
    f = open("data.txt", "w")
    for i in range(20):
        f.write(str(randint(0, 10)) + '\n')
    f.close()

    f = open("data.txt", "r")
    data = f.readlines()
    f.close()

    line = []
    global x_axis

    for i in range(len(data)):
        line.append(int(data[i].rstrip("\n")))
        x_axis.append(i)


    return line, x_axis


class MainFrame(ttk.Frame):

    # Initialization
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        """object main public variables"""
        self.name_entry = tk.StringVar()
        self.Date_entry = tk.StringVar()
        self.selected_filter = tk.StringVar()
        self.png_location_path = str()

        # Name label
        self.name_label = ttk.Label(self, text="Name :")
        self.name_label.grid(column=0, row=0, sticky=tk.W, **options)

        # Name entry
        self.name_entry = ttk.Entry(self, textvariable=self.name_entry)
        self.name_entry.grid(column=1, row=0, sticky=tk.E, **options)
        self.name_entry.focus()

        # Date label
        self.Date_label = ttk.Label(self, text="Date : (Only _ )")
        self.Date_label.grid(column=0, row=1, sticky=tk.W, **options)

        # Date entry
        self.Date_entry = ttk.Entry(self, textvariable=self.Date_entry)
        self.Date_entry.grid(column=1, row=1, sticky=tk.E, **options)
        self.Date_entry.focus()

        # filter label and combo box
        self.filter_label = ttk.Label(self, text="Filter:")
        self.filter_label.grid(column=0, row=2, sticky=tk.W, **options)
        self.filter_cb = ttk.Combobox(self, textvariable=self.selected_filter)
        self.filter_cb['values'] = ('No Filter', 'LP Filter', 'HP Filter', 'Notch Filter', 'All Filter')
        self.filter_cb['state'] = 'readonly'
        self.filter_cb.grid(column=1, row=2, sticky=tk.NE, **options)
        self.filter_cb.set('No Filter')

        # Dump png here
        self.button = ttk.Button(self, text="Scope png - Location", command=self.new_png_location)
        self.button.grid(row=3, column=0, columnspan=2, sticky=tk.EW, **options)

        # Graph button
        self.start_button = ttk.Button(self, text='Start-Graph', command=self.start)
        self.start_button.grid(column=0, row=4, columnspan=2, sticky=tk.EW, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def new_png_location(self):
        self.png_location_path = self.folder_lookup()
        store_values(self.name_entry.get(), self.Date_entry.get(), self.png_location_path)

    def start(self):
        self.check_entry

    def stop(self):
        self.stop_entry

    def show_selected_filter(self):
        showinfo(
            title='Result',
            message=self.selected_filter.get()
        )

    @staticmethod
    def folder_lookup():
        directory = fd.askdirectory(
        )
        if directory != "":
            showinfo(
                title='Selected Directory',
                message=directory
            )
        return directory

    @property
    def check_entry(self):
        check = True
        # Retrieve the of name, date, and MTE Selection
        inputs = [self.Date_entry.get(), self.name_entry.get()]
        if inputs[0] == '':
            showerror(
                title='Error-Date',
                message='Please type in Date.'
            )
            check = False
        if inputs[1] == '':
            showerror(
                title='Error-Selection',
                message='Please type in a name.'
            )
            check = False
        if check:
            showinfo(
                title='Settings',
                message='Settings are Configured'
            )
            self.stop_button = ttk.Button(self, text='Exit-Graph', command=self.stop)
            self.stop_button.grid(column=0, row=4, columnspan=2, sticky=tk.EW)
            # field options
            '''
             TODO 
             Create a function that calls this class instead 
             of just declaring it. It could be user in the long run
            '''
            store_values(inputs[1], inputs[0], self.png_location_path)
            self.element = Graph()
            self.element.mainloop()

    @property
    def stop_entry(self):
        self.start_button = ttk.Button(self, text='Start-Graph', command=self.start)
        self.start_button.grid(column=0, row=4, columnspan=2, sticky=tk.EW)
        self.element.terminate()
        self.element.destroy()


"""
Here, we are creating our class, Window, and inheriting from the Frame
class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
"""


class Window(tk.Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master):
        super().__init__(master)
        # field options

        # reference to the master widget, which is the tk window
        self.save = tk.BooleanVar()
        self.save.set(False)
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Read Me", command=self.read_me_exit)
        file.add_command(label="Exit", command=self.user_exit)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object
        about = Menu(menu)

        # added "about the author" to our menu
        about.add_command(label="About Author", command=self.author_about)
        about.add_command(label="About Filters", command=self.filter_about)
        about.add_command(label="About ECG's", command=self.ecg_about)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        menu.add_cascade(label="About", menu=about)

        # create the file object
        github = Menu(menu)

        # added "about the author" to our menu
        github.add_command(label="GitHub Repository", command=self.Github_link)
        github.add_command(label="Email - Address", command=self.email_link)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        menu.add_cascade(label="GitHub", menu=github)

        # scope = Menu(menu)
        # scope.add_checkbutton(label="Save Waveform", onvalue=1, offvalue=0, variable=self.save)
        # menu.add_cascade(label="Scope", menu=scope)

    @staticmethod
    def read_me_exit():
        text_imports.text_window("Read Me", text_imports.read_info)

    @staticmethod
    def author_about():
        text_imports.text_window("About Author", text_imports.author_info)

    @staticmethod
    def filter_about():
        text_imports.text_window("About Filters", text_imports.filter_info)

    @staticmethod
    def ecg_about():
        text_imports.text_window("About ECGs", text_imports.ecg_info)

    @staticmethod
    def user_exit():
        exit()

    @staticmethod
    def Github_link():
        showinfo(
            title='GitHub Repository',
            message='This is where the github link will be placed'
        )

    @staticmethod
    def email_link():
        showinfo(
            title='Email',
            message='jorgejuradogarcia2@gmail.com'
        )


"""
Here is the class and methods for setting up the
the graphing tinker module when the start button 
is enabled
"""


class Graph(tk.Tk):

    def __init__(self):
        super().__init__()

        self.init_window()

        self.init_widgets()

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.title.set_text('ECG Monitoring')
        self.ax.set_xlabel("Time [mS]")
        self.ax.set_ylabel("Amplitude [V/mV]")
        self.ax.grid()

        self.graph = FigureCanvasTkAgg(self.fig, master=self)
        self.graph.get_tk_widget().pack(side="top", fill='both', expand=True)

    def init_window(self):
        self.title('DIY-ECG Graph')
        window_width = 1000
        window_height = 630

        # get screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # create the screen on window console
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y-30}')
        self.iconbitmap('./imports/msoe.ico')
        self.resizable(False, False)

    def init_widgets(self):
        # reference to the master widget, which is the tk window
        self.pause = tk.Button(self, text="Pause", command=self.button_handler,
                               bg="red", fg="black")
        self.start = tk.Button(self, text="Start", command=self.button_handler,
                               bg="green", fg="black")
        self.Screenshot = tk.Button(self, text="ScreenShot", command=self.screen_shot,
                                    bg="blue", fg="white")

        # creating top frame for left and right side of the buttons
        self.start.pack(side='top', fill='x')

        self.pause.pack(side='top', fill='x')

        # information of the heart rhyming in the future this will controlled by an AI
        self.rhythm = tk.Label(self, text='Rhythm - Normal Sinus').pack(side='top', fill='x')
        self.heart_label = tk.Label(self, text='HR: 100').pack(fill='x')
        self.PR_label = tk.Label(self, text='PR: 0.12').pack(fill='x')
        self.QRS_label = tk.Label(self, text='QRS: 0.12').pack(fill='x')
        self.QT_label = tk.Label(self, text='QT: 0.32').pack(fill='x')

        self.Screenshot.pack(side='bottom', fill='x')
        self.continuePlotting = False
        self.pause['state'] = 'disabled'
        self.start['state'] = 'normal'

    def button_handler(self):
        self.change_state()
        t = threading.Thread(target=self.plotter)
        t.setDaemon(True)
        t.start()

    def change_state(self):
        if self.continuePlotting:
            self.continuePlotting = False
            self.pause['state'] = 'disabled'
            self.start['state'] = 'normal'
        else:
            self.continuePlotting = True
            self.start['state'] = 'disabled'
            self.pause['state'] = 'normal'

    def plotter(self):
        while self.continuePlotting:
            self.ax.cla()
            self.ax.grid()
            self.ax.title.set_text('ECG Monitoring')
            self.ax.set_xlabel("Time [mS]")
            self.ax.set_ylabel("Amplitude [V/mV]")
            self.dpts, self.time = data_points()
            self.ax.plot(range(20), self.dpts, color='orange')
            self.ax.axis(ymin=-2, ymax=None)
            self.graph.draw()


    def screen_shot(self):
        global png_name

        if filepath == "":
            png_name = 'Screenshot(s)/' + '{0}_{1}_ECG_DIY.png'.format(name, date)
        else:
            png_name = filepath + '/{0}_{1}_ECG_DIY.png'.format(name, date)

        self.graph.draw()
        self.fig.savefig(png_name, bbox_inches='tight')
        notification.notify(
            title='ScreenShot Location',
            message= png_name,
            app_name='MSOE DIY-ECG',
            timeout=3,
            app_icon='./imports/msoe.ico'
        )

    def terminate(self):
        self.continuePlotting = False
        self.graph.close_event()
        self.fig.clear()


"""
This class will create a main window title, size and grid path 
of the GUI it will also import a small icon for its display
"""


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('DIY-ECG')
        self.resizable(False, False)
        # ensure that a window is always at the top of the stacking order
        self.attributes('-topmost', 1)

        """ CONFIGURE THE GRID OF THE GUI"""
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        window_width = 300
        window_height = 200

        # get screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        # create the screen on window console
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # changing the Tinker Logo into the MSOE logo instead for our development
        self.iconbitmap('./imports/msoe.ico')
        frm = ttk.Frame(self, padding=1)
        frm.grid()


"""
Main function and runs code settings information 
"""
if __name__ == "__main__":
    print("GUI.PY SHOULD NOT BE RUN, WARNING!!!.\n")
