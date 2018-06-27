
from apiclient.discovery import build
from oauth2client import file, client, tools
from httplib2 import Http

def authenticate_gdrive():
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('config/credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('config/client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    return service

if __name__ == '__main__':
    authenticate_gdrive()
