#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:58:08 2019

@author: lov35174
"""

import tkinter as tk
from tkinter import Label,Radiobutton, IntVar, Entry, LabelFrame, Message, StringVar, Button, messagebox
import pylab as lab


class Application(tk.Tk):
    name = 'Graf funkce'
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth=5)
        
        self.grflblfr=LabelFrame(self,text=u"Generuj graf funkce", padx=20)
        self.grflblfr.grid(row=1,column=1)
        
        self.fcelbl=Label(self.grflblfr)
        self.fcelbl.grid(row=1, column=1)
        
        self.v = IntVar()
        
        self.sinrdb=Radiobutton(self.fcelbl,text=u"sin",variable=self.v, value=1)
        self.sinrdb.grid(row=1,column=1)
        
        self.logrdb=Radiobutton(self.fcelbl,text=u"log",variable=self.v, value=2)
        self.logrdb.grid(row=2,column=1) 
        
        self.exprdb=Radiobutton(self.fcelbl,text=u"exp",variable=self.v, value=3)
        self.exprdb.grid(row=3,column=1)
        
        self.oddolbl=Label(self.grflblfr)
        self.oddolbl.grid(row=1, column=2)
        
        self.odmess = Message(self.oddolbl, text=u"Od:")
        self.odmess.grid(row=1, column=1)
        
        self.sod=StringVar()
        
        self.odentr=Entry(self.oddolbl, textvariable=self.sod,width=10)
        self.odentr.grid(row=1,column=2)
        
        self.domess = Message(self.oddolbl, text=u"Do:")
        self.domess.grid(row=2, column=1)
        
        self.sdo=StringVar()
        
        self.doentr=Entry(self.oddolbl, textvariable=self.sdo,width=10)
        self.doentr.grid(row=2,column=2)
        
        self.vga=Button(self,text=u"Vytvoř graf", width=7, height=4, command=self.vytgraf)
        self.vga.grid(row=1,column=2)
        
        self.grftxtlblfr=LabelFrame(self,text=u"Generuj graf z textových dat", padx=25)
        self.grftxtlblfr.grid(row=2,column=1)
        
        self.a=StringVar()
        self.a.set("")
        
        self.csentr=Entry(self.grftxtlblfr, textvariable=self.a)
        self.csentr.grid(row=1,column=1)
        
        self.vga=Button(self.grftxtlblfr,text=u"Vyber soubor")
        self.vga.grid(row=2,column=1)
        
        self.vgb=Button(self,text=u"Vytvoř graf", width=7, height=4)
        self.vgb.grid(row=2,column=2)
        
        self.osylblfr=LabelFrame(self,text=u"Popisky os", padx=40)
        self.osylblfr.grid(row=3,column=1)
        
        self.osxmess = Message(self.osylblfr, text=u"Osa X:")
        self.osxmess.grid(row=1, column=1)
        
        self.osx=StringVar()
        
        self.osxentr=Entry(self.osylblfr, textvariable=self.osx,width=10)
        self.osxentr.grid(row=1,column=2)
        
        self.osymess = Message(self.osylblfr, text=u"Osa Y:")
        self.osymess.grid(row=2, column=1)
        
        self.osy=StringVar()
        
        self.osyentr=Entry(self.osylblfr, textvariable=self.osy,width=10)
        self.osyentr.grid(row=2,column=2)
        
    def vytgraf(self):
        try:
            od=float(self.sod.get())
            do=float(self.sdo.get())
            x=lab.linspace(od, do, 500)
            if self.v.get() == 1:
                y=lab.sin(x)
            elif self.v.get() == 2:
                y=lab.log10(x)
            elif self.v.get() == 3:
                y=lab.exp(x)
            lab.figure()
            lab.plot(x,y)
            lab.xlabel(self.osx.get())
            lab.ylabel(self.osy.get())
            lab.grid(True)
            lab.show()
        except:
            messagebox.showerror(title='Chybné meze', message='Zadejte meze osy X\njako reálná čísla')        

app = Application()
app.mainloop()
