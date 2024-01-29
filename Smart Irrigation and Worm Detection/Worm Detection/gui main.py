# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''

root=tk.Tk()

root.title("Smart Irrigation and worm Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

# bg = Image.open(r"E:/carrier_choice_prediction/y9.jpg")
# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# bg_lbl.place(x=0,y=93)
# #, relwidth=1, relheight=1)

video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("new1.mp4", video_label,loop = 1, size = (w, h))
player.play()

w = tk.Label(root, text="Smart Irrigation and worm Detection",width=85,background="#800517",foreground="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800517")

text="Lorem Ipsum"



from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="......Welcome to Smart Irrigation and worm Detection......",width=120,height=3,background="#800517",foreground="white",font=("Times new roman",19,"bold"))
wlcm.place(x=0,y=620)




d2=tk.Button(root,text="Login",command=Login,width=20,height=2,bd=0,background="#800517",foreground="white",font=("times new roman",17,"bold"))
d2.place(x=1100,y=0)


d3=tk.Button(root,text="Register",command=Register,width=20,height=2,bd=0,background="#800517",foreground="white",font=("times new roman",17,"bold"))
d3.place(x=1300,y=0)



root.mainloop()
