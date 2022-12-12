
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import urllib.request
import re
from pytube import YouTube
import os
from playsound import playsound
import pyrebase

#Setup the credential to access firebase 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db= firestore.client()
"""firebaseConfig = {

    'apiKey': "AIzaSyCTqF8GmBwrFqWQy4-W2Soo5UIQY92yNbg",
    'authDomain': "clouddatabase-d844c.firebaseapp.com",
    'databaseURL': "https://clouddatabase-d844c-default-rtdb.firebaseio.com",
    'projectId': "clouddatabase-d844c",
    'storageBucket': "clouddatabase-d844c.appspot.com",
    'messagingSenderId': "115042044706",
    'appId': "1:115042044706:web:dce8cbc6119fd443f4737b",
    'measurementId': "G-V10XQF9VGV"
}
firebase =pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()"""


def main():
    print("Welcome to Music Library")
    print()
    print("1.- Show library")
    print()
    print("2.- Add Song")
    print()
    print("3.- Update Song")
    print()
    print("4.- Delete Song")
    print()
    print("5.- Play Song")
    print()
    print("6.- Close")

    try:
        welcome_input = int(input("Please choose one of the options above: "))
    except ValueError:
        exit("\nHy! That's not a number")
    else:
        print("\n")
    
    while welcome_input != 0:
        if welcome_input == 1:
            show_library()
        elif welcome_input == 2:
            add_song()
        elif welcome_input == 3:
            update_song()
        elif welcome_input == 4:
            delete_song()
        elif welcome_input == 5:
            play_song()
        elif welcome_input == 0:
            print("Goodbye!!")
            welcome_input = 0
        else:
            print("Please enter one of the correct choices: ")
            main()

def show_library():
    print("Library: ")
    print()
    print("1.- Show all songs: ")
    print()
    print("2.- Show by Genre: ")
    print()
    

    librarian = int(input(" Please choose one of the options above:  "))

    if librarian == 1:
        show_all()
    elif librarian == 2:
        show_genre()
    

def show_genre():
    print("Genre ")
    genre_nam = input("Which genre would you like to choose? ")
    genre_name = genre_nam.title()
    query = db.collection('Music').document('Genre').collection(genre_name)
    results = query.get()
    for i, result in enumerate(results,1):
        #print(result.to_dict())
        print( i, ".-",result.get('name'))

def show_all():
    print("All Songs: ")
    results = db.collection('Music').document('Genre').collections()
    for result in results:
        for doc in result.stream():
            print( "-",doc.get('name'))


def add_song():
    genr = input("Which genre is your song?  ")
    genre = genr.title()
    na = input("what is the name of the song?  ")
    nam = na.title()
    name = nam.replace(" ","")
    arti = input("Who is the artist?  ")
    artis = arti.title()
    artist = artis.replace(" ","")
    albu = input("What is the album name?  ")
    album = albu.title()
    year = int(input("What year did the song came out?  "))

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + name + artist)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_id = video_ids[0]
    final_video = "https://www.youtube.com/watch?v=" + video_id
    the_songs = YouTube(final_video)
    the_songs = the_songs.streams.get_audio_only()
    the_songs.download(  filename= nam + ".mp3")
    
    
    

    print("done")
    db.collection('Music').document('Genre').collection(genre).document(nam).set({'name' : nam, 'artist' : artis, 'year' : year, 'album' : album, 'url': final_video})

    """storGenre = f"{genre}/{nam}.wav"
    file = f"music\\{nam}.mp3"
    storage.child(storGenre).put(file)
    print("Added!")"""
    
def update_song():
    global update_spec
    global update_genre
    update_gen = input("What genre is the song you would like to change?")
    update_genre = update_gen.title()
    print()
    update_spe = input("Which song would you like to update?")
    update_spec = update_spe.title()

    print()
    print("Updates: ")
    print()
    print("1.- Name ")
    print()
    print("2.- Artist")
    print()
    print("3.- Album")
    print()
    print("4.- Year")
    print()

    updates = int(input("Which field would you like to change? "))

    if updates == 1:
        name_up()
    elif updates == 2:
        artist_up()
    elif updates == 3:
        album_up()
    elif updates == 4:
        year_up()
    
def name_up():
    global update_spec
    global update_genre
    name_updat = input("What is the new name for the song?")
    name_update = name_updat.title()
    print()
    db.collection('Music').document('Genre').collection(update_genre).document(update_spec).update({'name': name_update})

def artist_up():
    global update_spec
    global update_genre
    name_updat = input("What is the new artist  name for the song?")
    name_update = name_updat.title()
    print()
    db.collection('Music').document('Genre').collection(update_genre).document(update_spec).update({'artist': name_update})

def album_up():
    global update_spec
    global update_genre
    name_updat = input("What is the new album name for the song?")
    name_update = name_updat.title()
    print()
    db.collection('Music').document('Genre').collection(update_genre).document(update_spec).update({'album': name_update})

def year_up():
    global update_spec
    global update_genre
    name_update = int(input("What is the new year for the song?"))
    print()
    db.collection('Music').document('Genre').collection(update_genre).document(update_spec).update({'year': name_update})


def delete_song():
    print("Delete: ")
    print()
    update_gen = input("What genre is the song you would like to change?")
    update_genr = update_gen.title()
    delete_spec = input("Which song would you like to delete? ")
    delete_spect = delete_spec.title()
    print()
    db.collection('Music').document('Genre').collection(update_genr).document(delete_spect).delete()


def play_song():
    son = input("Which song would you like to play? ")
    song = son.title()
    results = db.collection('Music').document('Genre').collections()
    for result in results:
        for doc in result.where('name', '==' , song).stream():
            print( "-",doc.get('name'))
    
    playsound(f'music\\{song}.wav')
    print()
    print(f'Now playing {song}...')



main()