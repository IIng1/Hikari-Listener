from develop_utils.core.get_trainer import get

def train(name=False, dataset_path="", system_prompt_id=0):
    trainer = get(dataset_path, system_prompt_id)

    trainer.model.train()
    trainer.train()

    if name != False:
        trainer.model.save_pretrained(f"lora_adapter/{name}/")