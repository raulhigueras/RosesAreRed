import requests

def getRhymes(word):
    URL = "https://api.datamuse.com/words?rel_rhy=%s" % word
    r = requests.get(url = URL)
    data = r.json()
    res = list()
    for dict in data:
        res.append(dict['word'])

    return res
