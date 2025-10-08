import streamlit as st
from src.p_data import SENTENCES_LENGTH, SYSTEM_PROMPT
from src.core.text_model import inference
from src.core.text_tokenize import tokenizer

def s(conf):
    settings = st.session_state.p_settings

    request = f"[{{'task': 'text_generation'}}, {{'language': '{conf.language}'}}, {{'level': '{conf.level}'}}, {{'text_type': '{conf.text_type}'}}, {{'text_lenght': '{SENTENCES_LENGTH[conf.text_length]}'}}]"
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT[0]},
        {"role": "user", "content": f'"{request}"'}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # Temperature controls creativity vs. determinism in text generation.
    # If outputs deviate from configuration or contain artifacts, lower the temperature
    # (typical stable range: 0.7-1.0).
    # Warning: excessively low values may cause repetitive or overly similar results.
    return inference(
        LoRA_id=0,
        temperature=settings.sentence_temperature,
        text=text
    )