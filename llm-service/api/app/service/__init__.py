import torch
from ..manager.analyzer import LLMManager

def embedding(text):
    return LLMManager.embegging(text)



def ask_saiga_by_text(text, questions):
    embeddings = embedding(text)
    vault_embeddings_tensor = torch.tensor(embeddings) 
