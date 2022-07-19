#-----------------------------Import-----------------------------
import speech_recognition as sr
import pyttsx3
import torch
import numpy as np
import cv2
import pywhatkit
import wikipedia
import webbrowser
import os
import time
import datetime
from time import ctime
import collections
#   Import RO dependencies
import folium
import webbrowser

import sys
import csv

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import bokeh
from bokeh.io import show, output_notebook
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, StaticLayoutProvider
from bokeh.models.graphs import from_networkx

#-------------------Voice engine configuration------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#---------------------------Functions---------------------------
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    # assname = ("Yolo")
    speak("I am your Assistant, yolo")
    # speak(assname)

def username():
    # speak("What should i call you ")
    # uname = takeCommand()
    # speak("Welcome "+uname)
    speak("How can i Help you?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('')
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        print('')
        command = r.recognize_google(audio, language='en-in')
        print(command)

    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice.")
        return "None"

    return command

def RO():

    # Import data.xlsx
    GeoLoc = pd.read_excel("C:/Users/Mohamed Amine/Desktop/Geo Loc.xlsx")
    LatLong = GeoLoc[["Gov","Latitude","Longitude"]]
 
    # Networkx Prep
    G = nx.Graph()
    G.add_weighted_edges_from([('bizert','ariana',64), ('bizert', 'baja',104), ('bizert', 'la manouba',77),
                            ('baja', 'jendouba',51), ('baja', 'la manouba',105), ('baja', 'zaghouan',117),
                            ('baja', 'siliana',102), ('jendouba', 'le kef',57), ('jendouba', 'siliana',103),
                            ('ariana', 'tunis',13), ('ariana', 'la manouba',14), ('ben arous', 'zaghouan',50),
                            ('ben arous', 'nabeul',61), ('ben arous', 'la manouba',21), ('ben arous', 'tunis',11),
                            ('nabeul', 'zaghouan',65), ('nabeul', 'sousse',109), ('tunis', 'la manouba',16),
                            ('zaghouan', 'sousse',102), ('zaghouan', 'siliana',92), ('zaghouan', 'kairouan',111),
                            ('siliana', 'le kef',72), ('siliana', 'kasserine',145), ('siliana', 'kairouan',101),
                            ('siliana', 'sidi bouzid',162), ('le kef', 'kasserine',130), ('sousse', 'kairouan',55),
                            ('sousse', 'mounastir',22), ('sousse', 'mahdia',63), ('kairouan', 'sidi bouzid',106),
                            ('kairouan', 'mahdia',113), ('kairouan', 'sfax',136), ('kasserine', 'gafsa',110),
                            ('kasserine', 'sidi bouzid',74), ('mounastir', 'mahdia',47), ('mahdia', 'sfax',117),
                            ('sfax', 'gabes',161), ('sfax', 'sidi bouzid',132), ('sidi bouzid', 'gafsa',103),
                            ('sidi bouzid', 'gabes',178), ('gafsa', 'tozeur',92), ('gafsa', 'kebili',111),
                            ('gafsa', 'gabes',155), ('tozeur', 'kebili',96), ('kebili', 'gabes',118),
                            ('kebili', 'tataouine',233), ('kebili', 'medenine',196), ('gabes', 'medenine',76), 
                            ('medenine', 'tataouine',54)])

    Gfs = nx.DiGraph()
    # Gfs.add_edges_from([("A","B"),("A","C"),("B","D"),("B","D"),("C","F"),("C","G"),("D","H"),("G","I")])
    Gfs.add_edges_from([("ben arous", "nabeul"), ("ben arous", "tunis"), ("ben arous", "la manouba"),
                        ("ben arous",  "zaghouan"),("ben arous", "sousse"), ("kairouan", "siliana"),
                        ("kairouan", "zaghouan"), ("kairouan", "sousse"), ("kairouan", "mahdia"),
                        ("kairouan", "sfax"), ("kairouan", "sidi bouzid"), ("sousse", "zaghouan"),
                        ("sousse", "nabeul"), ("sousse", "kairouan"), ("sousse", "mahdia"),
                        ("sousse", "mounastir"),  ("nabeul", "zaghouan"),  ("nabeul", "ben arous"),
                        ("nabeul", "sousse"), ("le kef", "jendouba"), ("le kef", "siliana"), 
                        ("le kef", "kasserine"), ("sidi bouzid", "kasserine"), ("sidi bouzid", "siliana"),
                        ("sidi bouzid", "kairouan"), ("sidi bouzid", "sfax"), ("sidi bouzid", "gabes"),
                        ("sidi bouzid", "gafsa"), ("kasserine", "le kef"), ("kasserine", "siliana"),
                        ("kasserine", "sidi bouzid"), ("kasserine", "gafsa"), ("mahdia", "mounastir"),
                        ("mahdia", "sousse"), ("mahdia", "kairouan"), ("mahdia", "sfax"),
                        ("sfax", "mahdia"), ("sfax", "kairouan"), ("sfax", "sidi bouzid"),
                        ("sfax", "gabes"), ("tunis", "ariana"), ("tunis", "la manouba"),
                        ("tunis", "ben arous"), ("zaghouan", "ben arous"), ("zaghouan", "la manouba"),
                        ("zaghouan", "baja"), ("zaghouan", "siliana"), ("zaghouan", "kairouan"),
                        ("zaghouan", "sousse"), ("zaghouan", "nabeul"), ("jendouba", "baja"),
                        ("jendouba", "siliana"), ("jendouba", "le kef"), ("siliana", "le kef"),
                        ("siliana", "jendouba"), ("siliana", "baja"), ("siliana", "zaghouan"), 
                        ("siliana", "kairouan"), ("siliana", "sidi bouzid"), ("siliana", "kasserine"),
                        ("bizert", "ariana"), ("bizert", "la manouba"), ("bizert", "baja"),
                        ("ariana", "bizert"), ("ariana", "la manouba"), ("ariana", "tunis"),
                        ("la manouba", "bizert"), ("la manouba", "ariana"), ("la manouba", "tunis"),
                        ("la manouba", "zaghouan"), ("la manouba", "baja"), ("baja", "bizert"),
                        ("baja", "jendouba"), ("baja", "la manouba"), ("baja", "zaghouan"),
                        ("baja", "siliana"), ("tozeur", "gafsa"), ("tozeur", "kebili"),
                        ("tataouine", "kebili"), ("tataouine", "medenine"), ("mounastir", "sousse"),
                        ("mounastir", "mahdia"), ("gabes", "sfax"), ("gabes", "sidi bouzid"),
                        ("gabes", "gafsa"), ("gabes", "kebili"), ("gabes", "medenine"),
                        ("gafsa", "kasserine"), ("gafsa", "sidi bouzid"), ("gafsa", "gabes"),
                        ("gafsa", "kebili"), ("gafsa", "tozeur"), ("kebili", "tozeur"),
                        ("kebili", "gafsa"), ("kebili", "gabes"), ("kebili", "medenine"),
                        ("kebili", "tataouine"), ("medenine", "tataouine"), ("medenine", "kebili"), ("medenine", "gabes")])

    # Folium map manipulation
    def DFS(visited, Gfs, dep):
        if dep not in visited:
            print(dep)
            visited.add(dep)
            for neighbour in Gfs[dep]:
                DFS(visited, Gfs, neighbour)
        
    
    def BFS(Gfs, dep):
        visit = set()
        queue = collections.deque([dep])

        while queue:
            vertex = queue.popleft()
            visit.add(vertex)
            for i in Gfs[vertex]:
                if i not in visit:
                    queue.append(i)
        print(visit)
    
    # Add Popups
    def pop():
        for i in range(len(LatLong)) :
            Tooltip = LatLong.loc[i, "Gov"]
            pop = "<i>"+LatLong.loc[i, "Gov"]+"\n"+"Lat:"+str(LatLong.loc[i, "Latitude"])+"\n"+"Long:"+str(LatLong.loc[i, "Longitude"])+"</i>"

            folium.Marker(
                [float(LatLong.loc[i, "Latitude"]) , float(LatLong.loc[i, "Longitude"])], 
                popup=pop,
                tooltip=Tooltip).add_to(m)

        # Draw paths
    def draw(dep, arr):
        Loc = []
        speak("for the algorithm, we have two, choose one if you want bellman or two if you want djikistra")
        algo = input("algo:")
        if (algo.lower()=="one" or algo.lower()=="1"):
            path = nx.bellman_ford_path(G,dep,arr)
        elif (algo.lower()=="bfs"):
            print("BFS")
            path = BFS(Gfs, dep)
        elif (algo.lower()=="dfs"):
            print("DFS")
            visited = set()
            path = DFS(visited, Gfs, dep)
        else:
            path = nx.dijkstra_path(G,dep,arr)

        if (algo.lower()=="bfs" or algo.lower()=="dfs"):
            return path
        else:
            for lo in path:
                for locco in range(len(LatLong)) :
                    if lo==LatLong.loc[locco, "Gov"].lower():
                        tupletto = (LatLong.loc[locco, "Latitude"], LatLong.loc[locco, "Longitude"])
                        Loc.append(tupletto)

            print(path)
            print(Loc)

            folium.PolyLine(Loc,
                            color='green',
                            weight=5,
                            opacity=0.8).add_to(m)
            m.save("map.html")
            return webbrowser.open("map.html")

    #------------RunAll Functions------------
    L = []
    for l in LatLong["Gov"]:
        L.append(l.lower())
    speak("choose your start location")
    depart = input("depart: ")
    dep = depart.lower()
    while (dep not in L):
        speak("This localisation is not recognized, please try again !")
        dep = input("depart: ").lower()
    speak("choose your goal location")
    arrive = input("arrive: ")
    arr = arrive.lower()
    while (arr not in L):
        speak("This localisation is not recognized, please try again !")
        arr = input("arrive: ").lower()

    m = folium.Map(location=[float(LatLong[LatLong["Gov"]==dep.lower()]["Latitude"]),
                            float(LatLong[LatLong["Gov"]==dep.lower()]["Longitude"])], zoom_start=8)

    pop()
    draw(dep, arr)

#-------------------------The Big Magic-------------------------
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        command = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'command' and will be
        # converted to lower case for easily
        # recognition of command
        if 'hi' in command or 'hello' in command:
            speak('hi there')

        elif ('who are you') in command:
            speak("I am your virtual assistant ask me whatever you want and I will try to help you")

        elif 'how are you' in command:
            speak('fine thanks, what about you ?')

        elif 'fine' in command or 'good' in command or 'ok' in command or 'okey' in command:
            speak('it is good to know that you are fine')

        elif ('tired' or 'stressed' or 'not good' or 'not fine' or 'broke') in command:
            speak('you should take care of yourself I wish I can sheer you up ')
            speak('Let me know if I can do anything for you')

        elif ('path' in command) or ('location' in command):
            speak("welcome to this special project, so to begin you should first choose you start location then your goal location")
            speak("for this case, you will type in your localisation by yourself because there are too many diffrent pronenciation of the tunisian governorate, so we are sorry for that")
            RO()

        elif ('why' and 'create') in command or ('why' and 'created') in command or ('why' and 'made') in command:
            speak("I was created to help people to do some tasks especially the blind ones.")

        # elif 'location' in command or 'map' in command or 'locate' in command:
            # speak('what should i locate for you ?')
            # location = takeCommand()
            # webbrowser.open("http://www.google.com/maps/place/" + location)
            # speak("here is what i found for " + location)

        elif 'where is' in command:
            location = command.replace('where is', '')
            webbrowser.open("http://www.google.com/maps/place/" + location)
            speak("here is what i found for " + location)

        elif 'your name' in command:
            speak('my name is yolo')

        elif 'what time is it' in command or 'what is the time' in command or 'time' in command:
            speak(ctime())

        elif 'made you' in command or 'build you' in command or 'create you' in command:
            speak('a group of students at E S B, and i am so glad to be made by them')

        elif 'play' in command:
            speak('what can i play for you?')
            command = takeCommand()
            speak('i am playing for you ' + command)
            pywhatkit.playonyt(command)

        elif ('search' and 'wikipedia') in command:
            speak("what exactly?")
            command = takeCommand()
            info = wikipedia.summary(command, 1)
            speak(info)

        elif ('google' and 'search') in command or 'search' in command:
            speak("what do you want to search for?")
            command = takeCommand()
            url = "http://google.com/search?q=" + command
            webbrowser.get().open(url)
            speak("here is what i found for " + command)

        elif ('powerpoint' or 'presentation') in command:
            power = r"C:/Users/Mohamed Amine/Desktop/PROJET IA (1).pptx"
            os.startfile(power)
            speak('i am opening the presentation')

        elif command == '':
            speak('i can not hear you !')

        elif 'what is' in command:
            searchkey=command.replace('what is', '')
            info = wikipedia.summary(command, 1)
            speak(info)

        elif "don't listen" in command or "stop listening" in command:
            speak("for how much time you want to stop YOLO from listening commands")
            a = int(takeCommand())
            time.sleep(a*60)
            print(a)
            speak('now i can take your commands')

        elif 'remind me' in command:
            speak('after how much time you want me to remind you?')
            a = int(takeCommand())
            time.sleep(a * 60)
            speak('time is up')

        elif 'exit' in command or 'goodbye' in command or 'bye' in command:
            speak('good bye then, have a good day')
            exit()