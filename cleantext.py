from tika import parser

class ArrangedText:
    def __init__(self, file):
        text_string = ""
        if(file[-3:] == 'pdf'):
            raw = parser.from_file(file)
            text_string = (raw['content'])
            text_string = str(text_string)
        elif(file[-3:] == 'txt'):
            with open(file, 'r') as txt_file:
                text_string = txt_file.read()
                print(text_string)
        arr = self._clean(text_string)
        self.l = text_list = self._getList(arr)
        print(text_list)

    def _clean(self, text):
        text = text.replace(",","").replace("."," .").lower().replace("?"," ?").replace("¿", "").replace("!", " !").replace("¡", "").replace("(", "").replace(")","").replace("[","").replace("]","").replace("{","").replace("}","").replace("\n", " ").replace("  ", " ").replace(":", "").replace(";", "")
        text = text.replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "")
        return text

    def _getList(self, text):
        li = list(text.split(" "))
        return li

    def numberWords(self):
        print(len(self.l))

    def numberDifWords(self):
        text_set = set(self.l)
        print(len(text_set))
