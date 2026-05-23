from typing import Any, Dict
import pandas as pd
import streamlit as st

LANGUAGES = {"pt": "Português", "en": "English", "zh": "中文"}

UI_TEXT = {
    "pt": {
        "app_title": "Experiência Tábua YVORA",
        "language": "Idioma",
        "welcome": "WELCOME TO YVORA",
        "intro": "Você foi convidado para uma experiência criada para revelar sabores que normalmente passam despercebidos.",
        "identify": "Antes de iniciar, identifique-se para liberar sua jornada.",
        "name": "Nome",
        "name_placeholder": "Seu nome",
        "phone": "Telefone",
        "phone_placeholder": "DDD + telefone",
        "token": "Token",
        "start": "Vamos iniciar",
        "required": "Preencha nome, telefone e token para iniciar.",
        "invalid": "Token inválido ou inativo.",
        "sheet_error": "Não foi possível ler a aba",
        "welcome_guest": "Bem-vindo, {name}. Escolha a sessão para iniciar.",
        "no_experience": "Nenhuma experiência disponível.",
        "available": "Experiência disponível",
        "journey": "Jornada",
        "ritual": "Siga o ritual. Prove, combine e deixe a bebida transformar.",
        "not_found": "Experiência não encontrada ou sem etapas ativas.",
        "meat": "Carne",
        "cheese": "Queijo",
        "together": "Juntos",
        "together_note": "Prove a dupla na ordem indicada.",
        "wine": "Vinho",
        "drink": "Bebida",
        "feedback": "A jornada funcionou para você?",
        "feedback_selected": "Feedback selecionado",
        "highlight": "Qual jornada mais marcou sua experiência?",
        "comment": "Comentário opcional",
        "comment_placeholder": "Conte o que mais chamou sua atenção",
        "next": "Avançar",
        "back": "Retornar",
        "home": "Voltar ao início",
        "completed": "Degustação concluída",
        "thanks": "Obrigado por viver esta experiência. Você participou de uma leitura guiada de sabor criada para revelar como a culinária brasileira contemporânea pode ganhar novas camadas quando encontra técnica, bebida e percepção.",
        "closing": "Sua jornada ajuda a construir a inteligência sensorial da YVORA.",
        "labels": ["ELEMENTO", "ABERTURA", "BRASILIDADE", "PERCEPÇÃO GUIADA", "ENCONTRO", "VINHO", "BEBIDA", "O QUE ESTA JORNADA REVELA", "AGORA É COM VOCÊ", "CELEBRAÇÃO", "EXPERIÊNCIA", "CONCLUSÃO"],
        "fallback_block": "RITUAL",
    },
    "en": {
        "app_title": "YVORA Board Experience",
        "language": "Language",
        "welcome": "WELCOME TO YVORA",
        "intro": "You have been invited to an experience created to reveal flavours that normally go unnoticed.",
        "identify": "Before you begin, please identify yourself to unlock your journey.",
        "name": "Name",
        "name_placeholder": "Your name",
        "phone": "Phone",
        "phone_placeholder": "Area code + number",
        "token": "Access code",
        "start": "Begin the experience",
        "required": "Enter your name, phone number and access code to begin.",
        "invalid": "Invalid or inactive access code.",
        "sheet_error": "Could not read worksheet",
        "welcome_guest": "Welcome, {name}. Choose your experience to begin.",
        "no_experience": "No experience is currently available.",
        "available": "Available experience",
        "journey": "Journey",
        "ritual": "Follow the ritual. Taste, combine and let the drink transform the experience.",
        "not_found": "Experience not found or without active journeys.",
        "meat": "Meat",
        "cheese": "Cheese",
        "together": "Together",
        "together_note": "Taste the pair in the indicated order.",
        "wine": "Wine",
        "drink": "Drink",
        "feedback": "Did this journey work for you?",
        "feedback_selected": "Selected feedback",
        "highlight": "Which journey most marked your experience?",
        "comment": "Optional comment",
        "comment_placeholder": "Tell us what most caught your attention",
        "next": "Continue",
        "back": "Back",
        "home": "Return to start",
        "completed": "Tasting completed",
        "thanks": "Thank you for living this experience. You took part in a guided reading of flavour designed to reveal how contemporary Brazilian cuisine gains new layers when technique, drink and perception meet.",
        "closing": "Your journey helps build YVORA's sensory intelligence.",
        "labels": ["ELEMENT", "OPENING", "BRAZILIAN IDENTITY", "GUIDED TASTING", "ENCOUNTER", "WINE", "DRINK", "WHAT THIS JOURNEY REVEALS", "NOW IT IS YOUR TURN", "CELEBRATION", "EXPERIENCE", "CONCLUSION"],
        "fallback_block": "RITUAL",
    },
    "zh": {
        "app_title": "YVORA 风味体验拼盘",
        "language": "语言",
        "welcome": "欢迎来到 YVORA",
        "intro": "欢迎体验一场旨在揭示平时容易被忽略之风味变化的品鉴旅程。",
        "identify": "开始之前，请填写信息以进入您的品鉴旅程。",
        "name": "姓名",
        "name_placeholder": "您的姓名",
        "phone": "电话",
        "phone_placeholder": "区号 + 电话号码",
        "token": "访问码",
        "start": "开始体验",
        "required": "请输入姓名、电话号码和访问码以开始体验。",
        "invalid": "访问码无效或已停用。",
        "sheet_error": "无法读取工作表",
        "welcome_guest": "欢迎您，{name}。请选择要开始的品鉴体验。",
        "no_experience": "当前没有可用体验。",
        "available": "可用体验",
        "journey": "体验",
        "ritual": "跟随引导，品尝、组合，并感受饮品带来的变化。",
        "not_found": "找不到体验或没有启用中的品鉴阶段。",
        "meat": "肉类",
        "cheese": "奶酪",
        "together": "组合",
        "together_note": "按照引导顺序品尝组合。",
        "wine": "葡萄酒",
        "drink": "饮品",
        "feedback": "您是否感受到了这段体验？",
        "feedback_selected": "已选择反馈",
        "highlight": "哪一段体验给您留下最深印象？",
        "comment": "选填评论",
        "comment_placeholder": "请分享最吸引您注意的感受",
        "next": "继续",
        "back": "返回",
        "home": "返回首页",
        "completed": "品鉴完成",
        "thanks": "感谢您体验这场品鉴旅程。您参与了一次引导式风味感知，探索当技法、饮品与感知相遇时，巴西当代料理如何呈现新的层次。",
        "closing": "您的体验将帮助 YVORA 建立更丰富的感官洞察。",
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
