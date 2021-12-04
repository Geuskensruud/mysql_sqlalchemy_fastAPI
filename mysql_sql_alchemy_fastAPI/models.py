#imports 
#vanuit de database wordt Base gehaald voor inheritance
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Float
from database import Base


#Class die de Base inherit, vanuit de database is de view acteurs gebruikt met de onderstaande kolommen
class FilmInfo(Base):
    #tabelnaam vanuit de database
    __tablename__ = "films"

    #kolomnamen + titel is de primary key
    id = Column(Integer, primary_key=True, index=True)
    naamActeurs = Column(String, primary_key=False, index=False)
    titel  = Column(String, primary_key=False, index=False)
    descriptie  = Column(String, primary_key=False, index=False)
    LeeftijdRestrictie  = Column(String, primary_key=False, index=False)
    genre  = Column(String, primary_key=False, index=False)
    taal  = Column(String, primary_key=False, index=False)
    tijd  = Column(String, primary_key=False, index=False)
    minuten  = Column(Integer, primary_key=False, index=False)
    rating  = Column(Integer, primary_key=False, index=False)
    AantalKeerBekeken  = Column(Integer, primary_key=False, index=False)