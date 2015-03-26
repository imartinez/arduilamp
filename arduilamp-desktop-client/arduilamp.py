#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial, time
import Tkinter as tk
from Tkinter import *
from tkColorChooser import askcolor 

SERIALPORT = "/dev/tty.usbmodem1431"
# Set up serial port
try:
    ser = serial.Serial(SERIALPORT, 9600)
except serial.SerialException:
    print "no device connected - exit"
    sys.exit()

ser.write("R0")
ser.write("G0")
ser.write("B0")

class App:
  
    def __init__(self):        

        self.root = tk.Tk()
        self.root.wm_title("Lamp!")
        self.root.geometry('{}x{}'.format(200, 170))
        self.root.protocol("WM_DELETE_WINDOW", self.handler)
        self._job = None
        self.sliderR = tk.Scale(self.root, from_=0, to=255, 
                               orient="horizontal", 
                               command=self.updateRValue)
        self.sliderR.pack()
        self.sliderG = tk.Scale(self.root, from_=0, to=255, 
                               orient="horizontal", 
                               command=self.updateGValue)
        self.sliderG.pack()
        self.sliderB = tk.Scale(self.root, from_=0, to=255, 
                               orient="horizontal", 
                               command=self.updateBValue)
        self.sliderB.pack() 
        Button(text='Select Color', command=self.getColor).pack()       
        self.root.mainloop()

    def updateRValue(self, event):
        if self._job:
            self.root.after_cancel(self._job)
        self._job = self.root.after(500, self._update_R_arduino)

    def _update_R_arduino(self):
        self._job = None
        print "new R value:", self.sliderR.get()
        ser.write("R" + str(self.sliderR.get()))

    def updateGValue(self, event):
        if self._job:
            self.root.after_cancel(self._job)
        self._job = self.root.after(500, self._update_G_arduino)

    def _update_G_arduino(self):
        self._job = None
        print "new G value:", self.sliderG.get()
        ser.write("G" + str(self.sliderG.get()))   

    def updateBValue(self, event):
        if self._job:
            self.root.after_cancel(self._job)
        self._job = self.root.after(500, self._update_B_arduino)

    def _update_B_arduino(self):
        self._job = None
        print "new B value:", self.sliderB.get()
        ser.write("B" + str(self.sliderB.get()))     
    
    def getColor(self):
        color = askcolor() 
        if color != None:
            ser.write("R" + str(color[0][0]))               
            print "new R value:", str(color[0][0])  
            self.sliderR.set(color[0][0])
            time.sleep(0.1)
            ser.write("G" + str(color[0][1]))
            print "new G value:", str(color[0][1])
            self.sliderG.set(color[0][1])
            time.sleep(0.1)
            ser.write("B" + str(color[0][2]))
            print "new B value:", str(color[0][2])
            self.sliderB.set(color[0][2])
            time.sleep(0.1)
        print color

    def handler(self):
        self.root.quit()
        ser.close
        
app=App()


