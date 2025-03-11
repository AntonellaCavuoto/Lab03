class Dictionary:
    def __init__(self):
        self.dizionario = []

    def loadDictionary(self,path):
        self.path = path
        input_file = open(self.path, 'r', encoding='utf-8')

        riga = input_file.readline()

        while riga != "":
            self.dizionario.append(riga.strip("\n"))
            riga = input_file.readline()

        input_file.close()
        return self.dizionario

        # ./prova/testo.txt

    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict