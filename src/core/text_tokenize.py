from transformers import AutoTokenizer
from src.p_data import SENTENCE_MODEL_ID as id

tokenizer = AutoTokenizer.from_pretrained(
    id,
    trust_remote_code=True
)
tokenizer.pad_token = tokenizer.eos_token

def s(dataset):
    return tokenizer(dataset["text"], padding="max_length", truncation=True, max_length=1024)