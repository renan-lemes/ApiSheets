# Integração com Google Sheets

Este projeto fornece uma API REST para inserir e ler dados de planilhas no Google Sheets usando FastAPI e Uvicorn.

---

## 📦 Clonando o repositório

```bash
git clone https://github.com/renan-lemes/ApiSheets.git
cd ApiSheets
```

## 🛠️ Dependências

Lista de pacotes no `requirements.txt`:

* fastapi
* uvicorn
* google-api-python-client
* google-auth-httplib2
* google-auth-oauthlib
* python-dotenv

Instale todas as dependências:

```bash
pip install -r requirements.txt
```

---

## 🐍 Ambiente Conda

1. Crie e ative o ambiente:

   ```bash
   conda create -n api_env python=3.9.12 -y
   conda activate api_env
   ```
2. Instale as dependências (se ainda não fez):

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Variáveis de Ambiente

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione sua chave de API do Google Sheets:

   ```dotenv
   API_KEY=SUA_CHAVE_DE_API_AQUI
   ```

> **Observação:** Para acesso a planilhas privadas, utilize OAuth ou conta de serviço e adicione o respectivo arquivo de credenciais.

---

## 🚀 Executando a API

Com o ambiente ativo, inicie o servidor:

```bash
conda activate api_env      # caso ainda não esteja ativo
uvicorn api.main:app --reload
```

* A API estará disponível em: `http://127.0.0.1:8000`
* Documentação interativa (Swagger): `http://127.0.0.1:8000/docs`

---

## 📑 Endpoints Principais

* **GET /readsheet**: lê a planilha
* **POST /insertsheetspag**: inserir info na pagina
* **GET /searchsheetpag** pega a informação na pagina da planilha

Veja detalhes em `api/routers/`.

---

## 🤝 Contribuição

1. Crie um branch: `git checkout -b feature/nome-da-feature`
2. Commit suas alterações: `git commit -m "Descrição da mudança"`
3. Push para o repositório: `git push origin feature/nome-da-feature`
4. Abra um Pull Request.

---

## 📄 Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo `LICENSE` para mais informações.
