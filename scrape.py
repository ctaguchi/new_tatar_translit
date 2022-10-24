from bs4 import BeautifulSoup
import requests
import sys
import time

# tatar_russian.academic.ru
MAX_TATAR = 33463
url_base = sys.argv[1]

# tt_lexicon = []

start = time.time()
with open("tt_lexicon.txt", "a") as f:
    for i in range(9, MAX_TATAR):
        # somehow links up to 9 do not work
        print("Scraping word no. {}".format(i))
        elapsed = time.time()
        print("Elapsed time: {}".format(elapsed - start))
        url = url_base + str(i + 1)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        header = soup.find_all("h1")
        if len(header) == 0:
            print("Dictionary index {} was not found".format(i))
            continue
        word = header[0].get_text()
        f.write("{}\n".format(word))
        # tt_lexicon.append(word) 
        print("Added word {} to the lexicon".format(word))

print("Lexicon created!")