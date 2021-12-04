#imports
from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_All_Films, get_All_Films_limit_offset, get_specific_film_by_id
from database import get_db
from schemas import Film, LimitedFilmInfo

router = APIRouter()


#Class based view van de router om zo de dependencies te verminderen voor sessions
@cbv(router)
#cbv class (films met daarin de session dependency)
class Films_:
    session: Session = Depends(get_db)

    #routing voor het krijgen van alle eerste 1000000 records
    @router.get("/films", response_model=LimitedFilmInfo)
    def FilmList(self, limit: int = 1000000, offset: int = 0):
        film_list = get_All_Films(self.session, limit, offset)
        allFilms = {"limit": limit, "offset": offset, "data": film_list}
        return allFilms
    
    #routing voor het krijgen van een specifiek aantal records met een specifiek aantal overgeslagen records
    @router.get("/films/{limit}/{offset}", response_model=LimitedFilmInfo)
    def FilmList_limit_offset(self, limit: int, offset: int):
        film_list = get_All_Films_limit_offset(self.session, limit, offset)
        allFilms = {"limit": limit, "offset": offset, "data": film_list}
        return allFilms

    #routing voor het krijgen van een specifieke film
    @router.get("/film/{film_id}", response_model=Film)
    def get_specific_film(self, film_id: int):
        specific_film = get_specific_film_by_id(self.session, film_id)
        return specific_film



