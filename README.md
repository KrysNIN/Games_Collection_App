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

<h4><em>▶ App.py:</em></h4>

This file is responsible for creating the Graphical User Interface (GUI) that uses the Python tkinter library to create different visual elements such as labels, entries, buttons, and frames to interact with an SQLite database.

***The structure of this file is composed of 4 classes that are inherited from each other:***

- ```Frames Class:```

  Using the Tkinter library as a parameter, is responsible for creating all the frames corresponding to each section.

  It will create the buttons frame, to contain the labels and entries to enter the data of the game that you want to incorporate into the database.

  It will create the text frame, which will contain the TreeView in which the database records will be reflected.

  It will create the search frame, which will serve to contain the search bar to search for the games that you wish to find in the database, as well as the "Total"    label, which will reflect the total number of games saved so far.

- ```Widgets Class:```
  
  The Widgets class will inherit the Frames class, and will be in charge of creating the labels and the entries for the different frames.
  
  The labels and entries name, genre, date, company, platform, save and delete belong to the buttons frame.
  
  The labels and entries search and total, belong to the search frame.
  
- ```TreeView Class:```
  
  This class will inherit the Widgets Class, and be in charge of creating and configuring the treeview, in which the information contained in the database will be reflected, forming the columns name, gender, date, company and platform.
  
- ```Functions Class:```
  
  This class will inherit the TreeView class, and will be in charge of creating the logical functions of the application.
  
  The ```refresh_treeview``` argument will update the TreeView every time a game is saved, deleted or searched in the database.
  
  The ```clean_fields``` argument will clean the name, genre, date, company and platform fields, each time a game is saved to the database.
  
  The ```totals``` argument will display the number of index totals saved in the database so far, just like saving or deleting a game from the database.
  
  The ```save``` argument will be in charge of saving the information entered in the fields, in the database, taking into account that no field can be left empty when loading the information, and it will not admit titles that are repeated.
  
  The ```delete``` argument will be in charge of deleting the index that is being focused on when deleting the record from the database.
  
  The argument ```order_fecha``` will be in charge of ordering all the records from lowest to highest according to the year that has been assigned to each game. This will happen if you click on the "Date" label of the TreeView.
  
  The ```buscar_juego``` argument will be in charge of performing the search in the database by name, according to the name that we have entered in the "Search" entry, and will show the results in the TreeView.
  
  The ```close_program``` argument will indicate that when the application is closed, an "askokcancel" message will appear, in which the user will be asked if they are sure they want to exit, and will be given the option to accept or cancel.

<h4><em>▶ BDDLogic.py:</em></h4>

This file creates the database and manages the functions that interact with the database and perform corresponding operations, such as saving, searching, and deleting games.
  
***The structure of this file is composed of 8 functions:***
  
- ```crear_conexion:```
  
  This function is in charge of creating the structure of the database, and creating the connection to be able to interact and manage the database.
  
- ```get_juegos```
  
  This function will be in charge of searching for all the records in the database and returning them in ascending order.
  
- ```save_game```
  
  This function will be in charge of inserting the data entered in the entries, to save them in the database.
  
- ```delete_game```
  
  This function will be in charge of eliminating a record selected by the selected focus in the treeview.
  
- ```order_by_date```
  
  This function will be in charge of searching for all the records saved in the database, and returning them in order of Date, in ascending order.
  
- ```search_game```
  
  This function will search for all the records that match the data entered in the "Search Game" field by name, and will return all possible matches.
 
- ```validation```
  
  This function will verify that the data entered as name in the "Seach Game" field is not repeated in the database. If it is not repeated, it will allow the "save_game" function to continue, but if it is repeated, it will throw a message indicating that this record is already stored in the database.
  
- ```totales```
  
  This function will return the value of all the total records stored up to the moment, and will show them in the "Totals" label.

<h4><em>▶ games.db:</em></h4>

This file is the database where all the games are stored. Its columns are Name, Genre, Date, Company, and Platform.  

## License

MIT 
