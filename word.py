from dataclasses import dataclass

@dataclass
class Word:
    name: str
    type: str
    definition_link: str
    eng_level: str