"""В данном задании производится работа с файлом additional_task.py.
У вас есть таблица(переменная table), в которой вы передаете свои значения, и ответ из вебсокета бэкенда(переменная websocket_response).
Вам необходимо написать механизм, который принимает таблицу (table) и преобразовывает ее в запрос JSON.
Также известно, что ключи из таблицы равны значениям в base_ws и могут находиться в произвольном порядке.
В качестве конечного результата у вас должно полочуться содержимое переменной result в файле additional_task.py."""

import pandas as pd
import re


def convert_table_to_json(table_input, table):
    if table_input.endswith('.csv'):
        df = pd.read_csv(table_input)
    elif table_input.endswith('.xlsx') or table_input.endswith('.xls'):
        df = pd.read_excel(table_input)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    df.to_json(table)


table = convert_table_to_json('filename.csv', 'filename.json') 


def parse_conditions(condition_str):
    conditions = []
    if condition_str:
        for cond in condition_str.split(','):
            type_, value = cond.split('=')
            conditions.append({'type': type_, 'value': value})
    return conditions


def parse_highlights(highlight_str):
    highlights = []
    if highlight_str:
        parts = re.findall(r'([^,=]+)=(.*?)(?=(?:,[^,=]+=|$))', highlight_str)
        for part in parts:
            type_ = part[0]
            value = part[1]
            color = ''
            if '=' in value:
                value, color = value.split('=', 1)
            highlights.append({'type': type_, 'value': value, 'color': color})
    return highlights


result = {
    'columns': [],
    'order_by': {},
    'conditions_data': {},
    'page_size': '',
    'row_height': '',
    'color_conditions': {},
    'module': 'SO'
}

sort_index = 0
for entry in table:
    columns_view = entry['Columns View']
    if columns_view in websocket_response:
        index = websocket_response[columns_view]['index']

        # Columns field
        result['columns'].append({'index': index, 'sort': sort_index})
        sort_index += 1

        # Sort By field
        if entry['Sort By']:
            result['order_by'] = {'direction': entry['Sort By'], 'index': index}

        # Conditions field
        condition_key = websocket_response[columns_view]['filter']
        if entry['Condition']:
            result['conditions_data'][condition_key] = parse_conditions(entry['Condition'])

        # Highlight By (Color Conditions) field
        if entry['Highlight By']:
            result['color_conditions'][condition_key] = parse_highlights(entry['Highlight By'])
        else:
            result['color_conditions'][condition_key] = []

# Fields for row and page size
result['page_size'] = table[0]['Lines per page'] if table[0]['Lines per page'] else ''
result['row_height'] = table[0]['Row Height'] if table[0]['Row Height'] else ''

print(result)

