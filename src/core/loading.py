def load_all():
    yield "torch..."
    import torch
    yield "transformers..."
    import transformers
    yield "datasets..."
    import datasets
    yield "trl..."
    import trl
    yield "peft..."
    import peft
    yield "accelerate..."
    import accelerate
    yield "scipy..."
    import scipy
    yield "gTTS (Google TTS)..."
    import gtts
    yield "pandas..."
    import pandas
    yield "math..."
    import math
    yield "datetime..."
    import datetime
    yield "html..."
    import html
    yield "difflib..."
    import difflib
    yield "random..."
    import random
    yield "string..."
    import string
    yield "json..."
    import json
    yield "(It may take some time to download the model when you launch it for the first time.\nPlease wait!!! 👌🙂)"
    yield "Speech model..."
    import src.core.speech_model
    yield "Text model and LoRA adapters..."
    import src.core.get_peftmodel as t_model
    t_model.get(0)
    t_model.get(1)
    yield "Web-UI Pages..."
    import src.webui.home_page
    import src.webui.config_page
    import src.webui.listening_page
    import src.webui.statistics_page
    yield "DONE!!! 👍😁"