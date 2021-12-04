#imports
from fastapi import FastAPI
import api

#Initialiseer de fast api aoo via de router uit de api module
app = FastAPI()
app.include_router(api.router)
