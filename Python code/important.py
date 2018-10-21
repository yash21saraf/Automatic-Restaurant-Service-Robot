from tkinter import *
import struct
import speech_recognition as sr
import time
import pyaudio
import time
import calendar as cd
import tkinter as tk
from gtts import gTTS
import os
import sys
import pygame
import XBee




def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None





#Just an example how the dictionary may look like
myDict = {'Rs 45': ['rice '], 'Rs 250': ['chicken fried rice'],
      'Rs 20': ['soup '], 'Rs 120': ['noodles'],
      'Rs 30': ['curd '], 'Rs 320': ['soup3'],
      'Rs 40': ['idli'], 'Rs 200': ['soup5'],
      'Rs 25': ['dosa'], 'Rs 202': ['soup7'],
      'Rs 10': ['milk '], 'Rs 204': ['soup22'],
      'Rs 20': ['soup11'], 'Rs 206': ['soup77']}






 # Record Audio
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)
        global m
        m=r.recognize_google(audio)
        #time.sleep(2)
        #m="rice"
        print("You said: " + m)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #Checking if string 'Mary' exists in dictionary value
    #print (search(myDict,str(m))) #prints firstName
    b=search(myDict,str(m))
    if (b==None):
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/m sarap/Desktop/now/final/qq.mp3")
        pygame.mixer.music.play()
        print('invalid')
        sys.exit()
    tts = gTTS(text=m, lang='en')
    tts.save(str(m)+".mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/m sarap/Desktop/now/final/q.mp3")
    pygame.mixer.music.play()
    time.sleep(1)
    tts = gTTS(text=m, lang='en')
    tts.save(str(m)+".mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/m sarap/Desktop/now/final/"+str(m)+".mp3")
    pygame.mixer.music.play()
    e=int(''.join(list(filter(str.isdigit, b))))
    print(e)
    y=m+"  "+str(b)
    #display()
    return y,e,m



def clear(k):
    return lambda : callback(k)
def callback(k):
    if (k==1):
        e11.delete(0,END)
        e12.delete(0,END)
        e13.delete(0,END)
        e14.delete(0,END)
        e12.insert(10,'0')
    elif (k==2):
        e21.delete(0,END)
        e22.delete(0,END)
        e23.delete(0,END)
        e24.delete(0,END)
        e22.insert(10,'0')
    elif (k==3):
        e31.delete(0,END)
        e32.delete(0,END)
        e33.delete(0,END)
        e34.delete(0,END)
        e32.insert(10,'0')
    elif (k==4):
        e41.delete(0,END)
        e42.delete(0,END)
        e43.delete(0,END)
        e44.delete(0,END)
        e42.insert(10,'0')
    elif (k==5):
        e51.delete(0,END)
        e52.delete(0,END)
        e53.delete(0,END)
        e54.delete(0,END)
        e52.insert(10,'0')
    elif (k==6):
        e61.delete(0,END)
        e62.delete(0,END)
        e63.delete(0,END)
        e64.delete(0,END)
        e62.insert(10,'0')
    elif (k==7):
        e71.delete(0,END)
        e72.delete(0,END)
        e73.delete(0,END)
        e74.delete(0,END)
        e72.insert(10,'0')
    elif (k==8):
        e81.delete(0,END)
        e82.delete(0,END)
        e83.delete(0,END)
        e84.delete(0,END)
        e82.insert(10,'0')
    elif (k==9):
        e91.delete(0,END)
        e92.delete(0,END)
        e93.delete(0,END)
        e94.delete(0,END)
        e92.insert(10,'0')
    elif (k==10):
        e101.delete(0,END)
        e102.delete(0,END)
        e103.delete(0,END)
        e104.delete(0,END)
        e102.insert(10,'0')



def xbee1(event=None): #set event to None to take the key argument from .bind
    print('Function successfully called!') #this will output in the shell
    if __name__ == "__main__":
               xbee = XBee.XBee("COM8")  # Your serial port name here
               # A simple string message
               sent = xbee.SendStr("+")
               time.sleep(0.25)
               Msg = xbee.Receive()
               if Msg:
                      content = Msg[7:-1].decode('ascii')
                      print("Msg: " + content)  

def xbee2(event=None): #set event to None to take the key argument from .bind
    print('Function successfully called!') #this will output in the shell
    if __name__ == "__main__":
               xbee = XBee.XBee("COM8")  # Your serial port name here
               # A simple string message
               sent = xbee.SendStr("-")
               time.sleep(0.25)
               Msg = xbee.Receive()
               if Msg:
                      content = Msg[7:-1].decode('ascii')
                      print("Msg: " + content)
                      
def display(event=None): #set event to None to take the key argument from .bind
    print('Function successfully called!') #this will output in the shell
    if __name__ == "__main__":
               xbee = XBee.XBee("COM8")  # Your serial port name here
               # A simple string message
               sent = xbee.SendStr(y)
               time.sleep(0.25)
               Msg = xbee.Receive()
               if Msg:
                      content = Msg[7:-1].decode('ascii')
                      print("Msg: " + content)                        
def show_entry_fields(k):
    return lambda : callback1(k)
def callback1(k):
    global j
    j=k
    print('Function successfully called!') #this will output in the shell
    global T
    T="TABLE"+str(j)
    global y
    global a
    global e
    global m
    global i
    y,e,m=speech()
    localtime = time.asctime( time.localtime(time.time()) )
    i=T+"  "+y
    a=str(localtime)
    #print(a)
    m=str(m)+"    "
    #m="m     "
    #e="20"
    if (k==1):
        j=e12.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e12.delete(0,END)
        e13.delete(0,END)
        e14.delete(0,END)
        e11.insert(100,m)
        e12.insert(10,"RS "+str(e))
        e13.insert(10,a)
        e14.insert(10,'occupied')
    elif (k==2):
        j=e22.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e22.delete(0,END)
        e23.delete(0,END)
        e24.delete(0,END)
        e21.insert(100,m)
        e22.insert(10,"RS "+str(e))
        e23.insert(10,a)
        e24.insert(10,'occupied')
    elif (k==3):
        j=e32.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e32.delete(0,END)
        e33.delete(0,END)
        e34.delete(0,END)
        e31.insert(100,m)
        e32.insert(10,"RS "+str(e))
        e33.insert(10,a)
        e34.insert(10,'occupied')
    elif (k==4):
        j=e42.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e42.delete(0,END)
        e43.delete(0,END)
        e44.delete(0,END)
        e41.insert(100,m)
        e42.insert(10,"RS "+str(e))
        e43.insert(10,a)
        e44.insert(10,'occupied')
    elif (k==5):
        j=e52.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e52.delete(0,END)
        e53.delete(0,END)
        e54.delete(0,END)
        e51.insert(100,m)
        e52.insert(10,"RS "+str(e))
        e53.insert(10,a)
        e54.insert(10,'occupied')
    elif (k==6):
        j=e62.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e62.delete(0,END)
        e63.delete(0,END)
        e64.delete(0,END)
        e61.insert(100,m)
        e62.insert(10,"RS "+str(e))
        e63.insert(10,a)
        e64.insert(10,'occupied')
    elif (k==7):
        j=e72.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e72.delete(0,END)
        e73.delete(0,END)
        e74.delete(0,END)
        e71.insert(100,m)
        e72.insert(10,"RS "+str(e))
        e73.insert(10,a)
        e74.insert(10,'occupied')
    elif (k==8):
        j=e82.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e82.delete(0,END)
        e83.delete(0,END)
        e84.delete(0,END)
        e81.insert(100,m)
        e82.insert(10,"RS "+str(e))
        e83.insert(10,a)
        e84.insert(10,'occupied')
    elif (k==9):
        j=e92.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e92.delete(0,END)
        e93.delete(0,END)
        e94.delete(0,END)
        e91.insert(100,m)
        e92.insert(10,"RS "+str(e))
        e93.insert(10,a)
        e94.insert(10,'occupied')
    elif (k==10):
        j=e102.get()
        j=int(''.join(list(filter(str.isdigit, j))))
        e=j+int(e)
        e102.delete(0,END)
        e103.delete(0,END)
        e104.delete(0,END)
        e101.insert(100,m)
        e102.insert(10,"RS "+str(e))
        e103.insert(10,a)
        e104.insert(10,'occupied')


        
master = Tk()
for k in range(1,11):
    tv = 'TABLE {}'.format(k)
    Label(master, text=tv).grid(row=k,column=1)
    Label(master, text=tv).grid(row=k,column=2)
    Label(master, text=tv).grid(row=k,column=3)
    Label(master, text=tv).grid(row=k,column=4)
    
all_entries = []

Label(master, text='ORDER').grid(row=0,column=2)
Label(master, text='AMOUNT').grid(row=0,column=3)
Label(master, text='TIME').grid(row=0,column=4)
Label(master, text='STATUS').grid(row=0,column=5)



e11 = Entry(bg='yellow',width=105)
e21 = Entry(bg='yellow',width=105)
e31 = Entry(bg='yellow',width=105)
e41 = Entry(bg='yellow',width=105)
e51 = Entry(bg='yellow',width=105)
e61 = Entry(bg='yellow',width=105)
e71 = Entry(bg='yellow',width=105)
e81 = Entry(bg='yellow',width=105)
e91 = Entry(bg='yellow',width=105)
e101 = Entry(bg='yellow',width=105)

e12 = Entry(master,width=30)
e22 = Entry(master,width=30)
e32 = Entry(master,width=30)
e42 = Entry(master,width=30)
e52 = Entry(master,width=30)
e62 = Entry(master,width=30)
e72 = Entry(master,width=30)
e82 = Entry(master,width=30)
e92 = Entry(master,width=30)
e102 = Entry(master,width=30)

e13 = Entry(bg='yellow',width=30)
e23 = Entry(bg='yellow',width=30)
e33 = Entry(bg='yellow',width=30)
e43 = Entry(bg='yellow',width=30)
e53 = Entry(bg='yellow',width=30)
e63 = Entry(bg='yellow',width=30)
e73 = Entry(bg='yellow',width=30)
e83 = Entry(bg='yellow',width=30)
e93 = Entry(bg='yellow',width=30)
e103 = Entry(bg='yellow',width=30)

e14 = Entry(master,width=30)
e24 = Entry(master,width=30)
e34 = Entry(master,width=30)
e44 = Entry(master,width=30)
e54 = Entry(master,width=30)
e64 = Entry(master,width=30)
e74 = Entry(master,width=30)
e84 = Entry(master,width=30)
e94 = Entry(master,width=30)
e104 = Entry(master,width=30)

e11.grid(row=1, column=2)
e21.grid(row=2, column=2)
e31.grid(row=3, column=2)
e41.grid(row=4, column=2)
e51.grid(row=5, column=2)
e61.grid(row=6, column=2)
e71.grid(row=7, column=2)
e81.grid(row=8, column=2)
e91.grid(row=9, column=2)
e101.grid(row=10, column=2)

e12.insert(10,'0')
e22.insert(10,'0')
e32.insert(10,'0')
e42.insert(10,'0')
e52.insert(10,'0')
e62.insert(10,'0')
e72.insert(10,'0')
e82.insert(10,'0')
e92.insert(10,'0')
e102.insert(10,'0')

e12.grid(row=1, column=3)
e22.grid(row=2, column=3)
e32.grid(row=3, column=3)
e42.grid(row=4, column=3)
e52.grid(row=5, column=3)
e62.grid(row=6, column=3)
e72.grid(row=7, column=3)
e82.grid(row=8, column=3)
e92.grid(row=9, column=3)
e102.grid(row=10, column=3)

e13.grid(row=1, column=4)
e23.grid(row=2, column=4)
e33.grid(row=3, column=4)
e43.grid(row=4, column=4)
e53.grid(row=5, column=4)
e63.grid(row=6, column=4)
e73.grid(row=7, column=4)
e83.grid(row=8, column=4)
e93.grid(row=9, column=4)
e103.grid(row=10, column=4)

e14.grid(row=1, column=5)
e24.grid(row=2, column=5)
e34.grid(row=3, column=5)
e44.grid(row=4, column=5)
e54.grid(row=5, column=5)
e64.grid(row=6, column=5)
e74.grid(row=7, column=5)
e84.grid(row=8, column=5)
e94.grid(row=9, column=5)
e104.grid(row=10, column=5)


Button(bg='red', text='DISPLAY', command=display).grid(row=11, column=0, sticky=W, pady=4)
Button(bg='red', text='Quit', command=master.destroy).grid(row=11, column=5, sticky=W, pady=4)
Button(bg='orange', text='Send', command=xbee1).grid(row=11, column=2, sticky=W, pady=4)
Button(bg='orange', text='Call', command=xbee2).grid(row=11, column=3, sticky=W, pady=4)


for k in range(1,11):
    tv = 'TABLE {}'.format(k)
    Button(bg='green', text=tv, command=show_entry_fields(k)).grid(row=k, column=0, sticky=W, pady=4)

for k in range(1,11):
    Button(bg='orange', text="CLEAR", command=clear(k)).grid(row=k, column=6, sticky=W, pady=4)


mainloop( )
