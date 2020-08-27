# https://ishantheperson.github.io/posts/tkinter-matplotlib/
# https://www.youtube.com/watch?v=0V-6pu1Gyp8&t=255s

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter as tk
# from tkinter.ttk import *
import numpy as np
import serial as sr
from tkinter.filedialog import asksaveasfile
import matplotlib
matplotlib.use("TkAgg")

# ------global variables
data = np.array([], dtype=float)
save_data = data_1 = data_2 = data_3 = data_4 = data_5 = np.array(
    [], dtype=float)
condition = False

# -----plot data-----


def plot_data():
    global condition, data, save_data

    if (condition == True):

        serial_read = s.readline()
        serial_read.decode()

        save_data = np.append(save_data, float(serial_read[0:4]))

        if(len(data) < 300):
            data = np.append(data, float(serial_read[0:4]))
        else:
            data[0:299] = data[1:300]
            data[299] = float(serial_read[0:4])

        lines.set_xdata(np.arange(0, len(data)))
        lines.set_ydata(data)

        canvas.draw()

    root.after(1, plot_data)


def plot_start():
    global condition
    condition = True
    s.reset_input_buffer()


def plot_stop():
    global condition
    condition = False
    s.reset_input_buffer()


def save_fn1():
    plot_stop()
    data_1 = save_data
    # print(save_data)
    np.savetxt('Data_1.txt', data_1, fmt='%d', delimiter=',')
    s.reset_input_buffer()


def save_fn2():
    plot_stop()
    data_2 = save_data
    # print(save_data)
    np.savetxt('Data_2.txt', data_2, fmt='%d', delimiter=',')
    s.reset_input_buffer()


def save_fn3():
    plot_stop()
    data_3 = save_data
    # print(save_data)
    np.savetxt('Data_3.txt', data_3, fmt='%d', delimiter=',')
    s.reset_input_buffer()


def save_fn4():
    plot_stop()
    data_4 = save_data
    # print(save_data)
    np.savetxt('Data_4.txt', data_4, fmt='%d', delimiter=',')
    s.reset_input_buffer()


def save_fn5():
    plot_stop()
    data_5 = save_data
    # print(save_data)
    np.savetxt('Data_5.txt', data_5, fmt='%d', delimiter=',')
    s.reset_input_buffer()


# -----Main GUI code-----
root = Tk()
root.title('Real Time Plot of Serial Data')
# root.configure(background='light blue')


figure = Figure(figsize=(10, 4), dpi=100)
data_plot = figure.add_subplot(1, 1, 1)

data_plot.set_title('Real Time Serial Data')
data_plot.set_xlabel('Time')
data_plot.set_ylabel('Intensity')
data_plot.set_xlim(0, 300)
data_plot.set_ylim(0, 1024)
lines = data_plot.plot([], [])[0]  # To maintain the axis to be static

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, columnspan=5)

# ----------create button---------
root.update()
start = tk.Button(root, text="Start", font=('calbiri', 12), command=plot_start)
start.grid(row=2, column=1, pady=20)

root.update()
stop = tk.Button(root, text="Stop", font=('calbiri', 12), command=plot_stop)
stop.grid(row=2, column=2)

root.update()
plot_all = tk.Button(root, text="Plot All", font=('calbiri', 12))
plot_all.grid(row=2, column=3)

root.update()
save_btn1 = tk.Button(root, text="Save Data 1",
                      font=('calbiri', 12), command=save_fn1)
save_btn1.grid(row=3, column=0, pady=20)

root.update()
save_btn2 = tk.Button(root, text="Save Data 2",
                      font=('calbiri', 12), command=save_fn2)
save_btn2.grid(row=3, column=1)

root.update()
save_btn3 = tk.Button(root, text="Save Data 3",
                      font=('calbiri', 12), command=save_fn3)
save_btn3.grid(row=3, column=2)

root.update()
save_btn4 = tk.Button(root, text="Save Data 4",
                      font=('calbiri', 12), command=save_fn4)
save_btn4.grid(row=3, column=3)

root.update()
save_btn5 = tk.Button(root, text="Save Data 5",
                      font=('calbiri', 12), command=save_fn5)
save_btn5.grid(row=3, column=4)

# ----start serial port----
s = sr.Serial('COM3', 9600)
s.reset_input_buffer()

root.after(1, plot_data)

root.mainloop()
