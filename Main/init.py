"""
IMPORTATION DES BIBLIOTHEQUES
"""

from tkinter import *
from PIL import Image, ImageTk
from pytube import YouTube

"""
Initialisation de la fenetre acceuil  
"""
la_base = Tk()
la_base.geometry("1000x600")
la_base.configure(bg='#F9D371')

logo = Image.open("D:\daniil.py\ADVENUTRE\my_logo.png")
render = ImageTk.PhotoImage(logo)
img = Label(la_base, image=render)
img.place(x=100, y=100)

titre = Label(la_base, text='YT.MP.PI', fg='black', bg='#F9D371', font=('cortana', 35, 'bold'))
titre.place(x=180, y=50)

"""
fenetre pour telecharger le mp3 format de la video
"""


def convert():
    to_convert = Tk()
    to_convert.geometry('500x250')
    to_convert.configure(bg='#F9D371')
    titre = Label(to_convert, text='P U T  L I N K  B E L O W', fg='black', bg='#F9D371', font=('cortana', 20)).pack()

    pasted_link = Entry(to_convert, width=30, background='#EADEDE', font=('cortana', 15))
    pasted_link.place(x=100, y=60)

    def download_mp3():
        lien = pasted_link.get()
        video = YouTube(lien)
        audio = video.streams.get_audio_only()
        audio.download()

    download_mp3 = Button(to_convert, text='D O W N L O A D  M P 3', fg='black', bg='#F55353',
                          activebackground='#C74B50',
                          font=('cortana', 20), command=download_mp3)
    download_mp3.place(x=103, y=105)


"""
fenetre pour telechfrger la video
"""


def download():
    to_download = Tk()
    to_download.geometry('500x250')
    to_download.configure(bg='#F9D371')
    titre = Label(to_download, text='P U T  L I N K  B E L O W', fg='black', bg='#F9D371', font=('cortana', 20)).pack()

    pasted_link = Entry(to_download, width=30, background='#EADEDE', font=('cortana', 15))
    pasted_link.place(x=100, y=60)

    def download_mp4():
        lien = pasted_link.get()
        video = YouTube(lien)
        audio = video.streams.get_highest_resolution()
        audio.download()

    download_mp4 = Button(to_download, text='D O W N L O A D  M P 4', fg='black', bg='#F55353',
                          activebackground='#C74B50',
                          font=('cortana', 20), command=download_mp4)
    download_mp4.place(x=103, y=105)


"""
LE MENU
"""


def menu():
    b1 = Frame(la_base, width=300, height=600, bg='#F55353')  # Le menu dessine
    b1.place(x=700, y=0)

    def le_boutton(x, y, text, bcolor, fcolor, cmd):  # Changement de couleurs des boutons qui dependent des evenements
        def dans_la_zone(b):
            Boutton['background'] = bcolor
            Boutton['foreground'] = '#262626'

        def hors_la_zone(b):
            Boutton['background'] = fcolor
            Boutton['foreground'] = '#262626'

        Boutton = Button(b1, text=text,  # Creation des bouttons
                         width=42,
                         height=20,
                         fg='#262626',
                         border=0,
                         bg=fcolor,
                         activeforeground='#262626',
                         activebackground=bcolor,
                         command=cmd)

        Boutton.bind("<Enter>", dans_la_zone)  # Si mon curseur est sur le boutton
        Boutton.bind("<Leave>", hors_la_zone)  # Si mon curseur est dehors de boutton

        Boutton.place(x=x, y=y)

    le_boutton(0, 0, 'C O N V E R T', '#C74B50', '#F55353', cmd=convert)
    le_boutton(0, 300, 'D O W N L O A D', '#C74B50', '#F55353', cmd=download)

    def retour():
        b1.destroy()

    Button(b1, command=retour, text='C L O S E', border=0, activebackground='#F9D371', bg='#F9D371',
           font=('cortana', 20)).place(x=0, y=0)


Button(la_base, command=menu, text='O P E N', border=0, activebackground='#F9D371', bg='#F9D371',
       font=('cortana', 20)).place(x=850, y=0)

la_base.mainloop()  # Tourner le programme
