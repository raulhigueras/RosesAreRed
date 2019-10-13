from tika import parser

class ArrangedText:
    def __init__(self, file):
        if(file[-3:] == 'pdf'):
            raw = parser.from_file(file)
            self.text = str(raw['content'])
        elif(file[-3:] == 'txt'):
            with open(file, 'r') as txt_file:
                self.text = txt_file.read()

        self._clean()

        self.num_words = len(self.text)
        self.num_diff_words = len(set(self.text))


    def _clean(self):
        self.text = self.text.replace(",","").replace("."," .").lower().replace("?"," ?").replace("¿", "").replace("!", " .").replace("¡", "").replace("(", "")
        self.text = self.text.replace(")","").replace("[","").replace("]","").replace("{","").replace("}","").replace("\n", " ").replace(":", "")
        self.text = self.text.replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "")
        self.text = self.text.replace("9", "").replace("0", "").replace(";", "").replace("  ", " ")
        self.text = self.text.replace("chapter", "").replace(" ii","").replace(" iii","").replace(" iv ","").replace(" v ","").replace(" vi ","").replace(" vii","").replace(" viii","")
        self.text = self.text.replace(" ix ","").replace(" x ","").replace("--","-").replace('"', '')
        self.text = self.text.strip('"')
    def getList(self):
        return self.text.split(" ")
