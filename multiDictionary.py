import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dItaliano = d.Dictionary().loadDictionary("./resources/Italian.txt")
        self.dEnglish = d.Dictionary().loadDictionary("./resources/English.txt")
        self.dSpanish = d.Dictionary().loadDictionary("./resources/Spanish.txt")

    def printDic(self, language):
        if language == "italian":
            return self.dItaliano

        elif language == "english":
            return self.dEnglish

        elif language == "spanish":
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





