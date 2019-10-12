import random
from rhymer import getRhymes

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
        pass

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


    def _getFirstWords(self, w0):
        k = list(self.P1[w0].keys())
        v = list(self.P1[w0].values())
        w1 = random.choices(k, weights = v, k = 1)[0]

        k = list(self.P2[w0][w1].keys())
        v = list(self.P2[w0][w1].values())
        w2 = random.choices(k, weights = v, k = 1)[0]

        return w1, w2


    def _getNextWord(self, w2, w1, w0):
        k = list(self.P3[w0][w1][w2].keys())
        v = list(self.P3[w0][w1][w2].values())
        w3 = random.choices(k, weights = v, k = 1)[0]

        return w3


    def train(self, text):
        #text = text.split(" ")

        text = open(text, "r").read().split(" ")

        self._computeP1(text)
        self._computeP2(text)
        self._computeP3(text)

        self.trained = True


    def _getRhyme(self, w):
        rhymes_list = getRhymes(w)
        for word in rhymes_list:
            if word in self.P1: #and word in self.P2["."]:
                return word

        return "---- NULL ----"

    def generateText(self, n, w):
        assert(n > 3)
        assert(self.trained)

        w0 = self._getRhyme(w)

        w1, w2 = self._getFirstWords(w0)
        sentence = [w2, w1, w0]

        for i in range(n-3):
            print("---", sentence[0], sentence[1], sentence[2])
            w3 = self._getNextWord(sentence[0], sentence[1], sentence[2])
            sentence.insert(0, w3)

        return " ".join(sentence)
