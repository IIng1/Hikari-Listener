SENTENCE_MODEL_ID = "Qwen/Qwen1.5-0.5B-Chat"
SPEECH_MODEL_ID = "suno/bark"

DATASET_PATH = [
    "data/SENTENCE_DATASET.csv",
    "data/CHECKING_DATASET.csv"
]

STATISTICS_PATH = "data/statistics/data.json"

LORA_ADAPTER_PATH = [
    "IIng1/Hikari-0.5B-Sentence-Adapter",
    "IIng1/Hikari-0.5B-Checking-Adapter"
]

SYSTEM_PROMPT = [
    "You are a sentence generator. You need to follow the user configuration.",
    "You are a translation checker. You need to check user text translations and correct any mistakes."
]

LANGUAGES = [
    "not selected",
    "Chinese",
    "Korean",
    "Spanish",
    "French",            # NOT LEARNED
    "Portuguese",        # NOT LEARNED
    "Japanese"
]

LANGUAGES_LEVELS = {
    "not selected": ["not selected"],
    "Chinese": ["HSK 1", "HSK 2", "HSK 3", "HSK 4", "HSK 5", "HSK 6"],
    "Korean": ["TOPIK 1", "TOPIK 2", "TOPIK 3", "TOPIK 4", "TOPIK 5", "TOPIK 6"],
    "Spanish": ["CEFR A1", "CEFR A2", "CEFR B1", "CEFR B2", "CEFR C1", "CEFR C2"],
    "Ukrainian": ["CEFR A1", "CEFR A2", "CEFR B1", "CEFR B2", "CEFR C1", "CEFR C2"],
    "French": ["CEFR A1", "CEFR A2", "CEFR B1", "CEFR B2", "CEFR C1", "CEFR C2"],
    "Arabic": ["CEFR A1", "CEFR A2", "CEFR B1", "CEFR B2", "CEFR C1", "CEFR C2"],
    "Portuguese": ["CEFR A1", "CEFR A2", "CEFR B1", "CEFR B2", "CEFR C1", "CEFR C2"],
    "Japanese": ["JLPT N5", "JLPT N4", "JLPT N3", "JLPT N2", "JLPT N1"]
}

SENTENCES_LENGTH = {
    "short": "5-10",
    "medium": "10-20",
    "long": "20-35",
    "very long": "35-50"
}

LANGUAGES_CODE = {
    "Chinese": "zh",
    "Korean": "ko",
    "Spanish": "es",
    "French": "fr",            # NOT LEARNED
    "Portuguese": "pt",        # NOT LEARNED
    "Japanese": "ja"
}

RATE = {
    5: "GOOD JOB, EVERYTHING IS CORRECT! 👍😁",
    4: "GREAT, VERY CLOSE TO PERFECT! 🤏😀",
    3: "FINE, YOU UNDERSTOOD HALF OF THE SENSE! 👌🙂",
    2: "YOU STILL HAVE A LOT TO LEARN! ✍️😕",
    1: "A START HAS BEEN MADE, BUT NOTHING MORE! 👂😔",
    0: "ARE YOU SURE YOU HAVE SELECTED THE RIGHT LANGUAGE? 👋😅"
}

CALENDAR_LABELS = "<div class='labels'><div>Mo</div><div>Tu</div><div>We</div><div>Th</div><div>Fr</div><div>Sa</div><div>Su</div></div>"

CALENDAR_PALETTES = {
        "green": ["#ebedf0", "#c6e48b", "#7bc96f", "#239a3b", "#196127", "#0d3d12"],
        "blue":  ["#ebedf0", "#c6ddf9", "#89c4f4", "#4096ee", "#236ab9", "#0b3d91"]
    }

WARNING_TEXT = """ This system is currently under development.
        The LoRAs adapter has been trained on small datasets,
        so it may provide incorrect results.
        It does not fully follow the instructions for text length and level.
        It may also give an incorrect rating of your answer
        and make corrections even when it is not necessary.
        With this in mind, please note that at this stage,
        the system is intended for familiarization purposes only, not for learning."""

RECOMMENDATIONS_FOR_STABILITY = """ If the systems are working too badly,
        you can lower creativity (temperature) in the settings.
        This should give a better result, but a more similar output."""

ROADMAP = {
    "done": [
        "Develop a preview of the WEB-UI using StreamLit",
        "Research, evaluation, and selection of models",
        "Implementation of basic functionality",
        "Generate preview dataset (currently in use) for fine-tuning LoRA adapters",
        "Fine-tuning LoRA adapters for each task and improving inference",
        "Add the TTS model (suno/bark)",
        "Add a listening page with colordiff and user translation rating",
        "Add a statistics page for activity and ratings",
        "Add Google-TTS for low-performance PCs"
    ],
    "todo": [
        "Develop an API for functionality",
        "Development of utilities for expanding datasets",
        "Expanding the dataset with new utilities",
        "Re-fine-tuning with a new data set to improve inference results",
        "Enhance the listening page with detailed translation feedback",
        "Add a new type of WEB-UI (HTML + CSS / Gradio)",
        "Further improvements and features to be determined later"
    ]
}