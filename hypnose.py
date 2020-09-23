# -*- coding: utf-8 -*-

import tkinter as tk
import math

color_list = ('black', 'blue', 'cyan', 'gray', 'cyan', 'orange') * 10

class Circle:
    count = 0

    def __init__(self, canvas, center, radius, thickness, color=None, inc=10):
        self.id = Circle.count
        Circle.count += 1

        self.canvas = canvas
        self.center = center
        self.radius = radius
        self.thickness = thickness
        if color:
            self.color = color
        else:
            self.color = color_list[self.id]
        self.inc=inc
        self.create()

    def create(self):
        x, y = self.center
        x0 = x - self.radius
        x1 = x + self.radius
        y0 = y - self.radius
        y1 = y + self.radius
        self.oval = self.canvas.create_oval(x0, y0, x1, y1, width=self.thickness,
                                           outline=self.color)

    def increase(self):
        self.canvas.delete(self.oval)
        self.radius += self.inc
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])
        if self.radius > math.sqrt(width**2 + height**2)/2:
            self.radius = 10
        self.create()

    def __del__(self):
        self.canvas.delete(self.oval)

def increase(event, obj):
    for i in obj:
        i.increase()
    root.after(50, lambda: increase(event, obj))

root = tk.Tk()
canv = tk.Canvas(root, width=600, height=600, bg='white')
canv.pack()
but = tk.Button(root, text='Расширить')
but.pack()

rad_list = [x for x in range(20, 500, 10)]
oval_list = [Circle(canv, (300, 300), x, 11, inc=10) for x in rad_list]
#oval = Circle(canv, (300, 300), 100, 11, 'blue')

but.bind('<Button-1>', lambda event: increase(event, oval_list))
root.mainloop()
