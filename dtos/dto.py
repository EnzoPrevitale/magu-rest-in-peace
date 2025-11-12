from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class MovieDto:
    id: int
    title: str
    director_id: int
    duration: float
    release_date: date
    
    # fk para idioma
