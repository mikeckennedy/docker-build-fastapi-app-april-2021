from typing import List

from pydantic import BaseModel


class MovieModel(BaseModel):
    title: str
    keywords: List[str] = []
    director: str
    year: int
