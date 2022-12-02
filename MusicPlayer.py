from tkinter import *
import tkinter as tk
import tkinter.messagebox
from pygame import mixer
import os
from PIL import ImageTk, Image
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import urllib.request
import re
from pytube import YouTube



# Use the application default credentials.
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db= firestore.client()



#Show Music Library
def openLibrary():
    global text, music
    root1 = Tk()
    root1.geometry("400x700")
    root1.resizable(False,False)
    image = ImageTk.PhotoImage(file = r'assets\libraryWindows.png', master = root1)
    backgroundLibraryWindows = Label(root1, image=image, bd=0)
    backgroundLibraryWindows.place(x=0,y=0)
    frame = Frame(root1)
    frame.pack()
    #Play button
    player_song = ImageTk.PhotoImage( file = r'assets\play.png', master = root1)
    button_play = Button(root1, image= player_song, bd=0, relief=RIDGE,  background="#e6bcb6", command=playSong, height=40)
    button_play.place(x=148, y = 490)

    #Stop button
    stoper_song = ImageTk.PhotoImage( file = r'assets\stop.png', master = root1)
    button_play1 = Button(root1, image= stoper_song, bd=0, relief=RIDGE,  background="#e6bcb6", command=mixer.music.stop, height=40)
    button_play1.place(x=148, y = 550)

    #Pause
    pauser_song = ImageTk.PhotoImage( file = r'assets\pause-button.png', master = root1)
    button_play2 = Button(root1, image= pauser_song, bd=0, relief=RIDGE,  background="#e6bcb6", command=mixer.music.pause, height=40)
    button_play2.place(x=60, y = 515)

    #Unpause
    unpauser_song = ImageTk.PhotoImage( file = r'assets\resume.png', master = root1)
    button_play3 = Button(root1, image= unpauser_song, bd=0, relief=RIDGE,  background="#e6bcb6", command=mixer.music.unpause, height=40)
    button_play3.place(x=230, y = 515)

    #This is to search in the database
    #query = db.collection('Music').document('Genre').collections()


    music = Label(root1, text="", font=("arial", 12), fg="black", bg="#e6bcb6")
    music.place(x = 140, y= 440)

    #Place it on a text box in the app
    text = Listbox(root1,font = ("Times New Roman", 15), cursor= "hand2", bd = 0)
    scroll_bar = Scrollbar(root1,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 25, y = 120, width = 340, height = 300)
    path = r'C:\Users\lhida\OneDrive - BYU-Idaho\Documents\Music Player Ui\Music'
    if  path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            text.insert(END,song)
    """for result in query:
        for doc in result.stream():
            text.insert(tk.END,'- ' +  doc.get('name') + '\n')"""
    


            
    root1.mainloop()

def addSong():

    global genre, artist, name, album , year

    root2 = Tk()
    root2.geometry("400x700")
    root2.resizable(False,False)
    image = ImageTk.PhotoImage(file = r'assets\addSong.png', master = root2)
    backgroundLibraryWindows = Label(root2, image=image, bd=0)
    backgroundLibraryWindows.place(x=0,y=0)
    frame = Frame(root2)
    frame.pack()

    #Genre:
    genre = tkinter.Entry(root2)
    genre.place( x = 140, y= 165, height = 30, width = 230)
    entry_genre = genre.get()
    entry_genre_string = str(entry_genre)
    entry_genre_title = entry_genre_string.title()
    

    #Name:
    name = tkinter.Entry(root2)
    name.place( x = 140, y= 238, height = 30, width = 230)
    entry_name = name.get()
    entry_name_string = str(entry_name)
    entry_name_title = entry_name_string.title()
    entry_name_nospace = entry_name_title.replace(" ","")

    #Artist:
    artist = tkinter.Entry(root2)
    artist.place( x = 140, y= 305, height = 30, width = 230)
    entry_artist = artist.get()
    entry_artist_string = str(entry_artist)
    entry_artist_title = entry_artist_string.title()
    entry_artist_nospace = entry_artist_title.replace(" ","")

    #ALbum:
    album = tkinter.Entry(root2)
    album.place( x = 140, y= 378, height = 30, width = 230)
    entry_album = album.get()
    entry_album_string = str(entry_album)
    entry_album_title = entry_album_string.title()

    #Year:
    year = tkinter.Entry(root2)
    year.place( x = 140, y= 450, height = 30, width = 230)
    entry_year = year.get()
    entry_year_int = str(entry_year)
    #Button!
    submit_buttons = ImageTk.PhotoImage(file = r'assets\enter_add_song.png', master = root2)
    add_button = Button(root2, image = submit_buttons, borderwidth=0, command= song_has_been_added)
    add_button.place(x= 120, y=540, height=45, width=180)
    root2.mainloop()
    
def song_has_been_added():

    global genre, artist, name, album , year
    
    root3 = Tk()
    root3.geometry("400x700")
    root3.resizable(False,False)
    added_song = ImageTk.PhotoImage(file = r'assets\song_added.png', master = root3)
    added_song_background = Label(root3, image = added_song, bd = 0)
    added_song_background.place(x = 0, y = 0)
    frame = Frame(root3)
    frame.pack()

    #Genre:
    entry_genre = genre.get()
    entry_genre_string = str(entry_genre)
    entry_genre_title = entry_genre_string.title()
    

    #Name:
    entry_name = name.get()
    entry_name_string = str(entry_name)
    entry_name_title = entry_name_string.title()
    entry_name_nospace = entry_name_title.replace(" ","")

    #Artist:
    entry_artist = artist.get()
    entry_artist_string = str(entry_artist)
    entry_artist_title = entry_artist_string.title()
    entry_artist_nospace = entry_artist_title.replace(" ","")

    #ALbum:
    entry_album = album.get()
    entry_album_string = str(entry_album)
    entry_album_title = entry_album_string.title()

    #Year:
    entry_year = year.get()
    entry_year_int = str(entry_year)


    # look for the video in youtube
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + entry_name_nospace + entry_artist_nospace)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_id = video_ids[0]
    final_video = "https://www.youtube.com/watch?v=" + video_id
    the_songs = YouTube(final_video)
    the_songs = the_songs.streams.get_audio_only()
    the_songs.download(  filename= entry_name_title + ".mp3", output_path= r'Music')

    # Added into the Data Base
    db.collection('Music').document('Genre').collection(entry_genre_title).document(entry_name_title).set({'name' : entry_name_title, 'artist' : entry_artist_title, 'year' : entry_year_int, 'album' : entry_album_title, 'url': final_video})
   

    #Open a text box in the GUI
    text = tk.Text(root3,font = ("Times New Roman", 15), bd = 5, spacing1= 12 , wrap = WORD)
    scroll_bar = Scrollbar(root3,command=text.yview)
    scroll_bar.pack(side =RIGHT, fill = Y)
    text['yscrollcommand'] = scroll_bar.set
    text.place(x = 20, y = 120, width = 340, height = 550)
    query = db.collection('Music').document('Genre').collections()
    for result in query:
        for doc in result.stream():
            text.insert(tk.END,'- ' +  doc.get('name') + '\n')
    
    
    root3.mainloop()
    
def playSong():
    
    music_name  = text.get(ACTIVE)
    mixer.music.load(text.get(ACTIVE))
    mixer.music.play()
    music.config(text = music_name[0:-4])

def deleteSong():

    global name_to_be, gen_to_be
    root4 = Tk()
    root4.title("Musify by Luis")
    root4.geometry("400x500")
    root4.resizable(False,False)
    mainWindowPicture = ImageTk.PhotoImage(file = r'assets\deleteSong.png', master = root4)
    backgroundMainWindow = Label(root4, image= mainWindowPicture, bd = 0)
    backgroundMainWindow.place(x=0, y=0)
    frame = Frame(root4)
    frame.pack()

    #Genre:
    gen_to_be = tkinter.Entry(root4)
    gen_to_be.place( x = 140, y= 180, height = 30, width = 230)

    #Name:
    name_to_be = tkinter.Entry(root4)
    name_to_be.place( x = 140, y= 270, height = 30, width = 230)
    

    #Button!
    submit_buttons = ImageTk.PhotoImage(file = r'assets\deleteforreals.png', master = root4)
    add_button = Button(root4, image = submit_buttons, borderwidth=0, command= deleted)
    add_button.place(x= 115, y=390, height=45, width=180)
    

    root4.mainloop()

def deleted():
    root5 = Tk()
    root5.title("Musify by Luis")
    root5.geometry("400x400")
    root5.resizable(False,False)
    mainWindowPicture = ImageTk.PhotoImage(file = r'assets\deleted.png', master = root5)
    backgroundMainWindow = Label(root5, image= mainWindowPicture, bd = 0)
    backgroundMainWindow.place(x=0, y=0)
    frame = Frame(root5)
    frame.pack()

    entry_genre_to_be = gen_to_be.get()
    entry_genre_string_to_be = str(entry_genre_to_be)
    entry_genre_title_to_be = entry_genre_string_to_be.title()


    entry_name_to_be = name_to_be.get()
    entry_name_string_to_be = str(entry_name_to_be)
    entry_name_title_to_be = entry_name_string_to_be.title()

    db.collection('Music').document('Genre').collection(entry_genre_title_to_be).document(entry_name_title_to_be).delete()


    path = rf'C:\Users\lhida\OneDrive - BYU-Idaho\Documents\Music Player Ui\Music\{entry_name_title_to_be}.mp3'
    os.remove(path)
    
    root5.mainloop()





#Main Window
root = Tk()
root.title("Musify by Luis")
root.geometry("400x700")
root.resizable(False,False)
mixer.init()
mainWindowPicture = ImageTk.PhotoImage(file = r'assets\Main Window.png')
backgroundMainWindow = Label(root, image= mainWindowPicture, bd = 0)
backgroundMainWindow.place(x=0, y=0)

#library button
library_button = ImageTk.PhotoImage(file = r'assets\library.png')
button_library = Button(root, image= library_button, command= openLibrary, bd=0, relief=RIDGE, height=60, background="#e6bcb6")
button_library.place(x=148, y = 100)

#add song 
add_button = ImageTk.PhotoImage(file = r'assets/add.png')
button_add = Button(root, image= add_button, command= addSong, bd=0, relief=RIDGE, height=95,width=95, background="#e6bcb6")
button_add.place(x = 148, y =230 )

#delete song 
delete_button = ImageTk.PhotoImage(file = r'assets/delete.png')
button_delete = Button(root, image= delete_button, command= deleteSong, bd=0, relief=RIDGE, height=95,width=95, background="#e6bcb6")
button_delete.place(x = 148, y =390 )


frame = Frame(root)
frame.pack()

#Icon
image_icone = PhotoImage(file = r'assets\Musify.png' )
root.iconphoto(False, image_icone)

#Execute main loop
root.mainloop()
