from dataclasses import dataclass

class TextConfig(object):
    def __init__(self, language, level, text_type, text_length):
        super().__init__()
        self.language = language
        self.level = level
        self.text_type = text_type
        self.text_length = text_length

@dataclass
class ProjectSettings(object):
    _sentence_temperature: float = 1.2
    _checking_temperature: float = 0.5

    @property
    def sentence_temperature(self):
        return self._sentence_temperature

    @sentence_temperature.setter
    def sentence_temperature(self, temperature: float):
        if not temperature:
            raise ValueError("TEMPERATURE IS NOT SPECIFIED!")
        elif temperature > 2 or temperature < 0:
            raise ValueError("THE SPECIFIED TEMPERATURE IS OUT OF RANGE!")
        self._sentence_temperature = temperature

    @property
    def checking_temperature(self):
        return self._checking_temperature

    @checking_temperature.setter
    def checking_temperature(self, temperature: float):
        if not temperature:
            raise ValueError("TEMPERATURE IS NOT SPECIFIED!")
        elif temperature > 2 or temperature < 0:
            raise ValueError("THE SPECIFIED TEMPERATURE IS OUT OF RANGE!")
        self._checking_temperature = temperature