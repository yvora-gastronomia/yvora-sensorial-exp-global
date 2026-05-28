import streamlit as st


LANGUAGES = {
    "pt": "Português",
    "en": "English",
    "zh": "中文",
    "ja": "日本語",
    "es": "Español",
}


BASE_TRANSLATIONS = {
    "pt": {
        "welcome": "WELCOME",
        "intro": "Experiência sensorial",
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
    },
    "en": {
        "welcome": "WELCOME",
        "intro": "Sensory experience",
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
        "closing": "Now continue exploring your own favourite combinations.",
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
    },
    "zh": {
        "welcome": "WELCOME",
        "intro": "感官体验",
        "start": "进入体验",
        "name": "姓名",
        "name_placeholder": "请输入姓名",
        "phone": "电话",
        "phone_placeholder": "请输入电话",
        "token": "令牌",
        "required": "请填写所有字段。",
        "invalid": "令牌无效。",
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
        "feedback": "您觉得这一段如何？",
        "back": "返回",
        "next": "继续",
        "not_found": "未找到体验。",
        "meat": "肉类",
        "cheese": "奶酪",
        "together": "组合",
        "together_note": "一起品尝这些元素",
    },
    "ja": {
        "welcome": "WELCOME",
        "intro": "感覚体験",
        "start": "体験を始める",
        "name": "お名前",
        "name_placeholder": "お名前を入力してください",
        "phone": "電話番号",
        "phone_placeholder": "電話番号を入力してください",
        "token": "トークン",
        "required": "すべての項目を入力してください。",
        "invalid": "無効なトークンです。",
        "sheet_error": "シートアクセスエラー",
        "welcome_guest": "{name} さん、ようこそ",
        "available": "利用可能な体験",
        "journey": "旅",
        "no_experience": "利用可能な体験がありません。",
        "completed": "テイスティング完了",
        "thanks": "YVORA体験をご利用いただきありがとうございます。",
        "closing": "これからは自由にお好みの組み合わせを探してください。",
        "home": "最初に戻る",
        "ritual": "感覚の儀式",
        "feedback": "この旅はいかがでしたか？",
        "back": "戻る",
        "next": "続ける",
        "not_found": "体験が見つかりません。",
        "meat": "肉",
        "cheese": "チーズ",
        "together": "組み合わせ",
        "together_note": "要素を一緒に試してください",
    },
    "es": {
        "welcome": "WELCOME",
        "intro": "Experiencia sensorial",
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
    },
}


def safe(value):
    if value is None:
        return ""
    return str(value).strip()


def current_language():
    return st.session_state.get("language", "pt")


def tr(key):
    lang = current_language()

    return (
        BASE_TRANSLATIONS.get(lang, {}).get(key)
        or BASE_TRANSLATIONS["pt"].get(key)
        or key
    )


def localized(row, field, fallback=""):
    lang = current_language()

    if lang == "pt":
        return safe(row.get(field, fallback))

    localized_field = f"{field}_{lang}"

    return safe(
        row.get(localized_field)
        or row.get(field)
        or fallback
    )
