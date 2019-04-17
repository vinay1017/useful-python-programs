# A way to toggle a created object's color in Tkinter. Green to red, red to green.
# This is extracted from a school project. Thought it was an interesting and useful piece of code
# that took me a moment to create and understand logically.

import tkinter as tk
from tkinter import *

class room_visualizer():
    sensor = ...  # type: bool

    def __init__(self, canvas, start_x, start_y, size, text, sensor):
        """
        :param canvas: obj. Uses the canvas instance, probably called w.
        :param start_x: int. Starting x location.
        :param start_y: int. Starting y location.
        :param size: int. Size of appliance square. 300 for all rooms.
        :param text str. What the room is called.
        :param sensor: bool. True means green/on, False means red/off.
        """
        self.canvas = canvas
        self.sensor = sensor
        self.text = text
        self.start_x = start_x
        self.start_y = start_y
        self.size = size

        # self.room = room_visualizer(self.canvas, self.start_x, self.start_y, self.size, self.text, self.sensor)

        if self.sensor == False:
            self.id = self.canvas.create_rectangle((start_x, start_y, start_x + size, start_y + size), fill="red")
            self.canvas.update_idletasks()
        else:
            self.id = self.canvas.create_rectangle((start_x, start_y, start_x + size, start_y + size), fill="green")
            self.canvas.update_idletasks()

        self.textCanvas = canvas.create_text(start_x + size / 2, start_y + size / 2, text=text)
        self.canvas.tag_bind(self.id, "<ButtonPress-1>", self.set_color)
        self.color_change = True
        self.canvas.update_idletasks()

    def __str__(self):
        return str(self.text)

    def set_color(self, event=None):
        self.color_change = not self.color_change
        color = "red"
        # areLightsOff = True  # this could be useful for telling if a room light is off or on.
        if not self.color_change:
            color = "green"
            # areLightsOff = False
            print(self.text + " Turned on")
        else:
            print(self.text + " Turned Off")
        self.canvas.itemconfigure(self.id, fill=color)

# Useful for combining two methods' functionality together.
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def masterRoom():
    master = list()
    master.append(bedroom)
    master.append(bathroom)
    master.append(newroom)
    print(master)
    for i in master:
        i.set_color()

app = Tk()
canvas = Canvas(app, width=300, height=300)
canvas.grid(column=0, row=2)
bedroom = room_visualizer(canvas, 0, 0, 100, "BedRoom", True)
bathroom = room_visualizer(canvas, 200, 0, 100, "BathRoom", True)
newroom = room_visualizer(canvas, 100, 200, 100, "BathRoom", True)


button1 = tk.Button(text="toggle color", command=masterRoom)  # this is so close to WHAT I NEED
button1.grid(column=1, row=2)

app.geometry("")
app.title("GUI")

app.mainloop()
