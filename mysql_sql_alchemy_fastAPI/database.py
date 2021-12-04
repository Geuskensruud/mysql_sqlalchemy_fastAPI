#imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creeer een sql_alchemy engine
sqlalchemy_engine = create_engine('mysql+pymysql://root:root@localhost:3306/sakila')

#Creeer de locale session met de sqlalchemy_engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sqlalchemy_engine)

#base geeft een klasse aan deze wordt in de models.py file gebruikt als inheritance voor de ORM modellen
Base = declarative_base()

#
def get_db():
    db = SessionLocal
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
