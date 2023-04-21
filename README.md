<h1 align="center">
  <em>
  Games Collection App
  </em>
</h1>

<h3 align="center">
  <em>
Simple application created with Python and Tkinter, that allows managing a database through a graphical interface, in this case, it is a personal collection of video games.
  </em>
</h3>

<p align="center">
 <img src="https://github.com/KrysNIN/Games_Collection_App/blob/master/Captura.JPG?raw=true" 
</p>

## Starting:

This repository can be cloned on a regular basis, to run on any local machine.

## Prerequisites:

***Software required to run the script:***

✔ - [Python V3.10](https://www.python.org/downloads/)

✔ - [VSCode](https://code.visualstudio.com/) (Optional)

✔ - [Tkinter]

✔ - [Ttkthemes]

## Files:

***The project is composed of 3 main files:***

▶ ```App.py:``` 

This file is responsible for creating the Graphical User Interface (GUI) that uses the Python tkinter library to create different visual elements such as labels, entries, buttons, and frames to interact with an SQLite database.

***The structure of this file is composed of 4 classes that are inherited from each other:***

- Frames Class: 

  Is responsible for creating all the frames corresponding to each section.

  It will create the buttons frame, to contain the labels and entries to enter the data of the game that you want to incorporate into the database.

  It will create the text frame, which will contain the TreeView in which the database records will be reflected.

  It will create the search frame, which will serve to contain the search bar to search for the games that you wish to find in the database, as well as the "Total"    label, which will reflect the total number of games saved so far.

- Widgets Class:
  
  The Widgets class will inherit the Frames class, and will be in charge of creating the labels and the entries for the different frames.
  
  The labels and entries name, genre, date, company, platform, save and delete belong to the buttons frame.
  
  The labels and entries search and total, belong to the search frame.
  
- TreeView Class:
  
  This class will be in charge of creating and configuring the treeview, in which the information contained in the database will be reflected, forming the columns name, gender, date, company and platform.
  

▶ ```BDDLogic.py:```

This file creates the database and manages the functions that interact with the database and perform corresponding operations, such as saving, searching, and deleting games.

▶ ```games.db:```

This file is the database where all the games are stored. Its columns are Name, Genre, Date, Company, and Platform.

## License

MIT
