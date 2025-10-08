import develop_utils.core.LoRA_training as trainer
from src.p_data import DATASET_PATH
from sys import argv

if __name__ == "__main__":
    name, dataset_id = argv[1], argv[2]
    try:
        dataset_id = int(dataset_id)
        trainer.train(
            name=name,
            dataset_path=DATASET_PATH[dataset_id],
            system_prompt_id=dataset_id
        )
    except (IndexError, ValueError):
        print(f"-- [{dataset_id}] IS NOT AN ARGUMENT --")