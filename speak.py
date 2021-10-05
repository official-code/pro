#!/usr/bin/python3
import pyautogui
from pytube import YouTube
from colorama import Fore, Back, Style
import os
import time
import pyttsx3
import datetime
speak = pyttsx3.init()
e = ['q','Q','EXIT','QUIT','quit','exit']
password = []
user = []
while True:
 os.system("clear")
 print(Fore.RED+"""
                  ____    _______
                 | ___|  |  _____|
                _| |_    | |_____
               |_   _| R |  _____| E  
                 | |     | |______  
                 |_|     |_______|
  """)
 time.sleep(0.7)
 o = input(Fore.GREEN+"""
         __________OFFICIAL-CODE_______
        |                              |
        |    [1] CREAT FREE            |
        |                              |
        |    [2] LOGIN                 |
        |______________________________|
         
>>>>>>>>>>>""");
 if o == "1" or o == "CREAT FREE" or o == "creat free":
     os.system("clear")
     p = input(Fore.YELLOW+"""
        ----------------------------------------------
        | GMAIL : """)
     j = input(Fore.YELLOW+"""        |_____________________________________________
        | PASSWORD : """)
     print("        |_____________________________________________")
     ji = "                       Thank YOU for create account FREE"
     po =f"""
                     ______________________contact__________________
       <<<<<<<<<<<<<|                                              |>>>>>>>>>>>>
                                GMAIL : {p}                   
                               PASSWORD : {j}               
       <<<<<<<<<<<<<|_______________________________________________|>>>>>>>>>>>
       """
     if p == "":
         print (" Gmail --false--\n")
         time.sleep(2)
     elif j == "":
         print (" password --false--\n")
         time.sleep(2)
     else: 
      print (Fore.GREEN+po)
      print (Fore.RED+ji)
      user.append(p)
      password.append(j)

      os.system("clear")
 elif o == "2" or o == "LOGIN" or o == "login":
     os.system("clear")
     s = input("""
        ----------------------------------------------
        | GMAIL : """)
     l = input("""        |_____________________________________________
        | PASSWORD : """)
     print("        |_____________________________________________")
     if s in user and l in password:
      os.system("clear")
      print(Fore.RED+"ROBOT: hi")
      lw = Fore.RED+"ROBOT: OK MY FRIEND"
      wl = Fore.RED+"ROBOT : OK SIR"
      while True:
       me = input(Fore.WHITE+"me: ")
       speak.say(me)
       if me == "open terminal": 
         print(lw)
         os.system("gnome-terminal")
         speak.say("ok my friend")
       elif me == "open firefox":
         print(lw)
         speak.say("ok my friend")
         os.system("firefox")
       elif me == "hi" or me == "hello":
         print(Fore.RED+"ROBOT: DO YOU HELP ?")
         speak.say("fo you help")
       elif me == "yes" or me == "y":
         print(Fore.WHITE + """ROBOT:
FACEBOOK 
INSTGRAM
YOUTUBE
CLOCK
HACKING
GOOGLE
terminal
my ip
send brupforce
create file
:""")
         speak.say("facebook instgram youtube clock hacking google terminal my i p address send burpforce create file")
       elif me == "MY IP" or me == "my ip":
        print(lw)
        os.system("ifconfig")
        speak.say("ok my friend")
       elif me == "facebook" or me == "FACEBOOK":
        print (wl)
        os.system("xdg-open https://www.facebook.com")
        speak.say("ok sir")
       elif me == "INSTAGRAM" or me == "instagram":
         print (Fore.RED+"ROBOT : OK OPEN IMSTAGRAM")
         os.system("xdg-open https://www.instagram.com")
         speak.say("ok sir")
       elif me == "YOUTUBE" or me == "youtube":
         print ("ROBOT : OK SIR")
         speak.say("ok sir")
         os.system("xdg-open https://www.youtube.com")
       elif me == "clock":
          print (wl)
          speak.say("ok sir")
          date = datetime.datetime.now()
          speak.say(date)
          print(date)
       elif me == "hacking":
          print (wl)
          speak.say("ok sir")
          os.system("xdg-open https://www.blackhat.com")
       elif me in e:
          speak.say("ok exit")
          print(Fore.RED+"ROBOT:EXIT NOw")
          exit()
       elif me == "create file": 
         print (Fore.RED+"ROBOT : OK CREAT FILE")
         speak.say("ok creat file thanl you ")
         speak.runAndWait()
         o = input("name file for creat:")
         f = open(o,"w")
         f.write("Editor : Official-coDe")
         f.close()
       elif me == "terminal": 
        while True:
         print (lw)
         speak.say("ok my friend")
         speak.runAndWait()
         i = input("command: ")
         speak.say(i)
         speak.runAndWait()
         os.system(i)
         if i == "back":
           break
           print(Fore.RED+"ROBOT : OK BACK")
           speak.say("back")
           speak.runAndWait()   
       elif me == "google":
        os.system("clear")
        print("GooGlE")
        while True:
         w = input(Fore.RED+"""
>>>>>>>>search:""")
         if  w == "back":
           break
           print("ROBOT : OK BACK")
           speak.say("back")   
           speak.runAndWait()
         else:
            os.system("xdg-open https://www.google.com/search?q="+w) 
       elif me == "send burpforce":
            print (Fore.RED+"ROBOT : Brup force attack")
            speak.say('brup force attack')
            speak.runAndWait()
            ui = int(input("time:"))
            iu = input("text:")
            while True:
             time.sleep(ui)
             pyautogui.typewrite(iu)
             pyautogui.press('enter')
       speak.runAndWait()
     else:
         print ("Gmail or password false\n")
         time.sleep(2)
 elif o in e:
       exit()
       os.system("clear")
 else :
       print ("what is  {}".format(o))
       time.sleep(1)
