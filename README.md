# Overview

Music is the medicine of the soul for everybody. The music itself is a universal language that helps us through hard times, good times and any other time. Now a days to be able to listen to music we have to pay a small subscription fee otherwise our music will be interrupted by a random ad. So I will be building a music player in python.

In this project, I created a music player which is  able to add, delete and update songs. The software is connected to the Firestore database where the songs and all its information is to be stored. Also, in order to the music, the program is using pytube and the urllib library to be able to look up the songs on YouTube, and eventually downloaded into your system.

The purpose of this program is to dive more in depth with the Tkinter library and become familiar with the Firestore database.



[Software Demo Video](https://youtu.be/tKrI6juSjXk)

# Cloud Database

The program uses the Firestore Database 

Cloud Firestore is a NoSQL, unlike SQL database, there are no tables or rows. Instead, the data is stored in documents which are organized into collections. The main collection is called "Music" which will store all the other collections and documents pertaining to music files and its information.

# Development Environment

The tools utilized in this software are:

* Github
* Node.js
* Firestore

The programming language used in this program is python. 
The libraries utilized throughout the program are: 
* Firebase_admin
* Pytube
* Urllib
* Playsound
* Tkinter

# Useful Websites

* [Google Firebase](https://firebase.google.com/docs/firestore/data-model)
* [Pypi](https://pypi.org/project/playsound/)

# Future Work

* Improve the user interface.
* Save the downloaded music to google storage instead of the system.
* Improve the speed of the program.