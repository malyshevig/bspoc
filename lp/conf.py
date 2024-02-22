from dataclasses import dataclass

@dataclass()
class Config:
    period = 30
    filename: str = ""
    technology: str = ""
    directory: str = ""
    session: str = ""
    warmup = 0
    remove_head = 0

