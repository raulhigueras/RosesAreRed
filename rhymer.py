import requests

def getRhymes(word):
    URL = "https://rhymebrain.com/talk?function=getRhymes&word=%s" % word
    r = requests.get(url = URL)
    data = r.json()
    res = list()
    for dict in data:
        res.append(dict['word'])

    return res
