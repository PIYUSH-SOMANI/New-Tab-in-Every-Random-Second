"IMPORT WEBBROWSER" is for opening pages(line 7)
"IMPORT TIME" is to give time period(line 8)
"IMPORT RANDOM" is to choose random website and set time limit(line 9)
"WHILE TRUE" is to run the loop again and again till the shell is closed
"site=random.choice(['google.com','youtube.com','weather.gov'])" new tab will be opened with thesw sites
"visit="http://{}".format(site)" it will get added before the site name
"webbrowser.open(visit)" will open the website in new tab
"sec=random.randrange(5,20)" will choose a random number between 5 and 20
"time.sleep(sec)" is to wiat for some sec And since the while loop is always true this process will get continued
