from similarity.model import Similarity



sentence1 = [
    "The cat sits outside",
   
]

sentence2 = [
    "The dog plays in the garden",
    
]

model = Similarity()

print(model.compute( sentence1 , sentence2))