### Integração com o google Sheets

* API destinada para insert no googlesheets
* Comandos para rodar localmente
    uvicorn main:app --reload

* Dependencias :
    * uvicorn
    * FastAPI
    * google-api-python-client google-auth-httplib2 google-auth-oauthlib

* git clone 
- clone https://github.com/renan-lemes/ApiSheets
- cd app

* Crie o ambiente conda
- conda create -n api_env python=3.9.12 -y
- conda activate api_env
- pip install -r requirements.txt

* Variáveis de ambiente
- API_KEY=SUA_CHAVE_DE_API_AQUI

* Ativar o ambiente 
- uvicorn api.main:app --reload

* Execute o servidor FastAPI com o Uvicorn:
- conda activate api_env
- uvicorn api.main:app --reload