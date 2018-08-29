READ ME First
=============

This program written in python generates a responsive html page that represents
 a movie library.

First Step:
=============

Program requirements:
=====================

To be able to run this program, you must have installed and configured in your
computer a python interpreter with version 2.7 or above. Be sure python's 
environment variable is properly defined for correct python's folder.

How To Insert Records Into the Library:
=======================================

To fill your library database, it is necessary insert records into 
"records.txt" file inside app folder. In each row of file, insert 
the itens like this way (use semicolon to separate the fields):

<Movie Title>;<Duration>;<Description>;
<Movie Banner Link (Thumbnail)>;<Movie's Trailer - Youtube Link>

Example:

Taare Zameen Par;100;A story of special little guy;
https://upload.wikimedia.org/wikipedia/en/b/b4/Taare_Zameen_Par_
Like_Stars_on_Earth_poster.png;https://www.youtube.com/watch?v=F-PAI2HnQUo

WARNING: 
========
-DO NOT BREAK LINE. 
-SEMICOLON IS A RESERVED CHARACTER INTO THE RECORD.TXT FILE, AVOID 
ITS USE IF NOT USED TO SEPARATE THE FIELDS.   


Running the program:
====================

Once the requirements above described are met, copy the app folder into your hard 
drive (preferably into local C:\ ) open the windows or linux terminal, get into 
project's path (app path ex. C:\<PROJECT_FOLDER>) and execute 
entertainment_center.py - copy and paste the command line:

- py entertainment_center.py

If the application ran properly, a web browser will open automatically. 
If not, check out the terminal console to see the error log.

New Releases:
=============

The up coming version will enable users insert new trailers records from
text file insertions.

Futher Information:
===================

The images used in app are from external links and, depending of your
Internet bandwidth, it may takes some seconds to appear on screen. 