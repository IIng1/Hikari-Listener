import src.core.text_tokenize as tokenizer
from src.p_data import SENTENCE_MODEL_ID as id
from develop_utils.dataset.from_csv import get_dataset
from develop_utils.core.training_config import lora_config, trainer_args
from transformers import AutoModelForCausalLM
from peft import get_peft_model
from trl import SFTTrainer

def get(dataset_path, system_prompt_id):
    model = AutoModelForCausalLM.from_pretrained(
        id,
        device_map="auto",
        trust_remote_code=True
    )
    dataset = get_dataset(dataset_path, system_prompt_id)

    model = get_peft_model(model, lora_config)
    dataset = dataset.map(tokenizer.s)

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        args=trainer_args
    )

    return trainer