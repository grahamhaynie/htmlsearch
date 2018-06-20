#! python3
"""
htmlsearch.py -
Create a gui that using tkinter, allowing the user to select an html element from a list of buttons, 
and input a url of the website to search. Upon clicking the search button, display the results.

Created by Graham Haynie
"""

from tkinter import *
import urllib.request
import re

# TODO - add custom search
# TODO - add search for embedded items
# TODO - what about elements with more than just <p> ?
#      - improve regular expression to get more desirable results??

#TODO - fix left/right buttons 
#TODO - make gui prettier
#TODO - add instructions - make readme.md

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master

        self.searchLabel = Label(self, text="URL:")
        self.v = StringVar() #Tk variable to track changes to radio button
        self.searchText = Text(self)
        self.searchButton = Button(self, text="Search",command=self.search)
        self.resultMessage = Message(self, text="Results will appear here", bg='white', anchor=NW)

        self.leftButton = Button(self, text="<", command=self.leftClicked)
        self.rightButton = Button(self, text=">", command=self.rightClicked)

        self.init_window(
            self.searchLabel, self.searchText, self.searchButton, self.resultMessage, 
            self.leftButton, self.rightButton, self.v
        )

        self.results = []
        self.currentIndex = 0
        self.validResults = False

    def init_window(
        self, searchLabel, searchText, searchButton, resultMessage,
        leftButton, rightButton, v):
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        #create dictionary of options for elements
        OPTIONS = [
            ("<p>","p"), 
            ("<i>","i"),
            ("<u>","u"),
            ("<h1>","h1"),
            ("<div>","div"),
            ("<title>", "title")
        ]

        v.set("p")

        #loop to create radio buttons
        for text, mode in OPTIONS:
            b = Radiobutton(self, text=text, variable=v, value=mode, indicatoron=False, height=1, width=6)
            b.pack(anchor=W)

        #place widgets
        self.searchLabel.place(x=55, y=0)
        self.searchText.place(x=55, y=20, height=50, width=725)
        self.searchButton.place(x=385, y=75)
        self.resultMessage.place(x=85, y=110, height=300, width=665)
        self.leftButton.place(x= 55, y= 225, height=25, width=25)
        self.rightButton.place(x= 755, y= 225, height=25, width=25)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu,tearoff=False)

        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

    def client_exit(self):
        exit()

    def search(self):
        try: #attempt to load and parse given url, if not display error message in text box

            #1.0 = read from line one, characters zero
            #end-lc = read until end, -1c gets rid of trailing newline
            url = self.searchText.get("1.0", 'end-1c')

            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            respData = resp.read()

            regDict = { 
                "p":r'<p>(.*?)</p>',
                "i":r'<i>(.*?)</i>',
                "u":r'<u>(.*?)</u>',
                "h1":r'<h1>(.*?)</h1>',
                "div":r'<div>(.*?)</div>',
                "title":r'<title>(.*?)</title>'
            }

            curReg = regDict[self.v.get()]

            #print(curReg)

            self.results = re.findall(curReg,str(respData))

            if(len(self.results) > 0):
                self.resultMessage.configure(text=self.results[0])
                self.validResults = True
            else:
                self.resultMessage.configure(text="No results found")
                self.validResults = False


            #for eachP in paragraphs:
               # print(eachP)
            
        except Exception as e:
            self.resultMessage.configure(text="Invalid URL")
            #print(str(e))

    def leftClicked(self):
        if(self.validResults):
            if(self.currentIndex - 1 >= 0):
                self.leftButton.config(state=ACTIVE)
                self.currentIndex = self.currentIndex - 1
                self.resultMessage.configure(text=self.results[self.currentIndex])
            else:
                self.leftButton.config(state=DISABLED)
        print(self.currentIndex)

    def rightClicked(self):
        if(self.validResults):
            if(self.currentIndex + 1 < len(self.results)):
                self.rightButton.config(state=ACTIVE)
                self.currentIndex = self.currentIndex + 1
                self.resultMessage.configure(text=self.results[self.currentIndex])
            else:
                self.rightButton.config(state=DISABLED)
        print(self.currentIndex)
        
#Tkinter stuff to display window
root = Tk()
root.geometry("800x500")
app = Window(root)
root.mainloop()