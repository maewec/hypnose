# -*- coding: utf-8 -*-

import tkinter as tk

class Circle:
    def __init__(self, canvas, center, radius, thickness, color='green'):
        self.canvas = canvas
        self.center = center
        self.radius = radius
        self.thickness = thickness
        self.start = 0
        self.color = color
        self.create()

    def create(self):
        x, y = self.center
        x0 = x - self.radius
        x1 = x + self.radius
        y0 = y - self.radius
        y1 = y + self.radius
        self.oval = self.canvas.create_oval(x0, y0, x1, y1, start=self.start,
                                          extent=self.ang, style='arc',
                                          outline=self.color, width=self.thickness)

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
        self.canvas.delete(self.arc)


root = tk.Tk()
canv = tk.Canvas(root, width=600, height=600, bg='white')
canv.pack()

arc = Arc(canv, (300, 300), 100, 10, 365, 'blue', 10)

root.mainloop()
