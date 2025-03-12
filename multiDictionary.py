import datetime
import math

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
        sbagliate = []
        tic = datetime.datetime.now()
        s = ""
        for parola in words:
            r = rw.RichWord(parola)
            dizionario = self.printDic(language.lower())

            if dizionario.__contains__(parola):
                r.corretta = True

            else:
                r.corretta = False
                sbagliate.append(parola)

        for j in sbagliate:
            s = s + str(j) + "\n"

        toc = datetime.datetime.now()
        print(f"Using contains \n{s}Time elapsed: {(toc-tic).total_seconds()}\n______________________________")

    def searchWordLinear(self, words, language):
        sbagliate = []
        tic = datetime.datetime.now()
        s = ""

        for parola in words:
            r = rw.RichWord(parola)
            dizionario = self.printDic(language.lower())
            i = 0
            for i in dizionario:
                if parola == i:
                    r.corretta = True
                    break
                else:
                    r.corretta = False

            if r.corretta == False:
                sbagliate.append(parola)

        for j in sbagliate:
            s = s + str(j) + "\n"


        toc = datetime.datetime.now()
        print(f"Using Linear search \n{s}Time elapsed: {(toc-tic).total_seconds()}\n______________________________")

    def searchWordDichotomic(self, words, language):
        sbagliate = []
        tic = datetime.datetime.now()
        s = ""

        for parola in words:
            j = 0
            r = rw.RichWord(parola)
            dizionario = self.printDic(language.lower())
            i = math.floor(len(dizionario)/2)

            if dizionario[i] == parola:
                r.corretta = True

            elif dizionario[i] < parola:
                k = i + 1
                list = dizionario[k:]

                for straniera in list:
                    if k < len(list):
                        if parola == straniera:
                            r.corretta = True
                            k = len(list)
                        else:
                            r.corretta = False
                            k += 1
                    else:
                        break


            elif dizionario[i] > parola:
                k = 0
                list = dizionario[:i-1]
                for straniera in list:
                    if k < i:
                        if parola == straniera:
                            r.corretta = True
                            k = i
                        else:
                            r.corretta = False
                            k += 1
                    else:
                        break

            if r.corretta == False:
                sbagliate.append(parola)

        for j in sbagliate:
            s = s + str(j) + "\n"


        toc = datetime.datetime.now()
        print(f"Using Dichotomic search \n{s}Time elapsed: {(toc-tic).total_seconds()}")

