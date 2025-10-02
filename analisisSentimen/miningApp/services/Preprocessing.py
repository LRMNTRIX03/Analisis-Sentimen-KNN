import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from ..models import Stopword, Slangword

class PreprocessingServices:
    def __init__(self):
        self.stopword_remover = StopWordRemoverFactory().create_stop_word_remover()
        self.stemmer = StemmerFactory().create_stemmer()
        self.stopwords_db = list(Stopword.objects.values_list("kata", flat=True))
        self.slangwords_db = {sl.kata: sl.kata_baku for sl in Slangword.objects.all()}  
     

    @staticmethod
    def case_folding(teks: str) -> str:
        return teks.lower()

    @staticmethod
    def regex(teks: str) -> str:
        return re.sub(r'[@_!#$%^&*()<>?/\|}{~:]', '', teks)

    @staticmethod
    def symbol_removal(teks: str) -> str:
        teks = re.sub(r'[^a-zA-Z\s]', ' ', teks)  
        teks = re.sub(r'\s+', ' ', teks).strip()  
        return teks

    @staticmethod
    def tokenisasi(teks: str) -> list:
        return teks.split()

    def stopword_removal(self, tokens: list) -> list:
    
        tokens = [t for t in tokens if t not in self.stopwords_db]
       
        teks = " ".join(tokens)
        
        teks = self.stopword_remover.remove(teks)
        return teks.split()

    def slangword_normalization(self, tokens: list) -> list:
      
        return [self.slangwords_db.get(t, t) for t in tokens]

    def stemming(self, tokens: list) -> list:
  
        teks = " ".join(tokens)
        return self.stemmer.stem(teks).split()

    def preprocess(self, teks: str) -> list:
        teks = self.case_folding(teks)
        teks = self.regex(teks)
        teks = self.symbol_removal(teks)
        tokens = self.tokenisasi(teks)
        tokens = self.slangword_normalization(tokens)
        tokens = self.stopword_removal(tokens)
        tokens = self.stemming(tokens)
        return tokens
