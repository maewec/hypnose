# -*- coding: utf-8 -*-

import tkinter as tk

class Circle:
    def __init__(self, canvas, center, radius, thickness, color='green', inc=10):
        self.canvas = canvas
        self.center = center
        self.radius = radius
        self.thickness = thickness
        self.color = color
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
        self.create()

    def rotate(self, angle=None):
        if self.start > 360:
            self.start -= 360
        if angle:
            self.start += angle
        else:
            self.start += self.ang_rot
        self.canvas.delete(self.arc)
        self.create()

    def __del__(self):
        self.canvas.delete(self.oval)

def increase(event, obj):
    obj.increase()

root = tk.Tk()
canv = tk.Canvas(root, width=600, height=600, bg='white')
canv.pack()
but = tk.Button(root, text='Расширить')
but.pack()

oval = Circle(canv, (300, 300), 100, 10, 'blue')

but.bind('<Button-1>', lambda event: increase(event, oval))
root.mainloop()
