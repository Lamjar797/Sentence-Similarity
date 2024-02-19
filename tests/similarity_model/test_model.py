import pytest
from src.similarity.model import Similarity


class Test:    
    def test_predict(self):
        model = Similarity()

        sentence1 = "The cat sits outside" 
        sentence2 = "The dog plays in the garden"

        predict = model.compute(sentence1 , sentence2)

        assert isinstance(predict , float) == True



