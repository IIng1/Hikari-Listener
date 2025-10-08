import torch
import random, string
from src.p_data import SPEECH_MODEL_ID as id
from transformers import AutoProcessor, BarkModel
from scipy.io.wavfile import write as write_wav

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

processor = AutoProcessor.from_pretrained(id)
model = BarkModel.from_pretrained(id)
model.to(device)

def inference(text, voice_preset):
    sampling_rate = model.generation_config.sample_rate
    wav_name = ''.join(random.choice(string.ascii_letters) for char in range(50))
    save_as = f"data/audio_result/{wav_name}.wav"
    model_inputs = processor(
        [text],
        voice_preset=voice_preset,
        return_tensors="pt").to(model.device)
    model.eval()
    # Speech synthesis requires significant compute resources.
    # On systems without CUDA or with limited GPU capacity, expect noticeable delays.
    # The current model prioritizes quality over speed, so hardware constraints
    # directly impact performance.
    with torch.no_grad():
        generated_speech_values = model.generate(
            **model_inputs,
            do_sample=True,
        )
    generated_speech_values = generated_speech_values.cpu().numpy().squeeze()
    write_wav(
        filename=save_as,
        rate=sampling_rate,
        data=generated_speech_values
    )

    return save_as