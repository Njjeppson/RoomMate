# Overview

By creating this project, I wanted to accomplish the creation of a complex algorithm that accepts detailed information and uses it to determine the single person you would get along with best from a database.

The dataset I am using contains personal information about a variety of people that can be used to determine how well they match up with the user's preferences. The dataset within this project is unique, in that it procedurally grows with each user who provides it with new information. Because of this, I did not obtain the data from anywhere, but rather fed the program sample information throughout my testing that built up into a sort of "example" database over time.

I wrote this software because of an idea I had a few months ago. My first roommate had been a bit problematic, and I was fearful that my new one might be just the same or even worse. I thought "I wish there was an application that let you not only search for someone you get along with, but also found the single best match for your specifications." And then it clicked. I could make it myself.

[Software Demo Video](https://youtu.be/ZpOKwb7lO6s)

# Data Analysis Results

To test out this program, I decided to find the best roommate from the sample data for three different celebrities. Here are the results:
~~~
Jeff Bezos would get along with: Jeffrey Epstein

Taylor Swift would get along with: Ariana Grande

The Green Giant would get along with: Chef Boyardee
~~~
# Development Environment

I developed this software using the Pylance Python extention within Visual Studio Code.
For the database, I used a dictionary within a JSON file.

# Useful Websites

* [Python.org](http://python.org)
* [Json.org](https://www.json.org/json-en.html)
* [W3Schools.com/python](https://www.w3schools.com/python/)
* [W3Schools.com/js](https://www.w3schools.com/js/js_json_intro.asp)

# Future Work

* At the moment, the database is small and only contains my own examples. In the future, I hope to fill the database with much more information from actual people.
* I am considering converting from a JSON file to a web-based database so that the information can be stored and accessed from multiple devices.
* I am also considering creating a mobile or web app for this program in order to make it more accessable.