import webbrowser
import random

filename = 'The_Oxford_3000.txt'
randomnum = random.randint(0,3000)


line = random.choice(open(filename).readlines())
url = "https://etymonline.com/word/%s" %line


webbrowser.open(url)
