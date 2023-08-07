
''' 
    Importando as libs
'''
from fastapi import FastAPI
# import pandas as pd
# import numpy as np

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError




# import gspread
# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request
# from google.oauth2.service_account import Credentials

import json
import os

## ------------------------------------------------------- ## 
app = FastAPI()

''' 
    Metodos da API
'''

# import gspread
# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request

app = FastAPI()

def Read_Sheets (SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, creds):
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets() ## Pegou o arquivo inteiro 
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute() ## aqui que passo qual planilha quero ler e qual intervalo de celulas vou ler
    values = result.get('values', []) ## esse cara que diz se quero pegar os valores ou estilização do google

    return values

def Conection (SCOPES = ['https://www.googleapis.com/auth/spreadsheets']):
    creds = None
    
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds


@app.get("/read_google_sheet/")
async def read_google_sheet(sheet_id: str, range_plan:str):

    
    # Conectar ao Google Sheets
    client = Conection()
    # print(client)
    data = Read_Sheets(sheet_id,range_plan, client)

    return {"data": data}

    


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