import pytest
from .src.similarity.model import Similarity

class Test():

    
    def predict_test():
        model = Similarity.compute()

        sentence1 = "The cat sits outside" 
        sentence2 = "The dog plays in the garden"

        predict = model(sentence1 , sentence2)

        return isinstance(predict , float )



