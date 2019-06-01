from scipy import misc

from tkinter import messagebox
from tkinter.filedialog import *

#insert the binary message in the ind_bit of each pixels in the color plan
def convert (f,msg,color,ind_bit):
    
    ind=0
    
    for i in range (f.shape[0]):
        for  j in range (f.shape[1]):
            #get the binary representation of the [i][j][color] pixel
            Nb_b2=bin(256+f[i][j][color])[3:]
            if ind>= len(msg):
                return
            else :
                #insert the ind caractere of the binary msg in the ind_bit of [i][j][color] pixel's binary representation 
                Nb_b2_with_LSB=Nb_b2[:ind_bit]
                Nb_b2_with_LSB+=msg[ind]
                Nb_b2_with_LSB+=Nb_b2[ind_bit+1:]
                ind=ind+1
                f[i][j][color]=int(Nb_b2_with_LSB,2)





def  SteganographyHideMethod2 (msg,path,a=0,b=1,c=2):
    #read image
    f=misc.imread(path)
    x,y=f.shape[0],f.shape[1]
    #number of pixels in the image
    nb_of_pixels=(x*y)
    msg_b2=''
    #convert message to a binary message
    for i in msg :
        # the binary representation of the ASCII CODE of each caractere in th message 
        msg_b2+=bin(256+ord(i))[3:]
    # add \0 to the end of the message to discribe the end of the message
    msg_b2+='00000000'
    if len(msg_b2)>9*nb_of_pixels:
        messagebox.showwarning('Message too long  ', "Message length must be less then "+str(9*nb_of_pixels//8))
        return
    left_range=0
    right_range=nb_of_pixels
    ind=0
    #donnating plan priority eg : Red - green - blue
    color_priority=[a,b,c]
    ind_bit=0
    while (msg_b2[left_range:right_range]!=''):
        #hide the information starting from left range to right range in the color_priority[ind]  plan  and in the 7-(ind_bit//3) bit of each pixels
        convert(f,msg_b2[left_range:right_range],color_priority[ind],7-(ind_bit//3))
        ind_bit+=1
        ind+=1
        ind%=3
        left_range+=nb_of_pixels
        right_range+=nb_of_pixels
    # save image
    path=asksaveasfilename(defaultextension=".png",filetypes=[('png files','.png')])
    misc.imsave(path,f)
    return 

def SteganographyRetriveMethod2 (path ,a=0,b=1,c=2):
    l=''        
    msg=''
    color_priority=[a,b,c]
    #read image 
    f=misc.imread(path)
     
    for k in range(7,-1,-1):
        for o in color_priority :
            for i in range (f.shape[0]):
                for j in range (f.shape[1]):
                    #get the binary representation onf the i,j pixels of the o plan the get the k pixel
                    l+=(bin(256+f[i][j][o])[3:])[k]
                    if len (l)==8 :
                        # l describes a caractere
                        car=''
                        for d in range (len(l)):
                            car+=l[d]
                        #car : is the binary representation on the caracter 
                        if (int(car,2))==0 :
                            #the end of the crypted  message \0
                            return  msg;
                        #get the caracter 
                        msg+=(chr(int(car,2)))
                        l=''
                        
