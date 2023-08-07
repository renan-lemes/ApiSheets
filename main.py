
''' 
    Importando as libs
'''
from fastapi import FastAPI
# import pandas as pd
# import numpy as np

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError




import gspread
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
# from google.oauth2.service_account import Credentials

import json
import os

## ------------------------------------------------------- ## 
app = FastAPI()

''' 
    Metodos da API
'''

def Conection (SCOPES = 'https://www.googleapis.com/auth/spreadsheets'):
    scope = SCOPES

    # Carregar as credenciais do arquivo JSON
    creds = None
    if creds and creds.valid:
        creds.refresh(Request())
    else:
        creds = Credentials.from_authorized_user_info(
            "token.json", scopes=scope
        )

    client = gspread.authorize(creds)
    return client



## interesante o fastapi 
@app.post('/SheetsPull') 
async def SheetsPull (data:dict):
    cred = Conection()

    return {"value":'ok'}


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