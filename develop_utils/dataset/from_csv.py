import pandas as pd
from datasets import Dataset
from src.core.text_tokenize import tokenizer
from src.p_data import SYSTEM_PROMPT as sp

def template(prompt, completion, system_prompt):
    prompt = prompt.replace('"[{', '[{')
    prompt = prompt.replace('}]"', '}]')
    completion = completion.replace('"[{', '[{')
    completion = completion.replace('}]"', '}]')

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": completion}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    return text

def get_dataset(path, system_prompt_id):
    system_prompt = sp[system_prompt_id]
    df = pd.read_csv(path)
    df = df.dropna()
    df["text"] = df.apply(lambda row: template(row["prompt"], row["completion"], system_prompt), axis=1)
    df = Dataset.from_pandas(df[["text"]])
    df = df.shuffle(seed=111)
    return df