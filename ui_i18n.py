from typing import Any, Dict

import streamlit as st


LANGUAGES = {
    "pt": "Português",
    "en": "English",
    "zh": "中文",
    "ja": "日本語",
    "es": "Español",
}


UI_TEXT: Dict[str, Dict[str, str]] = {
    "pt": {
        "welcome": "BEM-VINDO",
        "intro": "Experiência sensorial",
        "app_title": "Experiência Tábua YVORA",
        "identify": "Identifique-se para iniciar a experiência",
        "start": "Entrar na experiência",
        "name": "Nome",
        "name_placeholder": "Digite seu nome",
        "phone": "Telefone",
        "phone_placeholder": "Digite seu telefone",
        "token": "Token",
        "required": "Preencha todos os campos.",
        "invalid": "Token inválido.",
        "sheet_error": "Erro ao acessar a planilha",
        "welcome_guest": "Bem-vindo, {name}",
        "available": "Experiência disponível",
        "journey": "Jornada",
        "no_experience": "Nenhuma experiência disponível.",
        "completed": "Degustação concluída",
        "thanks": "Obrigado por explorar a experiência YVORA.",
        "closing": "Agora continue explorando livremente suas combinações preferidas.",
        "home": "Voltar ao início",
        "ritual": "Ritual Sensorial",
        "feedback": "Como foi essa jornada?",
        "back": "Voltar",
        "next": "Continuar",
        "not_found": "Experiência não encontrada.",
        "meat": "Carne",
        "cheese": "Queijo",
        "together": "Combinação",
        "together_note": "Experimente os elementos juntos",
        "wine": "Vinho",
        "drink": "Bebida",
        "language": "Idioma",
    },
    "en": {
        "welcome": "WELCOME",
        "intro": "Sensory experience",
        "app_title": "YVORA Board Experience",
        "identify": "Identify yourself to start the experience",
        "start": "Enter the experience",
        "name": "Name",
        "name_placeholder": "Enter your name",
        "phone": "Phone",
        "phone_placeholder": "Enter your phone",
        "token": "Token",
        "required": "Please complete all fields.",
        "invalid": "Invalid token.",
        "sheet_error": "Spreadsheet access error",
        "welcome_guest": "Welcome, {name}",
        "available": "Available experience",
        "journey": "Journey",
        "no_experience": "No experiences available.",
        "completed": "Tasting completed",
        "thanks": "Thank you for exploring the YVORA experience.",
        "closing": "Now continue exploring your favourite combinations.",
        "home": "Back to home",
        "ritual": "Sensory Ritual",
        "feedback": "How was this journey?",
        "back": "Back",
        "next": "Continue",
        "not_found": "Experience not found.",
        "meat": "Meat",
        "cheese": "Cheese",
        "together": "Combination",
        "together_note": "Try the elements together",
        "wine": "Wine",
        "drink": "Drink",
        "language": "Language",
    },
    "zh": {
        "welcome": "欢迎",
        "intro": "感官体验",
        "app_title": "YVORA 风味体验拼盘",
        "identify": "请填写信息以开始体验",
        "start": "进入体验",
        "name": "姓名",
        "name_placeholder": "请输入姓名",
        "phone": "电话",
        "phone_placeholder": "请输入电话",
        "token": "口令",
        "required": "请填写所有字段。",
        "invalid": "口令无效。",
        "sheet_error": "表格访问错误",
        "welcome_guest": "欢迎，{name}",
        "available": "可用体验",
        "journey": "旅程",
        "no_experience": "暂无可用体验。",
        "completed": "品鉴完成",
        "thanks": "感谢您体验 YVORA。",
        "closing": "现在请自由探索您最喜欢的组合。",
        "home": "返回首页",
        "ritual": "感官仪式",
        "feedback": "您觉得这一段体验如何？",
        "back": "返回",
        "next": "继续",
        "not_found": "未找到体验。",
        "meat": "肉类",
        "cheese": "奶酪",
        "together": "组合",
        "together_note": "一起品尝这些元素",
        "wine": "葡萄酒",
        "drink": "饮品",
        "language": "语言",
    },
    "ja": {
        "welcome": "ようこそ",
        "intro": "感覚体験",
        "app_title": "YVORA テイスティングボード体験",
        "identify": "体験を始めるために情報を入力してください",
        "start": "体験を始める",
        "name": "お名前",
        "name_placeholder": "お名前を入力してください",
        "phone": "電話番号",
        "phone_placeholder": "電話番号を入力してください",
        "token": "トークン",
        "required": "すべての項目を入力してください。",
        "invalid": "無効なトークンです。",
        "sheet_error": "シートへのアクセスエラー",
        "welcome_guest": "{name} さん、ようこそ",
        "available": "利用可能な体験",
        "journey": "旅",
        "no_experience": "利用可能な体験がありません。",
        "completed": "テイスティング完了",
        "thanks": "YVORA体験をお楽しみいただき、ありがとうございます。",
        "closing": "ここからは、お好みの組み合わせを自由に探してください。",
        "home": "最初に戻る",
        "ritual": "感覚の儀式",
        "feedback": "この旅はいかがでしたか？",
        "back": "戻る",
        "next": "続ける",
        "not_found": "体験が見つかりません。",
        "meat": "肉",
        "cheese": "チーズ",
        "together": "組み合わせ",
        "together_note": "要素を一緒に味わってください",
        "wine": "ワイン",
        "drink": "飲み物",
        "language": "言語",
    },
    "es": {
        "welcome": "BIENVENIDO",
        "intro": "Experiencia sensorial",
        "app_title": "Experiencia Tabla YVORA",
        "identify": "Identifíquese para iniciar la experiencia",
        "start": "Entrar en la experiencia",
        "name": "Nombre",
        "name_placeholder": "Ingrese su nombre",
        "phone": "Teléfono",
        "phone_placeholder": "Ingrese su teléfono",
        "token": "Token",
        "required": "Complete todos los campos.",
        "invalid": "Token inválido.",
        "sheet_error": "Error al acceder a la hoja",
        "welcome_guest": "Bienvenido, {name}",
        "available": "Experiencia disponible",
        "journey": "Recorrido",
        "no_experience": "No hay experiencias disponibles.",
        "completed": "Degustación concluida",
        "thanks": "Gracias por explorar la experiencia YVORA.",
        "closing": "Ahora continúe explorando libremente sus combinaciones preferidas.",
        "home": "Volver al inicio",
        "ritual": "Ritual Sensorial",
        "feedback": "¿Cómo fue este recorrido?",
        "back": "Volver",
        "next": "Continuar",
        "not_found": "Experiencia no encontrada.",
        "meat": "Carne",
        "cheese": "Queso",
        "together": "Combinación",
        "together_note": "Pruebe los elementos juntos",
        "wine": "Vino",
        "drink": "Bebida",
        "language": "Idioma",
    },
}


def safe(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def current_language() -> str:
    language = safe(st.session_state.get("language", "pt"))
    return language if language in LANGUAGES else "pt"


def tr(key: str) -> str:
    language = current_language()
    return UI_TEXT.get(language, {}).get(key) or UI_TEXT["pt"].get(key) or key


def localized(row: Dict[str, Any], field: str, fallback: str = "") -> str:
    language = current_language()

    if language == "pt":
        return safe(row.get(field) or fallback)

    translated_field = f"{field}_{language}"

    return safe(
        row.get(translated_field)
        or row.get(field)
        or fallback
    )
