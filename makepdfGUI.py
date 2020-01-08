# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog,messagebox
import ntpath
import subprocess
import glob
import threading
import sys
import os
import shutil

ctext = ""
dir = ntpath.dirname(__file__)
savedir = ""
pdffile = ""

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        global var
        var = tk.StringVar()
        var.set("Select image directory")
        self.lbl = tk.Label(root, textvariable=var)
        self.lbl.place(x=50, y=10)

        self.button1 = tk.Button(root)
        self.button1["text"] = "Set output pdf"
        self.button1["command"] = self.savepdf
        self.button1.place(x=20, y=50)

        self.button2 = tk.Button(root)
        self.button2["text"] = "Set IMG Dir"
        self.button2["command"] = self.thread
        self.button2.place(x=120, y=50)

        self.button3 = tk.Button(root)
        self.button3["text"] = "Config"
        self.button3["command"] = self.create_window
        self.button3.place(x=210, y=50)

        self.quit = tk.Button(root, text="Quit")
        self.quit["command"] = self.appQuit
        self.quit.place(x=300, y=50)

    def create_window(self):
        global t, text
        t = tk.Toplevel(self)
        t.geometry("350x100")
        t.wm_title("API KEY Config")
        l = tk.Label(t, text="Set Google API key")
        l.place(x=100, y=5)
        text = tk.Entry(t, width=20)
        text.place(x=90, y=30)
        button3 = tk.Button(t)
        button3.place(x=150, y=60)
        button3["text"] = "Save"
        button3["command"] = self.saveconfig

    def makepdf(self):

        if pdffile=="":
            messagebox.showerror("Error", 'Set pdf file before set images')
            self.savepdf()
            sys.exit(1)

        imgdir = filedialog.askdirectory(initialdir = dir)
        
        try:
            files = sorted(glob.glob(imgdir+"/*jpg"))
        except TypeError:                                  # cancel
            sys.exit(1)

        gcvocr = ntpath.dirname(__file__)+"/gcvocr.exe"

        confpath = ntpath.dirname(__file__)+"/config.txt"
        try:
            with open(confpath) as f:
                APIKEY = f.read()
        except FileNotFoundError:
            messagebox.showerror("Error", 'No config file, Input your API key')
            self.create_window()
            sys.exit(1)

        if APIKEY == "":
            messagebox.showerror("Error", 'No API key, Input your API key')
            self.create_window()
            sys.exit(1)
        
        if savedir == "":
            messagebox.showerror("Error", 'Set output pdf folder')
            self.savepdf()
            sys.exit(1)

        for name in files:
            print("google OCR", ntpath.basename(name))
            var.set("google OCR " + ntpath.basename(name))
            command = [gcvocr, name, APIKEY, savedir + "/temp"]
            subprocess.call(command)
 
            print ("Convert ", ntpath.basename(name) ,"to hocr")
            var.set("Convert " + ntpath.basename(name) + " to hocr")
            hocr = imgdir + "/" + ntpath.basename(name).replace("jpg", "hocr")
            json = savedir + "/temp/" + ntpath.basename(name).replace("jpg", "jpg.json")
            gcv2hocr = ntpath.dirname(__file__)+"/gcv2hocr.exe"
            command = [gcv2hocr, json, hocr]
            subprocess.call(command)

        print("Generating pdf")
        var.set("Generating pdf")
        hocr_pdf = ntpath.dirname(__file__)+"/hocr-pdf.exe"

        command = [hocr_pdf, "--savefile", pdffile, imgdir]
        subprocess.call(command)
        move_glob(savedir + "/temp/", imgdir + "/*.hocr")
        move_glob(savedir + "/temp/", imgdir + "/*.txt")
        move_glob(savedir + "/temp/", ntpath.dirname(__file__) + "/preout*.txt")        

        print("Done!")
        var.set("Done!")
        sys.exit(1)

    def thread(self):
        global th
        th = threading.Thread(target=self.makepdf)
        th.start()

    def appQuit(self):
        sys.exit(0)

    def saveconfig(self):
        ctext = text.get()
        if ctext == "":
            messagebox.showerror("Error", "No API KEY") 
            t.destroy()
            sys.exit(1)
        path = ntpath.dirname(__file__)+"/config.txt"
        with open(path, mode='w') as f:
            f.write(ctext)
        t.destroy()

    def savepdf(self):
        global pdffile, savedir
        pdffile = filedialog.asksaveasfilename(filetypes = [("pdf file",'*.pdf')], initialdir = dir)        
        savedir = ntpath.dirname(pdffile)
        os.mkdir(savedir + "/temp")

def move_glob(dst_path, pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        shutil.move(p, dst_path)

root = tk.Tk()
root.geometry("400x100")
root.title("Make pdf")
app = Application(master=root)
app.mainloop()