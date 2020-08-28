Okay so I did this project for Internshalla's competition "Python Programming". I made this project in PyCharm Community version and using Python 3.7x. The iccui.py is the main script. What this program does is that it gets the ODi ranking data of batsmen , bowlers and All Rounders and saves them to a data base (ICC_ODI_RANKING.db). The a GUI opens that lets you select the genre (Batting , Bowling or All-Rounder) and enter any desired rank. As soon as you click get rank , the script retrieves the data associated to the rank and genre you selected and even lets your computer dictate your selection using Python Text TO Speech Module. Enjoy)

libraries req. are as under:

bs4		### Beautiful Soup 4
requests		### Url Request Library
sqlite3		### SQLite 3 RDBMS library
PyQt5		### PyQt5 Python GUI library
pyttsx3		### Python Text To Speech Library

Please Note :

1) The script was written using Python 3.7x and iccui.py is the main file that has to be run.
2) If ICC_ODI_RANKING.db is not available to you, only then remove the comment block in the Lines 8,9,10 in the file     iccui.py
3) Files ICC_ALL_ROUNDER_RANK.py , ICC_BAT_RANKS.py , ICC_BOWL_RANK.py , iccui.py and    ICC_ODI_RANKING.db need to be in the same directory.
4) To view icc.ui file you need Designer.exe (available in PyQt5 package).
5) To view ICC_ODI_RANKING.db file you need to install SQLite from the web.
