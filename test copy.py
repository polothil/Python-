# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:25:31 2019

@author: mm
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr

# ------global variables
data = np.array([])
cond = False

# -----plot data-----


def plot_data():
    global cond, data

    if (cond == True):

        a = s.readline()
        a.decode()

        if(len(data) < 500):
            data = np.append(data, float(a[0:4]))
        else:
            data[0:499] = data[1:500]
            data[499] = float(a[0:4])

        lines.set_xdata(np.arange(0, len(data)))
        lines.set_ydata(data)

        canvas.draw()

    root.after(1, plot_data)


def plot_start():
    global cond
    cond = True
    s.reset_input_buffer()


def plot_stop():
    global cond
    cond = False


# -----Main GUI code-----
root = tk.Tk()
root.title('Real Time Plot of Serial Data')
root.configure(background='light blue')
root.geometry("1000x700")  # set the window size

# ------create Plot object on GUI----------
# add figure canvas
fig = Figure()
ax = fig.add_subplot(111)

ax.set_title('Serial Data')
ax.set_xlabel('Sample')
ax.set_ylabel('Intensity')
ax.set_xlim(0, 500)
ax.set_ylim(0, 1024)
lines = ax.plot([], [])[0]

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().place(x=10, y=10, width=900, height=600)
canvas.draw()

# ----------create button---------
root.update()
start = tk.Button(root, text="Start", font=(
    'calbiri', 12), command=plot_start)
start.place(x=100, y=650)

root.update()
stop = tk.Button(root, text="Stop", font=(
    'calbiri', 12), command=plot_stop)
stop.place(x=start.winfo_x()+start.winfo_reqwidth() + 20, y=650)

# ----start serial port----
s = sr.Serial('COM3', 9600)
s.reset_input_buffer()


root.after(1, plot_data)
root.mainloop()
