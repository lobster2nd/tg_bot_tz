import os
import re
from datetime import datetime

from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv


load_dotenv()

credentials_file = os.getenv('CREDENTIALS_FILE')
spreadsheet_id = os.getenv('SPREADSHEET_ID')

credentials = service_account.Credentials.from_service_account_file(
                        credentials_file,
                        scopes=['https://www.googleapis.com/auth/spreadsheets',
                                'https://www.googleapis.com/auth/drive'])

http_auth = credentials.with_scopes(
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)

service = build('sheets', 'v4', credentials=http_auth)


def get_first_empty_cell():
    """Возвращает первую свободную ячейку в столбце В"""

    range_name = 'B:B'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                 range=range_name).execute()
    values = result.get('values', [])

    for i, row in enumerate(values):
        if not row:
            first_empty_cell = i + 1
            print(f'Первая пустая ячейка в столбце B: {first_empty_cell}')
            return first_empty_cell
    return len(values) + 1


def validate_date(date_str):
    """Проверка корректности введённой даты"""

    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def get_cell_value(cell_range):
    """Возвращает значение заданной ячейки"""

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=cell_range,
        # majorDimension='COLUMNS'   указать в случае передачи диапазона
    ).execute()

    value = result.get('values', [[]])[0][0]
    return value


def write_cell_value(usr_input):
    """Записывает введённую пользователем дату в свободную ячейку В"""

    if not validate_date(usr_input):
        return 'Дата введена некорректно. Введите дату в формате DD.MM.YYYY'
    else:
        cell = 'B' + str(get_first_empty_cell())
        value = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": cell,
                     "values": [[usr_input]]},
                ]
            }
        ).execute()
        return f'В ячейку {cell} внесено значение {get_cell_value(cell)}'

