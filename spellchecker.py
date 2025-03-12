import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.m = md.MultiDictionary()


    def handleSentence(self, txtIn, language):
        frase = replaceChars(txtIn)
        campi = frase.lower().split(" ")
        self.m.searchWord(words=campi, language=language)
        self.m.searchWordLinear(campi, language)
        self.m.searchWordDichotomic(campi, language)
    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
        chars ="\\'}*_{}[]()>#+-.!$%^;,=_?"
        for c in chars:
            text = text.replace(c, "")
        return text

