import cv2
import tkinter as tk
from PIL import Image, ImageTk
import mediapipe as mp
import pyautogui
import simpleaudio as sa
from SELFfunction import * 

def startProg():
    #destroying the current window and starting a new one
    root.destroy()
    start_program()


root = tk.Tk()
root.title('CaptureImg')
root.iconbitmap('camera.ico')
root.geometry("800x800")
root.resizable(False, False)

start_btn = tk.PhotoImage( file='start.png')
img_label = tk.Label(image= start_btn)
start_button = tk.Button(root, image= start_btn, command=startProg, borderwidth=0)
start_button.pack()




root.mainloop()