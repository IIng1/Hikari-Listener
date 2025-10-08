import random, string
from gtts import gTTS

def inference(text, lang):
    wav_name = ''.join(random.choice(string.ascii_letters) for char in range(50))
    save_as = f"data/audio_result/{wav_name}.wav"

    tts = gTTS(text, lang=lang)
    tts.save(save_as)

    return save_as