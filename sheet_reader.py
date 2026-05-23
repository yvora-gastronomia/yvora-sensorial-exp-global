import pandas as pd
import streamlit as st
from ui_i18n import safe


def active(value):
    return safe(value).lower() in ['1', 'sim', 'ativo', 'true', 'yes', 'publicado', 'live']


@st.cache_data(ttl=180)
def records(workbook, tab):
    try:
        return pd.DataFrame(workbook.worksheet(tab).get_all_records())
    except Exception as error:
        st.error('Erro ao carregar ' + tab + ': ' + str(error))
        return pd.DataFrame()


def append(workbook, tab, values):
    worksheet = workbook.worksheet(tab)
    headers = worksheet.row_values(1)
    worksheet.append_row([values.get(header, '') for header in headers], value_input_option='USER_ENTERED')


def valid_token(workbook, token):
    data = records(workbook, 'tokens')
    if data.empty or 'token' not in data.columns:
        return False
    data['token'] = data['token'].astype(str).str.strip()
    matched = data[data['token'] == token.strip()]
    if matched.empty:
        return False
    return active(matched.iloc[0].get('status')) if 'status' in matched.columns else True


def experiences(workbook):
    data = records(workbook, 'experiencias')
    if data.empty:
        return data
    if 'status' in data.columns:
        data = data[data['status'].apply(active)].copy()
    data['_ordem'] = pd.to_numeric(data.get('ordem', 0), errors='coerce').fillna(9999)
    return data.sort_values('_ordem')


def steps(workbook, experience_id):
    data = records(workbook, 'jornada')
    if data.empty:
        return data
    data['experience_id'] = data['experience_id'].astype(str).str.strip()
    data = data[data['experience_id'] == experience_id].copy()
    if 'ativo' in data.columns:
        data = data[data['ativo'].apply(active)]
    data['ordem'] = pd.to_numeric(data.get('ordem', 0), errors='coerce').fillna(0).astype(int)
    return data.sort_values('ordem').reset_index(drop=True)
