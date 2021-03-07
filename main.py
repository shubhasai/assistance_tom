import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests 
import bs4
listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
print('welcome')
engine.say('Hey I am tom')
engine.say('What i can do for you')
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone(device_index=0) as source:
            print('Listening...')
            voice = listener.listen(source,timeout=1, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command=command.lower()
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
        info = wikipedia.summary(preson,3)
        print(info)
        talk(info)
        pywhatkit.search(preson)
        talk('opening browser')
        text= preson
        url = 'https://google.com/search?q=' + text
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text,"html.parser")
        heading_object=soup.find_all('h3')
        for info in heading_object: 
            talk(info.getText())
            print("------")
            break
    elif 'what is' in command:
        product=command.replace('what is','')
        info = wikipedia.summary(product,5)
        print(info)
        talk(info)
        pywhatkit.search(product)
        talk('opening browser')
        text= product
        url = 'https://google.com/search?q=' + text
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text,"html.parser")
        heading_object=soup.find_all('h3' )
        for info in heading_object: 
            talk(info.getText())
            print("------")
            break
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
        soup = bs4.BeautifulSoup(request_result.text,"html.parser")
        heading_object=soup.find_all('h3')
        for info in heading_object: 
            talk(info.getText())
            print("------")
            break
    elif 'find' in command:
        text=command.replace('','')
        url = 'https://google.com/search?q=' + text
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text,"html.parser")
        heading_object=soup.find_all('h3')
        for info in heading_object: 
            talk(info.getText())
            print("------")
            break
    elif 'who are you' in command:
        talk('I am made by S.M with python')
        talk('I am sad that you dont know any thing about me')
        talk('but i know who are you.')
    elif 'who i am' in command:
        talk('haha,    Homo sapiens LOL')
    elif 'who am i' in command:
        talk('haha,    Homo sapiens LOL')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    else:
        talk('sorry, i could not understand')
        talk('please try again')
while True:
    run_tom()