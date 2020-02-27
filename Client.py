import tkinter
from tkinter import *
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.1.209"
port =8000
s.connect((host,port))

produkt = 0
r = tkinter.Tk()


def counter():
    global produkt
    produkt = produkt+1
    print(produkt)


def ts():
    global produkt
    produkt = produkt+1
    string = str(produkt)
    s.send(string.encode())
    data = ''
    data = s.recv(1024).decode()
    print (data)


def main():
    r.title("DU ER LOGGET IND SOM ")
    w = Label(r, text="Bestil 1")
    w.pack()
    button = tkinter.Button(r, text='Tryk Her', width=10, command=ts)
    button.pack()
    r.mainloop()