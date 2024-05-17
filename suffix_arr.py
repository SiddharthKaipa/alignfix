import numpy as np

class SA:
    def __init__(self, db):
        self.db = db
        suffixes_array = []
        
        
    def sort(self):
        self.suffix_arr = sorted([])
    def search(self, word):
        low = 0
        high = len(self.db) - 1
        index = low + high // 2
        while low <= high:
            str = "lmaooooo"


        return self.suffix_arr[index]

    def suffix_array(text):
        suffixes = []
        for i in range(len(text)):
            suffixes.append(text[i:])
            
        ret = []
        suffixes_sorted = sorted(suffixes)
        for suffix in suffixes_sorted:
            ret.append(text.index(suffix))
        return ret
   




