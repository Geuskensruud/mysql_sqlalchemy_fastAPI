#imports
#pydantic wordt gebruikt omdat dit helpt in de validatie procedure, hierdoor hoeven de functies niet te worden blootgesteld aan een lang proces van validatie 
from pydantic import BaseModel
from typing import List

#Pydantic model voor de gewone (niet indentificerende) attributen voor het het lezen (get-methode) van de data van Acteurs
class SelectFilm(BaseModel):

    #niet identificerende attributen aka niet primary keys van uit models
    naamActeurs :str
    titel  : str
    descriptie  : str
    LeeftijdRestrictie  : str
    genre  : str
    taal  : str
    tijd  : str
    minuten  : int
    rating  : float
    AantalKeerBekeken  : int
   
#Pydantic model aan de hand van de SelectFilm class kan het identificerende (primary-key) attribuut worden gebruikt voor de latere GET methode
class Film(SelectFilm):
    id: int

    #Pydantic modellen zijn compatibel met ORM en daardoor kan het data lezen zonder dat het een dict (notatie gebruikt in models kolommen) is
    class Config:
        orm_mode = True

#Pydantic model aan de hand van de SelectFilm class kan het identificerende (primary-key) attribuut worden gebruikt voor de latere GET methode
class FilmTitle(SelectFilm):
    titel  : str

    #Pydantic modellen zijn compatibel met ORM en daardoor kan het data lezen zonder dat het een dict (notatie gebruikt in models kolommen) is
    class Config:
        orm_mode = True

#Omdat er veel records zijn kan er ook alleen een subset worden getoond
class LimitedFilmInfo(BaseModel):
    limit: int
    offset: int
    data: List[Film]

