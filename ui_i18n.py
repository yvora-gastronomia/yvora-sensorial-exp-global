from typing import Any, Dict
import pandas as pd
import streamlit as st

LANGUAGES = {"pt": "Português", "en": "English", "zh": "中文"}

UI_TEXT = {
    "pt": {
        "language": "Idioma",
        "name": "Nome",
        "name_placeholder": "Seu nome",
        "phone": "Telefone",
        "phone_placeholder": "DDD + telefone",
        "token": "Token",
        "required": "Preencha nome, telefone e token para iniciar.",
        "invalid": "Token inválido ou inativo.",
        "sheet_error": "Não foi possível ler a aba",
        "journey": "Jornada",
        "meat": "Carne",
        "cheese": "Queijo",
        "together": "Juntos",
        "together_note": "Prove a dupla na ordem indicada.",
        "wine": "Vinho",
        "drink": "Bebida",
        "feedback": "A jornada funcionou para você?",
        "feedback_selected": "Feedback selecionado",
        "next": "Avançar",
        "back": "Retornar",
        "home": "Voltar ao início",
        "labels": ["ELEMENTO", "ABERTURA", "BRASILIDADE", "PERCEPÇÃO GUIADA", "ENCONTRO", "VINHO", "BEBIDA", "O QUE ESTA JORNADA REVELA", "AGORA É COM VOCÊ", "CELEBRAÇÃO", "EXPERIÊNCIA", "CONCLUSÃO"],
        "fallback_block": "RITUAL",
    },
    "en": {
        "language": "Language",
        "name": "Name",
        "name_placeholder": "Your name",
        "phone": "Phone",
        "phone_placeholder": "Area code + number",
        "token": "Access code",
        "required": "Enter your name, phone number and access code to begin.",
        "invalid": "Invalid or inactive access code.",
        "sheet_error": "Could not read worksheet",
        "journey": "Journey",
        "meat": "Meat",
        "cheese": "Cheese",
        "together": "Together",
        "together_note": "Taste the pair in the indicated order.",
        "wine": "Wine",
        "drink": "Drink",
        "feedback": "Did this journey work for you?",
        "feedback_selected": "Selected feedback",
        "next": "Continue",
        "back": "Back",
        "home": "Return to start",
        "labels": ["ELEMENT", "OPENING", "BRAZILIAN IDENTITY", "GUIDED TASTING", "ENCOUNTER", "WINE", "DRINK", "WHAT THIS JOURNEY REVEALS", "NOW IT IS YOUR TURN", "CELEBRATION", "EXPERIENCE", "CONCLUSION"],
        "fallback_block": "RITUAL",
    },
    "zh": {
        "language": "语言",
        "name": "姓名",
        "name_placeholder": "您的姓名",
        "phone": "电话",
        "phone_placeholder": "区号 + 电话号码",
        "token": "访问码",
        "required": "请输入姓名、电话号码和访问码以开始体验。",
        "invalid": "访问码无效或已停用。",
        "sheet_error": "无法读取工作表",
        "journey": "体验",
        "meat": "肉类",
        "cheese": "奶酪",
        "together": "组合",
        "together_note": "按照引导顺序品尝组合。",
        "wine": "葡萄酒",
        "drink": "饮品",
        "feedback": "您是否感受到了这段体验？",
        "feedback_selected": "已选择反馈",
        "next": "继续",
        "back": "返回",
        "home": "返回首页",
        "labels": ["元素", "开场", "巴西特色", "引导品尝", "相遇", "葡萄酒", "饮品", "体验揭示", "现在由您创造", "庆祝", "体验", "结论"],
        "fallback_block": "体验引导",
    },
}


def safe(value: Any, default: str = "") -> str:
    if value is None:
        return default
    try:
        if pd.isna(value):
            return default
    except Exception:
        pass
    text = str(value).strip()
    return text if text else default


def current_language() -> str:
    value = safe(st.session_state.get("language"), "pt")
    return value if value in LANGUAGES else "pt"


def tr(key: str) -> str:
    return UI_TEXT[current_language()].get(key, UI_TEXT["pt"].get(key, key))


def localized(row: Dict[str, Any], field: str, default: str = "") -> str:
    language = current_language()
    if language != "pt":
        translated = safe(row.get(f"{field}_{language}"))
        if translated:
            return translated
    return safe(row.get(field), default)
