from fastapi import FastAPI

# import pandas as pd
# import numpy as np

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

def Conection ():
    pass

app = FastAPI()

## interesante o fastapi 
@app.post('/SheetsPull') 
def SheetsPull (data:dict):
    
    return {'reseive':data}


## Deixar a class para depois fazer o mais cru primeiro
# class GoogleSheets:
    
#     def Conection (self,args):
#         pass

#     def Read (self, args):
#         pass

#     def Update (self, args):
#         pass

#     def Delete (self, args):
#         pass

#     pass

# print("ola")