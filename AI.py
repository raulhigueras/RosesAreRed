import random
import json
from rhymer import getRhymes
from ArrangedText import ArrangedText

class MarkovChain:
    def __init__(self, savedP = None):
        if savedP:
            self.P1, self.P2, self.P3 = self._recoverP(savedP)
            self.trained = True
        else:
            self.P1 = dict()
            self.P2 = dict()
            self.P3 = dict()
            self.trained = False


    def _debug(self, thing):
        print(thing)


    def _recoverP(self, file):
        with open(file, "r") as f:
            data = json.load(f)
            return data[0], data[1], data[2]


    def _saveP(self, file):
        with open(file, "w") as f:
            json.dump([self.P1, self.P2, self.P3], f, indent=1)


    def _computeP1(self, text):
        P = self.P1
        for i in range(1, len(text)):
            w1 = text[i-1]
            w2 = text[i]

            if w2 not in P:
                P[w2] = dict()
            if w1 not in P[w2]:
                P[w2][w1] = 1
            else:
                P[w2][w1] += 1
        self.P1 = P

    def _computeP2(self, text):
        P = self.P2
        for i in range(3, len(text)):
            w1 = text[i-2]
            w2 = text[i-1]
            w3 = text[i]

            if w3 not in P:
                P[w3] = dict()
            if w2 not in P[w3]:
                P[w3][w2] = dict()
            if w1 not in P[w3][w2]:
                P[w3][w2][w1] = 1
            else:
                P[w3][w2][w1] += 1
        self.P2 = P

    def _computeP3(self, text):
        P = self.P3
        for i in range(4, len(text)):
            w1 = text[i-3]
            w2 = text[i-2]
            w3 = text[i-1]
            w4 = text[i]

            if w4 not in P:
                P[w4] = dict()
            if w3 not in P[w4]:
                P[w4][w3] = dict()
            if w2 not in P[w4][w3]:
                P[w4][w3][w2] = dict()
            if w1 not in P[w4][w3][w2]:
                P[w4][w3][w2][w1] = 1
            else:
                P[w4][w3][w2][w1] += 1

        self.P3 = P


    def _getFirstWord(self, w1):
        k = list(self.P2["."][w1].keys())
        v = list(self.P2["."][w1].values())
        w2 = random.choices(k, weights = v, k = 1)[0]

        return w2


    def _getNextWord(self, w2, w1, w0):
        k = list(self.P3[w0][w1][w2].keys())
        v = list(self.P3[w0][w1][w2].values())
        print(k[v.index(max(v))])
        if (k[v.index(max(v))] == str(".")):
            print("entro a nw")
            w3 = str(".")
        else: w3 = random.choices(k, weights = v, k = 1)[0]

        return w3


    def train(self, file):
        text = ArrangedText(file).getList();

        self._computeP1(text)
        self._computeP2(text)
        self._computeP3(text)

        self._saveP("saves/save.txt")


    def _getRhyme(self, w):
        rhymes_list = getRhymes(w)
        random.shuffle(rhymes_list)
        for word in rhymes_list:
            if word in self.P1 and word in self.P2["."].keys():
                return word

        return "---- NULL ----"

    def generateText(self, n, w):
        w0 = "."
        w1 = self._getRhyme(w)
        w2 = self._getFirstWord(w1)
        sentence = [w2, w1, w0]
        i = 2
        while (sentence[0] != "." and i < n):
            print("---", sentence[0], sentence[1], sentence[2])
            w3 = self._getNextWord(sentence[0], sentence[1], sentence[2])
            sentence.insert(0, w3)
            i = i +1
        if (sentence[0] == "."):
            print("we have a dot")
            sentence.pop(0)
        sentence.pop(-1)
        return " ".join(sentence)
