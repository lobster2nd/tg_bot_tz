import os

from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv


load_dotenv()

credentials_file = os.getenv('CREDENTIALS_FILE')
spreadsheet_id = os.getenv('SPREADSHEET_ID')


def get_cell_value(cell_range):
    """Возвращает значение заданной ячейки"""
    print(credentials_file)
    credentials = service_account.Credentials.from_service_account_file(
                            credentials_file,
                            scopes=['https://www.googleapis.com/auth/spreadsheets',
                                    'https://www.googleapis.com/auth/drive'])

    http_auth = credentials.with_scopes(
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
    )

    service = build('sheets', 'v4', credentials=http_auth)

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=cell_range,
        # majorDimension='COLUMNS'   указать в случае передачи диапазона
    ).execute()

    value = result.get('values', [[]])[0][0]
    return value
