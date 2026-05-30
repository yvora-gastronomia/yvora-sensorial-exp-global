import uuid
from datetime import datetime
from typing import Any, Dict

import pandas as pd
import streamlit as st

from google_access import get_workbook
from render_helpers import beverage_label, esc, header, language_selector, progress, story_blocks
from styles import inject_css
from ui_i18n import LANGUAGES, current_language, localized, safe, tr


APP_TITLE = "Experiência Tábua YVORA"
ACTIVE_VALUES = {"1", "sim", "ativo", "true", "yes", "publicado", "live"}

st.set_page_config(page_title=APP_TITLE, layout="wide", initial_sidebar_state="collapsed")


def active(value: Any) -> bool:
    return safe(value).lower() in ACTIVE_VALUES


@st.cache_data(ttl=120)
def read_sheet(tab: str) -> pd.DataFrame:
    try:
        return pd.DataFrame(get_workbook().worksheet(tab).get_all_records())
    except Exception as error:
        st.error(f"{tr('sheet_error')} '{tab}': {error}")
        return pd.DataFrame()


def write_row(tab: str, values: Dict[str, Any]) -> None:
    try:
        sheet = get_workbook().worksheet(tab)
        columns = sheet.row_values(1)
        sheet.append_row([values.get(column, "") for column in columns], value_input_option="USER_ENTERED")
    except Exception:
        pass


def valid_token(token: str) -> bool:
    data = read_sheet("tokens")
    if data.empty or "token" not in data.columns:
        return False
    selected = data[data["token"].astype(str).str.strip() == token.strip()]
    if selected.empty:
        return False
    return active(selected.iloc[0].get("status")) if "status" in selected.columns else True


def available_experiences() -> pd.DataFrame:
    data = read_sheet("experiencias")
    if data.empty:
        return data
    if "status" in data.columns:
        data = data[data["status"].apply(active)].copy()
    data["_sort"] = pd.to_numeric(data.get("ordem", 0), errors="coerce").fillna(9999)
    return data.sort_values("_sort")


def first_available_experience() -> Dict[str, Any]:
    data = available_experiences()
    if data.empty:
        return {}
    return data.iloc[0].to_dict()


def available_journeys(experience_id: str) -> pd.DataFrame:
    data = read_sheet("jornada")
    if data.empty:
        return data
    data = data[data["experience_id"].astype(str).str.strip() == experience_id].copy()
    if "ativo" in data.columns:
        data = data[data["ativo"].apply(active)]
    data["ordem"] = pd.to_numeric(data.get("ordem", 0), errors="coerce").fillna(0).astype(int)
    return data.sort_values("ordem").reset_index(drop=True)


def initialize() -> None:
    defaults = {
        "session_token": str(uuid.uuid4()),
        "language": "pt",
        "authenticated": False,
        "guest_name": "",
        "guest_phone": "",
        "guest_token": "",
        "selected_experience": None,
        "step_index": 0,
        "saved_answers": set(),
        "celebrated": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_login() -> None:
    language_selector()
    row = first_available_experience()
    title = localized(row, "nome_sessao", APP_TITLE)
    opening = localized(row, "texto_abertura", tr("intro"))
    start_label = localized(row, "botao_inicio", tr("start"))
    image = safe(row.get("imagem_capa_url"))
    background = f"background-image:url('{esc(image)}');" if image else "background-image:radial-gradient(circle at 70% 30%, rgba(198,169,106,.28), transparent 38%);"
    st.markdown(f'<section class="yv-cinema"><div class="yv-cinema-bg" style="{background}"></div><div class="yv-orb"></div><div class="yv-cinema-content"><div class="yv-kicker">{esc(tr("welcome"))}</div><div class="yv-h1">{esc(title)}</div><div class="yv-story">{esc(opening)}</div></div></section>', unsafe_allow_html=True)
    st.markdown('<div class="yv-card">', unsafe_allow_html=True)
    first, second, third = st.columns([1.2, 1, 0.7])
    with first:
        name = st.text_input(tr("name"), placeholder=tr("name_placeholder"))
    with second:
        phone = st.text_input(tr("phone"), placeholder=tr("phone_placeholder"))
    with third:
        token = st.text_input(tr("token"))
    if st.button(start_label, use_container_width=True):
        if not name.strip() or not phone.strip() or not token.strip():
            st.warning(tr("required"))
        elif valid_token(token):
            st.session_state.authenticated = True
            st.session_state.guest_name = name.strip()
            st.session_state.guest_phone = phone.strip()
            st.session_state.guest_token = token.strip()
            write_row("login_logs", {"created_at": datetime.now().isoformat(timespec="seconds"), "nome": name.strip(), "telefone": phone.strip(), "token": token.strip(), "status": "autorizado", "session_token": st.session_state.session_token, "idioma": current_language()})
            st.rerun()
        else:
            st.error(tr("invalid"))
    st.markdown("</div>", unsafe_allow_html=True)


def overview(experience_id: str) -> str:
    data = available_journeys(experience_id)
    if data.empty:
        return ""
    if "tipo_tela" in data.columns:
        visible = data[data["tipo_tela"].astype(str).str.strip().str.lower() == "jornada"]
        data = visible if not visible.empty else data
    cards = []
    for _, series in data.iterrows():
        row = series.to_dict()
        cards.append(f'<div class="yv-overview-card"><b>{esc(tr("journey"))} {esc(row.get("jornada_numero"))} - {esc(localized(row, "conceito_sensorial"))}</b><br>{esc(localized(row, "instrucao_cliente"))}</div>')
    return '<div class="yv-overview">' + "".join(cards) + "</div>"


def render_landing() -> None:
    language_selector()
    header(tr("welcome_guest").format(name=st.session_state.guest_name))
    data = available_experiences()
    if data.empty:
        st.info(tr("no_experience"))
        return
    for _, series in data.iterrows():
        row = series.to_dict()
        experience_id = safe(row.get("experience_id"))
        st.markdown(f'<div class="yv-card"><div class="yv-kicker">{esc(tr("available"))}</div><div class="yv-h2">{esc(localized(row, "nome_sessao", APP_TITLE))}</div><div class="yv-muted"><b>{esc(localized(row, "subtitulo"))}</b><br>{esc(localized(row, "descricao_card"))}</div>{overview(experience_id)}</div>', unsafe_allow_html=True)
        if st.button(localized(row, "botao_inicio", tr("start")), key="start_" + experience_id, use_container_width=True):
            st.session_state.selected_experience = experience_id
            st.session_state.step_index = 0
            st.session_state.celebrated = False
            st.rerun()


def render_journey(row: Dict[str, Any], position: int, total: int) -> None:
    st.markdown(progress(total, position), unsafe_allow_html=True)
    image = safe(row.get("imagem_url"))
    background = f"background-image:url('{esc(image)}');" if image else "background-image:radial-gradient(circle at 70% 30%, rgba(198,169,106,.28), transparent 38%);"
    blocks = "".join(f'<div class="yv-story-block"><div class="yv-story-block-title">{esc(title)}</div><div>{esc(body)}</div></div>' for title, body in story_blocks(localized(row, "texto_principal")))
    tiles = f'<div class="yv-steps"><div class="yv-step"><b>1. {esc(tr("meat"))}</b><br>{esc(localized(row, "carne"))}</div><div class="yv-step"><b>2. {esc(tr("cheese"))}</b><br>{esc(localized(row, "queijo"))}</div><div class="yv-step"><b>3. {esc(tr("together"))}</b><br>{esc(tr("together_note"))}</div><div class="yv-step"><b>4. {esc(beverage_label(row.get("experience_id")))}</b><br>{esc(localized(row, "vinho"))}</div></div>'
    section_html = f'<section class="yv-cinema"><div class="yv-cinema-bg" style="{background}"></div><div class="yv-orb"></div><div class="yv-cinema-content"><div class="yv-kicker">{esc(localized(row, "conceito_sensorial"))}</div><div class="yv-h1">{esc(localized(row, "titulo_tela"))}</div><div class="yv-story"><b>{esc(localized(row, "subtitulo_tela"))}</b></div><div class="yv-blocks">{blocks}</div>{tiles}<br><div class="yv-white-muted">{esc(localized(row, "instrucao_cliente"))}</div></div></section>'
    st.markdown(section_html, unsafe_allow_html=True)


def store_feedback(row: Dict[str, Any], answer: str, comment: str = "") -> None:
    if not answer and not comment:
        return
    marker = safe(row.get("etapa_id")) + answer + comment + current_language()
    if marker in st.session_state.saved_answers:
        return
    write_row("feedbacks", {"created_at": datetime.now().isoformat(timespec="seconds"), "experience_id": safe(row.get("experience_id")), "etapa_id": safe(row.get("etapa_id")), "jornada_numero": safe(row.get("jornada_numero")), "nome_jornada": localized(row, "titulo_tela"), "tipo_tela": safe(row.get("tipo_tela")), "session_token": st.session_state.session_token, "nome": st.session_state.guest_name, "telefone": st.session_state.guest_phone, "token": st.session_state.guest_token, "resposta": answer, "comentario_final": comment, "idioma": current_language()})
    st.session_state.saved_answers.add(marker)


def render_completed() -> None:
    header(tr("completed"))
    st.markdown(f'<section class="yv-cinema"><div class="yv-cinema-content yv-celebration"><div class="yv-kicker">YVORA</div><div class="yv-h1">{esc(tr("completed"))}</div><div class="yv-story">{esc(tr("thanks"))}</div><br><div class="yv-white-muted">{esc(tr("closing"))}</div></div></section>', unsafe_allow_html=True)
    if st.button(tr("home"), use_container_width=True):
        st.session_state.selected_experience = None
        st.session_state.step_index = 0
        st.session_state.celebrated = False
        st.rerun()


def render_experience(experience_id: str) -> None:
    language_selector()
    if st.session_state.celebrated:
        render_completed()
        return
    data = available_journeys(experience_id)
    if data.empty:
        st.warning(tr("not_found"))
        return
    position = min(st.session_state.step_index, len(data) - 1)
    row = data.iloc[position].to_dict()
    header(tr("ritual"))
    render_journey(row, position, len(data))
    answer = st.radio(tr("feedback"), ["👍", "👎"], horizontal=True, index=None, key="answer_" + safe(row.get("etapa_id")))
    back, forward, home = st.columns(3)
    with back:
        if position > 0 and st.button(tr("back"), use_container_width=True):
            st.session_state.step_index -= 1
            st.rerun()
    with forward:
        if st.button(localized(row, "botao_texto", tr("next")), use_container_width=True):
            store_feedback(row, safe(answer))
            if position >= len(data) - 1:
                st.session_state.celebrated = True
            else:
                st.session_state.step_index += 1
            st.rerun()
    with home:
        if st.button(tr("home"), use_container_width=True):
            st.session_state.selected_experience = None
            st.session_state.step_index = 0
            st.rerun()


initialize()
inject_css()
parameters = st.query_params
if safe(parameters.get("lang")) in LANGUAGES:
    st.session_state.language = safe(parameters.get("lang"))
if not st.session_state.authenticated:
    render_login()
elif st.session_state.selected_experience:
    render_experience(st.session_state.selected_experience)
else:
    render_landing()
