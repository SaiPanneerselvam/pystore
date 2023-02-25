import requests,webbrowser
from bs4 import BeautifulSoup
from tkinter import *
struct=Tk()
struct.geometry("430x350")
struct.title("Python Structure Websearch")
label=Label(struct,text="Python Websearch engine beta",bg="teal",fg="white",font=("Verdana",20))
label.pack(side=TOP)
struct.config(background="teal")
text=StringVar()
def search():
     data=requests.get('https://www.google.com/search?q='+text.get())
     soup=BeautifulSoup(data.content,"html.parser")
     result=soup.select(".kCrYT a")
     for link in result[:1]:
         searching=link.get("href")
         searching=searching[7:]
         searching=searching.split("&")
         webbrowser.open(searching[0])
label=Label(struct,text="Enter here to search",bg="teal",fg="white",font=("Arial",15))
label.place(x=50,y=100)
label=Label(struct,text="By SaiPanneerselvam",bg="teal",fg="white",font=("Arial",14))
label.place(x=50,y=130)
enter=Entry(struct,font=("Arial",10,"bold"),textvar=text,width=30,bd=2,bg="white")
enter.place(x=50,y=160)
button=Button(struct,text="Search",font=("Arial",10,"bold"),width=30,bd=2,command=search)
button.place(x=50,y=200)
struct.mainloop()
