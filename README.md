# Overview

This software takes my previously designed RoomMate algorithm and integrates it with a web database. Firstly, the program retrieves information from the online database and temporarily stores it for editing. Next, the user provides their personal information for entry into the database. The program then takes this information, updates the database, and sends it back to the web. Next, the user specifies what and what not they are looking for in a roommate in order of importance. Finally, the algorithm determines the user's best match and returns the answer.

I wrote this software because, if I was ever to distribute this program, it would be very useful for all users to be able to connect to and store their information within the same database.

[Software Demo Video](https://www.youtube.com/watch?v=zSEnAuod6to)

# Cloud Database

For this project, I used a realtime database from Google Firebase to host my information.

The structure of my web database is largely the same as within my previous program. It is one big dictionary filled with smaller
dictionaries for each person, each of which stores that person's provided information.

# Development Environment

To develop this software, I used Visual Studio Code and Google Firebase.

This program was created using the Python programming language, along with the JSON and Firebase libraries.

# Useful Websites

* [Google Firebase](https://firebase.google.com/)
* [FreeCodeCamp](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/)

# Future Work

* In the future, I may give the program a GUI in order to make it more user-friendly overall.
* Additionally, I intend to look into the idea of potentially converting the program into a mobile or web app.