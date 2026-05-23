import os
import re
from html import escape
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st

from ui_i18n import LANGUAGES, UI_TEXT, current_language, localized, safe, tr

LOGO_PATHS = [
    "yvora_logo.JPG", "yvora_logo.jpg", "yvora_logo.jpeg", "yvora_logo.png",
    "logo.png", "logo.jpg", "assets/yvora_logo.png", "assets/yvora_logo.jpg",
]


def esc(value: Any) -> str:
    return escape(safe(value))


def split_options(value: Any) -> List[str]:
    text = safe(value)
    return [item.strip() for item in text.split(";") if item.strip()] if text else []


def logo_path() -> Optional[str]:
    for path in LOGO_PATHS:
        if os.path.exists(path):
            return path
    return None


def story_blocks(text: str) -> List[Tuple[str, str]]:
    config = UI_TEXT[current_language()]
    labels = config["labels"]
    pattern = r"(" + "|".join(re.escape(label) for label in labels) + r")\s*\|"
    parts = re.split(pattern, safe(text))
    if len(parts) <= 1:
        return [(config["fallback_block"], safe(text))]
    blocks: List[Tuple[str, str]] = []
    if parts[0].strip():
        blocks.append((config["fallback_block"], parts[0].strip()))
    for index in range(1, len(parts), 2):
        body = parts[index + 1].strip() if index + 1 < len(parts) else ""
        if body:
            blocks.append((parts[index].strip(), body))
    return blocks


def language_selector() -> None:
    options = list(LANGUAGES.keys())
    selected = st.radio(
        tr("language"), options, horizontal=True,
        index=options.index(current_language()),
        format_func=lambda value: LANGUAGES[value], key="language_widget",
    )
    if selected != current_language():
        st.session_state.language = selected
        st.rerun()


def header(subtitle: str = "") -> None:
    left, right = st.columns([1, 8])
    with left:
        path = logo_path()
        if path:
            st.image(path, width=78)
        else:
            st.markdown('<div class="yv-logo-mark">Y</div>', unsafe_allow_html=True)
    with right:
        st.markdown(
            f'<h1 class="yv-title">{esc(tr("app_title"))}</h1><div class="yv-subtitle">{esc(subtitle)}</div>',
            unsafe_allow_html=True,
        )


def progress(total: int, current: int) -> str:
    dots = ['<div class="yv-dot yv-dot-on"></div>' if index <= current else '<div class="yv-dot"></div>' for index in range(total)]
    return '<div class="yv-progress">' + "".join(dots) + "</div>"


def beverage_label(experience_id: Any) -> str:
    text = safe(experience_id).lower()
    return tr("drink") if "kombucha" in text or "sem alcool" in text or "sem álcool" in text else tr("wine")


def localized_story(row: Dict[str, Any]) -> str:
    return localized(row, "texto_principal")
