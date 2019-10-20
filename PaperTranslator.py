
import ClassDocument
import BaiduTranslation
import config

class PaperTranslator(object):
    appid =""
    sercekey = ""
    path = ""    
    def __init__(self,id,key):
        self.appid = id
        self.sercekey = key

    def Setpath(self,string):
        self.path = string

    def run(self):
        doc = ClassDocument.myDocument(self.path)


if __name__ == "__main__":
    Pt = PaperTranslator(config.appid,config.sercekey)
    Pt.Setpath(config.path)
 
    Pt.run()
