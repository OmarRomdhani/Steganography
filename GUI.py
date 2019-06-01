from tkinter import *
from tkinter.filedialog import *
import numpy as np
from scipy import misc
from tkinter import messagebox
from math import *
from PIL import ImageTk, Image
from SteganographyMethod1 import *
from SteganographyMethod2 import *

import matplotlib.pyplot  as plt
def alert():
    messagebox.showwarning("Alert","Sorry This command is still under construction")
    print(0)
class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("Steganography")
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Open image", command=self.add_image)
        menu1.add_command(label="Save as", command=alert)
        menu1.add_command(label="Save", command=alert)
        menu1.add_separator()
        menu1.add_command(label="Quit", command=self.quit)
        menubar.add_cascade(label="File", menu=menu1)
        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="insert", command=alert)
        menu2.add_command(label="Copy", command=alert)
        menu2.add_command(label="Past", command=alert)
        menubar.add_cascade(label="Edit", menu=menu2)
        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Help", command=alert)
        menubar.add_cascade(label="?", menu=menu3)
        # frame 1
        self.Frame1 = Frame(root, borderwidth=2, relief=GROOVE)
        self.Frame1.pack(side=TOP,padx=0, pady=0,fill=BOTH)
        # frame 2
        self.Frame2 = Frame(root, borderwidth=2, relief=GROOVE)
        self.Frame2.pack(side=TOP,expand=Y,fill=BOTH, padx=1, pady=1)
        # frame 3 dans frame 2
        self.Frame3 = Frame(self.Frame2,width=540, height=360, borderwidth=2, relief=GROOVE)
        self.Frame3.pack(side=LEFT,fill=BOTH, padx=1, pady=1)
        # Ajout de labels
        Label(self.Frame1,bg='red',text="Steganography",anchor=CENTER).pack(fill=BOTH)
        Label(self.Frame2, text="Choose settings:").pack(padx=10, pady=10)
        self.note=Label(self.Frame3,foreground="red", text="Leave it empty to read from a file ")
        #Canvas
        self.canvas = Canvas(self.Frame3,width=540, height=540)
        #button
        self.value = StringVar()
        self.value.set(1)
        self.button1 = Radiobutton(self.Frame2, text="First Method", variable=self.value, value=1 ,command=self.Send)
        self.button2 = Radiobutton(self.Frame2, text="Second Method", variable=self.value, value=2, command=self.Send)
        self.button1.pack(anchor=W)
        self.button2.pack(anchor=W)
        #send button
        #self.button=Button(self.Frame2, text="Next", command=self.Send)
        #self.button.pack()
        Frame(self.Frame2, borderwidth=0, relief=GROOVE,heigh=20).pack(side=TOP,padx=0, pady=0,fill=BOTH)

        
        #list method 1
        self.method1=["2Red-3Green-3Blue","3Red-2Green-3Blue","3Red-3Green-2Blue"]
        self.listM = Listbox(self.Frame2,height=6,width=20)
       
        
        #list method 2
        self.method2=["Red-Green-Blue","Green-Blue-Red","Blue-Red-Green","Red-Blue-Green","Green-Red-Blue","Blue-Green-Red"]
        
        #button cryptage/decryptage 
        
        self.value2= StringVar()
        self.value2.set(1)
        self.button2_1 = Radiobutton(self.Frame2, text="Hide message ", variable=self.value2, value=1,command=self.Send3)
        self.button2_2 = Radiobutton(self.Frame2, text="retrieve message", variable=self.value2, value=2,command=self.Send3)
        
        #send button cryptage /decryptage 
        #self.button3=Button(self.Frame2, text="Next", command=self.Send3)
        
        self.text=Text(self.Frame3,height=6)
        #send button cryptage 
        self.button4=Button(self.Frame2, text="")
        self.text=Text(self.Frame3,height=6)
        self.path=None
        self.Send()
        self.Send3()
    def Send3 (self):
        self.text.config(state=NORMAL)
        self.text.pack(side=BOTTOM)
        self.text.delete('1.0',END)
        if (int(self.value2.get())==1):
            self.note.config(text="Leave it empty to read text from a file ")
            self.note.pack(side=BOTTOM)
            self.button4.config(text="Hide",command=self.Hide)
        else :
            self.note.config(text="")
            self.text.insert(END,"""<You can not write ! Message will be writen here.>""")
            self.text.config(state=DISABLED)
            self.button4.config(text="retrieve",command=self.Retrive)
        self.button4.pack()
    def Hide(self):
        self.text.config(state=NORMAL)
        if (self.path==None):
            self.add_image()
        if 0==len(str(self.path).strip()):
            messagebox.showwarning("Error","No image was selected")
            return;
        msg=self.text.get("1.0",END)
        if (len(msg)<=1):
            patht=askopenfilename(title="Open a text file",filetypes=[('txt files','.txt'),('all files','.*')])
            if 0==len(str(patht).strip()):
                messagebox.showwarning("Error","No text-file was selected")
                return;
            file=open(patht,'r')
            msg=file.read()
            file.close()
        item= self.listM.curselection()
        try:
            self.listM.get(item)
        except :
            messagebox.showwarning("Alert","Choose a method")
            return
        try :
            if int(self.value.get())==1:
                if item[0]==0:
                    SteganographyHideMethod1(msg,self.path,2,3,3)
                if item[0]==1:
                    SteganographyHideMethod1(msg,self.path,3,2,3)
                if item[0]==2:
                    SteganographyHideMethod1(msg,self.path,3,3,2)
            else:
                if item[0]==0:
                    SteganographyHideMethod2(msg,self.path,0,1,2)
                if item[0]==1:
                    SteganographyHideMethod2(msg,self.path,1,2,0)
                if item[0]==2:
                    SteganographyHideMethod2(msg,self.path,2,0,1)
                if item[0]==3:
                    SteganographyHideMethod2(msg,self.path,0,2,1)
                if item[0]==4:
                    SteganographyHideMethod2(msg,self.path,1,0,2)
                if item[0]==5:
                    SteganographyHideMethod2(msg,self.path,2,1,0)
        except :
            messagebox.showwarning("Error","No image was selected")
            return;         
    def Retrive(self):
        if (self.path==None):
            self.add_image()

        if 0==len(str(self.path).strip()):
            messagebox.showwarning("Error","No image was selected")
            return;
            
        self.text.config(state=NORMAL)
        self.text.delete('1.0',END)
        item= self.listM.curselection()
        try:
            self.listM.get(item)
        except :
            messagebox.showwarning("Alert","Choose a method")
            return
        msg=''
        if int(self.value.get())==1:
            if item[0]==0:
                msg=SteganographyRetriveMethod1(self.path,2,3,3)
            if item[0]==1:
                msg=SteganographyRetriveMethod1(self.path,3,2,3)
            if item[0]==2:
                msg=SteganographyRetriveMethod1(self.path,3,3,2)
        else:
            if item[0]==0:
                msg=SteganographyRetriveMethod2(self.path,0,1,2)
            if item[0]==1:
                msg=SteganographyRetriveMethod2(self.path,1,2,0)
            if item[0]==2:
                msg=SteganographyRetriveMethod2(self.path,2,0,1)
            if item[0]==3:
                msg=SteganographyRetriveMethod2(self.path,0,2,1)
            if item[0]==4:
                msg=SteganographyRetriveMethod2(self.path,1,0,2)
            if item[0]==5:
                msg=SteganographyRetriveMethod2(self.path,2,1,0)
             
        if len(msg)>2000 :
            messagebox.showwarning('Message too long  ', "Message will be saved in a file:")
            patht=asksaveasfilename(defaultextension=".txt",filetypes=[('txt files','.txt')])
            file=open(patht,"w")
            file.write(msg)
            file.close()
            self.text.insert(END,"<Message will be saved in a file:>")
        else :
            self.text.insert(END,msg)
            self.text.config(state=DISABLED)
    def Send(self):
        try:
            self.listM.delete(0,END)
        except:
            pass
        if (int(self.value.get())==1):
            for i in self.method1:
                self.listM.insert(END,i)
        else :
            for i in self.method2:
                self.listM.insert(END,i)
        self.listM.select_set(0)
        self.listM.pack()
        self.button2_1.pack(anchor=W)
        self.button2_2.pack(anchor=W)
        #self.button3.pack()
        Frame(self.Frame2, borderwidth=0, relief=GROOVE,heigh=40).pack(side=TOP,padx=0, pady=0,fill=BOTH)
       
    def add_image(self):
        self.path=askopenfilename(title="Open an image",filetypes=[('bmp files','.bmp'),('png files','.png'),('all files','.*')])
        #photo = PhotoImage(file=self.path)
        try:
            self.canvas.destroy()
        except:
            pass
        img = misc.imread(self.path)
        m = int(ceil(max(img.shape[0]/540,img.shape[1]/540)))
        img = misc.imresize(img,(ceil(img.shape[0]/m),ceil(img.shape[1]/m)))
        img = Image.fromarray(img.astype('uint8'), 'RGB')
        img = ImageTk.PhotoImage(img)
        #img = img.resize(img.height()/m,img.weidht()/m)
        #photo = PhotoImage(image=img)
        self.canvas = Canvas(self.Frame3,width=540, height=540)
        self.canvas.create_image(0, 0, anchor=NW, image=img)
        

        
        #m = int(ceil(max(photo.height()/540,photo.width()/540)))
        #photo = photo.subsample(m)
        #self.canvas.create_image(0, 0, anchor=NW, image=photo)
        self.canvas.pack()
        self.Frame3.mainloop()
    def quit(self):
        global b
        self.destroy()
        self.master.destroy()

try :
    b=0
    root = Tk()    
    root['bg']='white'
    root.geometry("800x600")
    app = Window(root)
    root.mainloop()
    
except :
    messagebox.showwarning("ERROR","A fatal Error occurred. Please Restart the client !")
      
