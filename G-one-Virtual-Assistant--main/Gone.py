from ast import Str
import atexit
import operator
import profile
from sqlite3 import Time
import sys
from winsound import PlaySound
import instaloader
from numpy import str_
import pyttsx3
import subprocess
from tkinter.ttk import Progressbar
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import ctypes
import time
import requests
import shutil
import requests
from bs4 import BeautifulSoup
import  pyjokes
from click import command
import os.path
from requests import get
import requests
import time
import pyjokes
import requests
import smtplib
import cv2
import random
import pyautogui
import instadownloader
import instaloader
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from GoneUi import Ui_GoneUi
from pywikihow import search_wikihow
from pywikihow import WikiHow
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("G1")
	speak("I am your Assistant")
	speak(assname)

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('enter yourgmail.com', 'your pass')
    server.sendmail('your email id', to, content)
    server.close()

def news():
	main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bc6b5f7a1bb949e5af655d4df8ef0d84"
	main_page = requests.get(main_url).json()
	articles = main_page["articles"]
	head = []
	day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
	for ar in articles:
		head.append(ar["title"])
	for i in range(len(day)):
		speak(f"today's {(day[i])} news is:{head[i]}")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution() 

    def takeCommand(self):
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
        return self.query.lower()

    def TaskExecution(self):
        wishMe()
        while True:
            self.query= self.takeCommand().lower ()

            if "open notepad" in self.query:
                npath ="C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                os. system("start cmd")

            elif "open camera" in self.query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret, img=cap.read()
                    cv2.imshow('webcam', img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break;
                    cap.release()
                    cv2.destroyALLWindows()

            elif "play music" in self.query:
                music_dir="music"
                songs=os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
            

            elif "ip address" in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak ("searching wikipedia....")
                self.query=self.query .replace("wikipedia","")
                results = wikipedia.summary (self.query, sentences=2) 
                speak ("according to wikipedia")
                speak (results)
                print(results)

            elif "youtube search" in self.query:
                speak("OK sIR , This Is What I found For Your Search!")
                self.query = self.query.replace("G-1","")
                self.query = self.query.replace("youtube search","")
                self.query = self.query.replace("search youtube","")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                speak("Done sir!")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm =self.takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif "email to vraj" in self.query:
                try:
                    speak("what should i say?")
                    content=self.takeCommand().lower()
                    to="recevier emaail.com.com"
                    sendEmail(to,content)
                    speak("Email has been sent to avi")

                except Exception as e:
                    print(e)
                    speak ("sorry sir,iam not able to sent this email to vraj")

            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os. system("taskkill /f /im notepad.exe")

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "news" in self.query:
                speak("wait sir")
                news()
        
            elif "temperature" in self.query:
                self.query = self.query.replace("temperature","")
                self.query = self.query.replace("what temperature ","")
                self.query = self.query.replace("what's temperature ","")
                self.query = self.query.replace("G-1","")
                search = "temperature in"+self.query
                url = f"https://www.google.com/search?q={search}"
                r  = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div", class_= "BNeawe").text
                speak(f"current{search} is {temp}")


            elif "where i am" in self.query or "where we are" in self.query:
                speak ("wait sir, let me check")
                try:
                    ipAdd=requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url='https:///get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url) 
                    geo_data=geo_requests.json()
                    city = geo_data['city']
                    country=geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak ("sorry sir, Due to network issueiam not able to find where we are.")
                    pass
                
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name=input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}") 
                speak (f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition=self.takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak ("i am done sir, profile picture is saved in our main folder. nowiam ready")
                else:
                    pass

            elif "take screenshot" in self.query or "take a screenshort" in self.query:
                speak ("sir, please tell me the name for this screenshot file")
                name=self.takeCommand().lower()
                speak ("please sir hold the screen for few seconds,iam taking screenshot")
                time.sleep(3)
                img=pyautogui.screenshot ()
                img.save(f"{name}.png")
                speak ("i am done sir, the screenshot is saved in our main folder")
            
            elif "Good Morning" in self.query:
                speak("A warm" +self.query)
                speak("How are you Mister")
                speak("G-One")

            elif "who i am" in self.query:
                speak("If you talk then definitely your human.")

            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
            
            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")
            
            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(self.takecommand())
                time.sleep(a)
                print(a)

            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWor

startExecution = MainThread()
            
class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_GoneUi() 
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/Vraj Patel/Desktop/gone/Siri.gif") 
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("C:/Users/Vraj Patel/Desktop/gone/Initiate.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString('hh:mm:ss')
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText (label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
Gone = Main()
Gone.show()
atexit(app.exec_())
