import torch
from src.core.get_peftmodel import get
from src.core.text_tokenize import tokenizer

def inference(LoRA_id, temperature, text):
    model = get(LoRA_id)

    model_inputs = tokenizer(
        [text],
        return_tensors="pt").to(model.device)
    model.eval()
    with torch.no_grad():
        generated_ids = model.generate(
            **model_inputs,
            do_sample=True,
            temperature=temperature,
            top_k=500,
            max_new_tokens=100
        )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response