import json
import gspread
import streamlit as st
from google.oauth2.service_account import Credentials
from sheet_config import DEFAULT_SHEET_ID


@st.cache_resource(ttl=600)
def get_workbook():
    google = st.secrets.get("google", {})
    if google.get("service_account_json"):
        account = json.loads(google["service_account_json"])
    elif "gcp_service_account" in st.secrets:
        account = dict(st.secrets["gcp_service_account"])
    else:
        st.error("Configure as credenciais do Google Sheets nos secrets do Streamlit.")
        st.stop()
    creds = Credentials.from_service_account_info(
        account,
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    sheet_id = google.get("sheet_id") or st.secrets.get("SPREADSHEET_ID") or DEFAULT_SHEET_ID
    return gspread.authorize(creds).open_by_key(sheet_id)
