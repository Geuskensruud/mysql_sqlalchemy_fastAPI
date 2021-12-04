#Imports
from typing import List
from sqlalchemy.orm import Session
from models import FilmInfo

#GET functie om een lijst met alle films terug te krijgen
def get_All_Films(session: Session, limit: int, offset: int) -> List[FilmInfo]:
    all_films = session.query(FilmInfo).offset(offset).limit(limit).all()
    return all_films

#GET functie om een lijst met alle films terug te krijgen
def get_All_Films_limit_offset(session: Session, limit: int, offset: int) -> List[FilmInfo]:
    all_films = session.query(FilmInfo).offset(offset).limit(limit).all()
    return all_films

#GET functie om een specifieke films terug te krijgen
def get_specific_film_by_id(session: Session, id: int) -> FilmInfo:
    specific_film_by_id = session.query(FilmInfo).get(id)
    return specific_film_by_id
