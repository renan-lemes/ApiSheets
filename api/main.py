
''' 
    Importando as libs
'''
from fastapi import FastAPI
import pandas as pd
# import numpy as np

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

## Libs distintas
# import gspread
# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request
# from google.oauth2.service_account import Credentials

import json 
import os

from dotenv import load_dotenv

## ------------------------------------------------------- ## 
## Inicializa a credencial
load_dotenv()

## Inicializa a API
app = FastAPI()

## Carrega o a cred
api_key = os.getenv("API_KEY")

def Conection(SCOPES = ['https://www.googleapis.com/auth/spreadsheets']):

    try:
        if not api_key:
            raise ValueError("API_KEY não encontrada. Verifique seu arquivo .env")

        return api_key
    except Exception as e :
        return f"Not found creds {e}"

def Read_Sheets(SAMPLE_SPREADSHEET_ID, range_page='Página1'):
    try:
        
        service = build('sheets', 'v4', developerKey=api_key)
        sheet = service.spreadsheets() ## Pegou o arquivo inteiro 
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_page).execute()
        values = result.get('values', [])

        return values
    except Exception as e:
        return f"Error reading sheets{e}"

def Search(sheet_id, client,name_pag, valor):
    
    service = build('sheets', 'v4', credentials=client) 
    sheet = service.spreadsheets()
    
    result = sheet.values().get(spreadsheetId=sheet_id, range=name_pag).execute()
    response = result.get('values', [])

    df = pd.DataFrame(response)

    df.reset_index(drop=True, inplace=True)

    value = None

    for i in df.columns:
        if (len(df[df[i] == valor]) > 0):
            value = df[df[i] == valor]
            break

    if value is None or len(value) == 0:
        value = 'Valor não encontrado!!'
    else:
        value = value.values.tolist()

    return value

def Insert_data_pag(sheet_id, client, name_pag, data):

    service = build('sheets', 'v4', credentials=client)
    
    sheet = service.spreadsheets() ## Pegou o arquivo inteiro 

    res = data['data']
    
    # spreedsheets = {
    #     'majorDimension':"ROWS",
    #     'range':att_range,
    #     'values':res
    # }
    
    result = sheet.values().update(spreadsheetId=sheet_id,range=name_pag+'!A1', valueInputOption='USER_ENTERED', body={'values':res}).execute()

    return result

def return_dataframe(data:list):
    ''' 
        Função destinada pegar valores da planilha já inserido e retornar o valor digitado na busca
    '''
    colunas = data[0]
    valores = data[1:]
    df = pd.DataFrame(valores, columns=colunas)
    return df

def df_now(data:list):
    df = pd.DataFrame(data)
    return df

def Update_data_pag(sheet_id, client, name_pag, data):
    service = build('sheets', 'v4', credentials=client)
    
    sheet = service.spreadsheets() ## Pegou o arquivo inteiro 
    result = sheet.values().get(spreadsheetId=sheet_id, range=name_pag).execute()
    response = result.get('values', [])

    data = data['data']

    
    df1 = df_now(data)
    df2 = df_now(response)
    df = pd.concat([df2, df1], axis=0).fillna('')
    list_df = df.values.tolist()

    result = sheet.values().update(spreadsheetId=sheet_id, range=name_pag, valueInputOption='USER_ENTERED', body={"values":list_df}).execute()
    
    return result

## ---------------------------------------------------------------------------------------------------------------------------------------------- ##
##                                                          As rotas da api 


@app.get("/")
async def root():

    return {"data":"Hello "}

'''  
    Ler planilha com base em um range do usuario 
    Futuramente posso alterar os dados como eu bem queira
'''
@app.get("/readsheet/")
async def read_google_sheet(sheet_id: str, range_pag:str):
    
    # Conectar ao Google Sheets
    cred = api_key
    
    data = Read_Sheets(sheet_id, cred, range_pag)

    return {"data": data}

'''
    Pegar dados especifico do googlesheets 
    Ja fiz o tratamento se ele não existir no df.
'''
@app.get('/searchsheetpag')
async def searchsheetpag(sheet_id:str, name_pag:str, value: str):

    client = Conection()

    data = Search(sheet_id, client, name_pag, value)

    if (len(data) == 0 ):
        data = 'Valor não encontrado !!'  

    return {"data": data}

''' 
    Inserir de dados por em lote
'''

@app.post('/insertsheetspag')
async def insertsheetspag(sheet_id:str, name_pag:str, data:dict):

    client = Conection()    
    result = Insert_data_pag(sheet_id, client, name_pag, data)

    return {"data":result}


''' 
    Atualizar planilha pag
'''
@app.post('/updatesheetspag')
async def update_sheets(sheet_id:str, name_pag:str, data:dict):
    
    client = Conection()
    result = Update_data_pag(sheet_id, client, name_pag, data)
    
    return result


