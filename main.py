from tkinter import *
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests 
import bs4
import threading
import os
#threading
def threading1(): 
    t1= threading.Thread (target = run_tom) 
    t1.start()
listener = sr.Recognizer()
engine = pyttsx3.init()
#exit function
def stop():
    os._exit(0)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    global dis
    global label
    print('welcome')
    engine.say('Hey I am tom, You can ask me anything. But if you want to quit say  STOP  ')
    engine.say('What i can do for you')
    engine.runAndWait()
    try:
        with sr.Microphone(device_index=0) as source:
            label = Label(dis, text = " Listening..........").place(x = 40, y = 60)
            voice = listener.listen(source,timeout=1, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command=command.lower()
            label = Label(dis, text = "                            ").place(x = 40, y = 60)
    except:
        print("Say that again please...")  
        return "None"
    return command
def run_tom():
    command = take_command()
    print("I got It")
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('Current time is'+ time)
        print(time)
    elif 'who is' in command:
        preson=command.replace('who is','')
        info = wikipedia.summary(preson,2)
        print(info)
        talk(info)
        pywhatkit.search(preson)
        talk('opening browser')
        text= preson
        url = 'https://google.com/search?q=' + text
        request_result=requests.get( url )
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text, 'lxml') 
        des = soup.get_text()
        talk(des[230:700])
    elif 'what is' in command:
        product=command.replace('what is','')
        info = wikipedia.summary(product,2)
        print(info)
        talk(info)
        pywhatkit.search(product)
        talk('opening browser')
        text= product
        url = 'https://google.com/search?q=' + text
        request_result=requests.get( url )
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text, 'lxml') 
        des = soup.get_text()
        talk(des[230:700])
    elif 'what are' in command:
        product=command.replace('what are','')
        info = wikipedia.summary(product,2)
        print(info)
        talk(info)
        pywhatkit.search(product)
        talk('opening browser')
        text= product
        url = 'https://google.com/search?q=' + text
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text, 'lxml') 
        des = soup.get_text()
        talk(des[230:500])
    elif 'who are you' in command:
        talk('I am TOM version 1.2    made by suibhsai with python')
        talk('I am sad that you dont know any thing about me')
        talk('but i know who are you.')
    elif 'who i am' in command:
        talk('haha,    Homo sapiens LOL')
    elif 'who am i' in command:
        talk('haha,    Homo sapiens LOL')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print('ha ha')
    elif 'stop' in command:
        exit()
    else:
        user_name = Label(dis, text = "Please try again").place(x = 40, y = 60)
        talk('sorry, i could not understand')
        talk('please try again')
        label = Label(dis, text = "                                      ").place(x = 40, y = 60)
dis = Tk()
dis.title("TOM_Version_1.1")
label = Label(dis, text ="Hey I am Your Assistance!" , font = ('Helvetica',20)).pack()
dis.geometry("550x600")
dis.maxsize(550,600)
bg = PhotoImage(file = "tom.png")
log = PhotoImage(file = "logo.png")
con = PhotoImage(file = "con2.png")
cont = PhotoImage(file = "con3.png")
photoimage = con.subsample(10, 10)
photoimage2 = cont.subsample(10, 10)
can1 = Canvas( dis, width = 550, height= 600)
can1.pack(fill = "both", expand = True)
can1.create_image( 0, 0, image = bg,anchor = "nw")
can1.create_image( 180, 10, image = log,anchor = "nw")
button1 = Button( dis, text = "ASK ME ", font = ('Verdana', 15),image = photoimage, bg = 'grey' ,compound = LEFT, command = threading1)
button1_canvas = can1.create_window( 230, 400,  anchor = "nw", window = button1)
button2 = Button( dis, text = "Quit!", font = ('Verdana', 15),image = photoimage2, bg = 'grey' ,compound = LEFT, command = stop)
button2_canvas = can1.create_window( 247, 470,  anchor = "nw", window = button2)
dis.mainloop()#make gui interactive 