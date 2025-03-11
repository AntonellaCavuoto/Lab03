import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dItaliano = d.Dictionary().loadDictionary("./resources/Italian.txt")

    def printDic(self, language):
        if language == "italian":
            self.dItaliano = d.Dictionary().loadDictionary("./resources/Italian.txt")
            return self.dItaliano
        elif language == "english":
            self.dEnglish = d.Dictionary().loadDictionary("./resources/English.txt")
            return self.dEnglish
        elif language == "spanish":
            self.dSpanish = d.Dictionary().loadDictionary("./resources/Spanish.txt")
            return self.dSpanish


    def searchWord(self, words, language):
        for parola in words:
            r = rw.RichWord(parola)
            dizionario = self.printDic(language.lower())
            if parola in dizionario:
                r.corretta = True
            else:
                r.corretta = False
                print(parola)





