from scipy import misc
import numpy as np
from tkinter import *
from tkinter.filedialog import *

i=int()
def SteganographyHideMethod1(msg,path,x=2,y=3,z=3):
   try :
      msg+=chr(0) # to marke the end of a message 
      #image is a 3 deminsion matrix RGB
      
      image = misc.imread(path)
      i = 0;
      height = image.shape[1]
      width = image.shape[0]
      pixelsNumber = height * width
      while (i<pixelsNumber and i <len(msg)):
         try:
            binaryRep = '{0:08b}'.format(ord(msg[i])) #binary representation with 8 bits
            BinRed = '{0:08b}'.format(image[i%width][i//width][0])
            BinGreen = '{0:08b}'.format(image[i%width][i//width][1])
            BinBlue = '{0:08b}'.format(image[i%width][i//width][2])
         except :
            print(i)
            print(width)
            print (i%width)
            print(i//width)
        #inserting information

        #slicing the x most segnificant bits of the msg in the x less segnificant bits of the Red
         BinRed=BinRed[:8-x]+binaryRep[:x]
         image[i%width][i//width][0] = int(BinRed,2)#converting to decimal base and inserting new value
        
        #slicing the y next bits of the msg in the y less segnificant bits of the Green
         BinGreen=BinGreen[:8-y]+binaryRep[x:y+x]
         image[i%width][i//width][1] = int(BinGreen,2)#converting to decimal base and inserting new value
        
        #slicing the z less segnificant bits of the msg in the z less segnificant bits of the Blue
         BinBlue=BinBlue[:8-z]+binaryRep[x+y:]
         image[i%width][i//width][2] = int(BinBlue,2)#converting to decimal base and inserting new value
         
         i+=1;
        
      path=asksaveasfilename(defaultextension=".png",filetypes=[('png files','.png')])
      if path =="":
         index = path[::-1].find('.')+1
         path = path[:-index]+'(1)'+path[-index:]
      misc.imsave(path,image)
      return ;
   except:
      messagebox.showwarning("ERROR","Please choose the method carefully !")
def SteganographyRetriveMethod1(path ,x=3,y=2,z=3):
   try:
      msg = ""
      image = misc.imread(path)
      width = image.shape[0]
      height = image.shape[1]
      pixelsNumber = width * height
      i=0;        
      while (i<pixelsNumber):
         #Getting the x most segnificant bits from Red less segnificant bits
         BinRed = '{0:08b}'.format(image[i%width][i//width][0])
         #Getting the y middle bits from Green less segnificant bits
         BinGreen = '{0:08b}'.format(image[i%width][i//width][1])
         #Getting the z less segnificant bits from Blue less segnificant bits
         BinBlue = '{0:08b}'.format(image[i%width][i//width][2])
         #concatinating xyz bits 
         binaryRep = BinRed[-x:]+BinGreen[-y:]+BinBlue[-z:]
         c=int(binaryRep,2)
         #print (c," ", chr(c))
         if (c == 0):return msg;
         msg += chr(c);
         i+=1;
         if i == pixelsNumber : return msg
   except:
      messagebox.showwarning("ERROR","Please choose the method carefully !")
