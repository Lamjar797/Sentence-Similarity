from fastapi import FastAPI
from similarity import model
from Input import sentences
import time
app = FastAPI()
model = model.Similarity()

@app.get("/")
async def root():         
    return {'message' : "Hello World"}



@app.post("/Similarity")
def similarity(sentences:sentences):
    start = time.time()
    score = model.compute(sentences.sentence1 , sentences.sentence2)
  
  
  
    compute_time = time.time() - start

    return { compute_time : compute_time, score : score}

