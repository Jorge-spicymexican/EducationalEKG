# these two imports are important
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
from tkinter import *
from random import randint
import threading

continuePlotting = False


def change_state():
    global continuePlotting
    if continuePlotting == True:
        continuePlotting = False
    else:
        continuePlotting = True


def data_points():
    f = open("./data.txt", "w")
    for i in range(10):
        f.write(str(randint(0, 10)) + '\n')
    f.close()

    f = open("./data.txt", "r")
    data = f.readlines()
    f.close()

    l = []
    for i in range(len(data)):
        l.append(int(data[i].rstrip("\n")))
    return l


def app():
    # initialise a window.
    root = Tk()
    root.config(background='white')
    root.geometry("700x500")

    lab = Label(root, text="Live Plotting", bg='white').pack()

    fig = Figure()

    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()

    graph = FigureCanvasTkAgg(fig, master=root)
    graph.get_tk_widget().pack(side="top", fill='both', expand=True)

    def plotter():
        while continuePlotting:
            print("inside plotter statment")
            ax.cla()
            ax.grid()
            dpts = data_points()
            ax.plot(range(10), dpts, marker='o', color='orange')
            graph.draw()
            time.sleep(1)

    def gui_handler():
        change_state()
        threading.Thread(target=plotter).start()

    b = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    b.pack()

    root.mainloop()


if __name__ == '__main__':
    app()

"""

class DataSource:
    data = []
    display = 25

    # Append one random number and return last 10 values
    def getData(self):
        self.data.append(np.random.rand(1)[0])
        if(len(self.data) <= self.display):
            return self.data
        else:
            return self.data[-self.display:]

    # Return the index of the last 10 values
    def getIndexVector(self):
        if(len(self.data) <= self.display):
            return list(range(len(self.data)))

        else:
            return list(range(len(self.data)))[-self.display:]


x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.ion()

figure, ax = plt.subplots(figsize=(8, 6))
line1, = ax.plot(x, y)

plt.title("Dynamic Plot of sinx", fontsize=25)

plt.xlabel("X", fontsize=18)
plt.ylabel("sinX", fontsize=18)

for p in range(100):
    updated_y = np.cos(x - 0.05 * p)

    line1.set_xdata(x)
    line1.set_ydata(updated_y)

    figure.canvas.draw()

    figure.canvas.flush_events()

"""