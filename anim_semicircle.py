# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:04:43 2020

@author: root
"""

import tkinter as tk
import time

flag = True
flag_razv = True

def flag_set(event, fl):
    global flag
    flag = fl
    
def flag_set_true(event, lst):
    global flag
    flag = True
    make(event, lst)


def make(event, lst):
    for obj in lst:
        obj.rotate()
    if flag:
        root.after(50, lambda: make(event, lst))

    
class Arc:
    def __init__(self, canvas, center, radius, thickness, ang=180, color='green',
                 ang_rot=0):
        self.canvas = canvas
        self.center = center
        self.radius = radius
        self.thickness = thickness
        self.start = 0
        self.ang = ang
        self.color = color
        self.ang_rot = ang_rot
        self.create()
        
    def create(self):
        x, y = self.center
        x0 = x - self.radius
        x1 = x + self.radius
        y0 = y - self.radius
        y1 = y + self.radius
        self.arc = self.canvas.create_arc(x0, y0, x1, y1, start=self.start,
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
        
def form_arc(event):
    global flag_razv
    if flag_razv:
        param_arc = [[x*10, x*1] for x in range(1, 19)]
        flag_razv = False
        form_arc_list(param_arc)
    else:
        param_arc = [[x*10, x*1] for x in range(1, 19)]
        param_arc = [[x, -y] if y%2==0 else [x, y] for x, y in param_arc]
        form_arc_list(param_arc)
        flag_razv = True

def form_arc_list(parav_arc):
    global arc_list
    if arc_list:
        for obj in arc_list:
            del obj
    arc_list = []
    for rad, rot in param_arc:
        arc_list.append(Arc(canv, (300, 300), rad, 11, ang_rot=rot))


root = tk.Tk()
canv = tk.Canvas(root, width=600, height=600, bg='white')
#canv.focus_set()
canv.pack()
but = tk.Button(text='Вращать')
but.pack()
but2 = tk.Button(text='Остановить')
but2.pack()
but0 = tk.Button(text='Развернуть')
but0.pack()


param_arc = [[x*10, x*1] for x in range(1, 19)]
#param_arc = [[x, -y] if y%2==0 else [x, y] for x, y in param_arc]

arc_list = []
for rad, rot in param_arc:
    arc_list.append(Arc(canv, (300, 300), rad, 11, ang_rot=rot))

but.bind('<Button-1>', lambda event: flag_set_true(event, arc_list))
but2.bind('<Button-1>', lambda event: flag_set(event, False))
but0.bind('<Button-1>', lambda event: form_arc(event))


root.mainloop()