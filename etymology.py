import webbrowser
import random

filename = 'The_Oxford_3000.txt'
randomnum = random.randint(0,3000)

//chooses the random word
line = random.choice(open(filename).readlines())

//creates the url name
url = "https://etymonline.com/word/%s" %line


webbrowser.open(url)
