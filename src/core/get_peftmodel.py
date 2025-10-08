import torch
from src.p_data import LORA_ADAPTER_PATH, SENTENCE_MODEL_ID as id
from transformers import AutoModelForCausalLM
from peft import PeftModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Loads specialized LoRA adapters for each task.
# Using task-specific LoRA ensures higher accuracy and prevents "blended" outputs.
# Without this separation, the model may confuse tasks or generate mixed results.
def get(LoRA_id):
    model = AutoModelForCausalLM.from_pretrained(
        pretrained_model_name_or_path=id,
        trust_remote_code=True,
        device_map="auto"
    )
    model = PeftModel.from_pretrained(
        model,
        LORA_ADAPTER_PATH[LoRA_id]
    )

    model.to(device)
    model.eval()

    return model