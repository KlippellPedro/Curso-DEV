# Importa as credenciais do Google
from google.oauth2.credentials import Credentials
# Fluxo OAuth
from google_auth_oauthlib.flow import InstalledAppFlow
# Requisição
from google.auth.transport.requests import Request
# API Gmail
from googleapiclient.discovery import build
# Codificação
import base64
# Email
from email.mime.text import MIMEText
# Arquivo
import os.path

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

class GmailService:
    @staticmethod
    def autenticar():
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        return creds
    
    @staticmethod
    def enviar_email(destinatario, assunto, mensagem):
        creds = GmailService.autenticar()
        service = build('gmail', 'v1', credentials=creds)
        
        msg = MIMEText(mensagem, 'html')
        msg['to'] = destinatario
        msg['subject']= assunto
        
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        body= {'raw': raw}
        service.users().messages().send(userId='me', body=body).execute()