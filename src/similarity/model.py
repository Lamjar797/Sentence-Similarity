from sentence_transformers import SentenceTransformer, util


class Similarity:
    def __init__(self)-> None:
        self.model= SentenceTransformer("all-MiniLM-L6-v2")

    def compute(self , sentence1 , sentence2)-> float:

        embeddings1 = self.model.encode(sentence1, convert_to_tensor=True)
        embeddings2 = self.model.encode(sentence2, convert_to_tensor=True)

        # Compute cosine-similarities
        cosine_scores = util.cos_sim(embeddings1, embeddings2)

        return float(cosine_scores.numpy()[0][0])