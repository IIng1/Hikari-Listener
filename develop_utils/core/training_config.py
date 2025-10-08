from torch.cuda import is_bf16_supported
from peft import LoraConfig, TaskType
from transformers import TrainingArguments

lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)

trainer_args = TrainingArguments(
    output_dir="./lora_adapter",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    logging_steps=10,
    save_strategy="epoch",
    bf16=is_bf16_supported(),
    optim="adamw_torch",
    report_to="none",
    save_total_limit=1
)