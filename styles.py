import streamlit as st

BRAND_BG = "#EFE7DD"
BRAND_BG_SOFT = "#FAF6EF"
BRAND_BLUE = "#0E2A47"
BRAND_GOLD = "#C6A96A"
BRAND_TEXT = "#47372E"


def inject_css() -> None:
    st.markdown(
        f"""
<style>
[data-testid="stSidebar"],
[data-testid="collapsedControl"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu,
header,
footer,
.stDeployButton {{
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
}}
html, body, [data-testid="stAppViewContainer"] {{
    background:
        radial-gradient(circle at 12% 8%, rgba(198,169,106,0.20), transparent 30%),
        radial-gradient(circle at 92% 18%, rgba(14,42,71,0.10), transparent 34%),
        linear-gradient(135deg, {BRAND_BG_SOFT} 0%, {BRAND_BG} 100%) !important;
    color: {BRAND_TEXT};
    scroll-behavior: smooth;
}}
.block-container {{ padding-top: 1.05rem; padding-bottom: 2rem; max-width: 1180px; }}
.yv-logo-mark {{ width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: {BRAND_BLUE}; color: {BRAND_BG_SOFT}; font-family: Georgia, serif; font-size: 24px; letter-spacing: 1px; }}
.yv-title {{ margin: 0; color: {BRAND_BLUE}; font-family: Georgia, 'Times New Roman', serif; font-size: clamp(30px, 4.5vw, 48px); line-height: 1.05; letter-spacing: .2px; }}
.yv-subtitle {{ margin-top: 7px; color: rgba(14,42,71,.70); font-size: clamp(16px, 2.8vw, 19px); line-height: 1.45; }}
.yv-card {{ background: rgba(255,255,255,.72); border: 1px solid rgba(14,42,71,.12); border-radius: 30px; padding: clamp(22px, 4vw, 40px); box-shadow: 0 18px 50px rgba(14,42,71,.08); margin-bottom: 18px; }}
.yv-kicker {{ color: {BRAND_GOLD}; font-size: clamp(13px, 2.4vw, 15px); letter-spacing: 2px; text-transform: uppercase; font-weight: 900; }}
.yv-h1 {{ font-family: Georgia, serif; font-size: clamp(42px, 7vw, 82px); line-height: 1.02; margin: 10px 0 16px; letter-spacing: -1.2px; }}
.yv-h2 {{ font-family: Georgia, serif; color: {BRAND_BLUE}; font-size: clamp(30px, 5vw, 46px); line-height: 1.08; margin: 0 0 12px; }}
.yv-muted {{ color: rgba(71,55,46,.76); font-size: clamp(17px, 2.8vw, 20px); line-height: 1.65; }}
.yv-cinema {{ position: relative; border-radius: 38px; overflow: hidden; background: linear-gradient(135deg, #061626, {BRAND_BLUE}); box-shadow: 0 30px 80px rgba(14,42,71,.28); margin-bottom: 18px; isolation: isolate; }}
.yv-cinema:before {{ content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(6,22,38,.97) 0%, rgba(6,22,38,.88) 48%, rgba(6,22,38,.55) 100%); z-index: 1; }}
.yv-cinema-bg {{ position: absolute; inset: 0; background-size: cover; background-position: center; transform: scale(1.06); filter: saturate(.92) contrast(1.02); opacity: .40; animation: slowZoom 18s ease-in-out infinite alternate; }}
.yv-cinema-content {{ position: relative; z-index: 2; padding: clamp(30px, 6vw, 68px); max-width: 1040px; }}
.yv-orb {{ position: absolute; width: 360px; height: 360px; right: -120px; top: -120px; border-radius: 50%; background: radial-gradient(circle, rgba(198,169,106,.32), transparent 66%); z-index: 2; }}
.yv-story {{ font-size: clamp(19px, 2.2vw, 24px); line-height: 1.62; color: rgba(250,246,239,.93); max-width: 1000px; }}
.yv-white-muted {{ color: rgba(250,246,239,.84); font-size: clamp(17px, 3.2vw, 21px); line-height: 1.65; }}
.yv-overview {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin-top: 20px; }}
.yv-overview-card {{ background: rgba(14,42,71,.055); border: 1px solid rgba(14,42,71,.10); border-radius: 22px; padding: 20px; min-height: 120px; font-size: clamp(17px, 3.2vw, 20px); line-height: 1.55; }}
.yv-overview-card b {{ color: {BRAND_BLUE}; font-size: clamp(18px, 3.4vw, 21px); }}
.yv-blocks {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 22px 0 18px; }}
.yv-story-block {{ border-radius: 24px; padding: 20px 22px; border: 1px solid rgba(250,246,239,.16); background: rgba(250,246,239,.09); color: rgba(250,246,239,.93); font-size: clamp(18px, 3.6vw, 22px); line-height: 1.68; }}
.yv-story-block:nth-child(even) {{ background: rgba(198,169,106,.13); }}
.yv-story-block-title {{ color: {BRAND_GOLD}; letter-spacing: 1.4px; font-size: clamp(13px, 2.8vw, 15px); font-weight: 900; text-transform: uppercase; margin-bottom: 10px; }}
.yv-steps {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin-top: 18px; }}
.yv-step {{ background: rgba(250,246,239,.10); border: 1px solid rgba(250,246,239,.18); border-radius: 22px; padding: 18px; color: rgba(250,246,239,.92); font-size: clamp(17px, 3.2vw, 20px); line-height: 1.5; }}
.yv-step b {{ color: {BRAND_GOLD}; font-size: clamp(17px, 3.2vw, 20px); }}
.yv-progress {{ display: flex; gap: 7px; margin: 18px 0 22px; overflow: hidden; }}
.yv-dot {{ height: 8px; flex: 1; border-radius: 999px; background: rgba(14,42,71,.15); }}
.yv-dot-on {{ background: linear-gradient(90deg, {BRAND_GOLD}, #E6D1A0); box-shadow: 0 0 12px rgba(198,169,106,.45); }}
.yv-feedback {{ background: rgba(255,255,255,.74); border: 1px solid rgba(14,42,71,.10); border-radius: 28px; padding: 24px 26px; margin: 18px 0; }}
.yv-feedback-title {{ color: {BRAND_BLUE}; font-weight: 800; margin-bottom: 12px; font-size: clamp(18px, 3.4vw, 22px); }}
.yv-feedback-selected {{ color: rgba(71,55,46,.76); font-size: clamp(16px, 3vw, 19px); margin-top: 8px; }}
.yv-celebration {{ text-align: center; padding: 50px 24px; }}
.yv-language {{ max-width: 430px; margin: 0 0 14px auto; }}
.stButton > button {{ border-radius: 999px !important; background: {BRAND_BLUE} !important; color: {BRAND_BG_SOFT} !important; border: 1px solid rgba(14,42,71,.2) !important; min-height: 3.15rem !important; font-size: 17px !important; font-weight: 900 !important; padding: 0 24px !important; }}
.stTextInput input, .stTextArea textarea {{ border-radius: 18px !important; border: 1px solid rgba(14,42,71,.16) !important; background: rgba(255,255,255,.82) !important; font-size: 17px !important; }}
button[kind="secondary"] {{ font-size: 28px !important; }}
@keyframes slowZoom {{ from {{ transform: scale(1.04); }} to {{ transform: scale(1.14); }} }}
@media(max-width:760px) {{
    .block-container {{ padding-left: .8rem; padding-right: .8rem; padding-top: .8rem; }}
    .yv-overview, .yv-blocks, .yv-steps {{ grid-template-columns: 1fr; }}
    .yv-cinema {{ border-radius: 28px; }}
    .yv-cinema:before {{ background: linear-gradient(180deg, rgba(6,22,38,.96), rgba(6,22,38,.82)); }}
    .yv-cinema-content {{ padding: 30px 20px; }}
    .yv-h1 {{ font-size: clamp(42px, 12vw, 60px); line-height: 1.02; }}
    .yv-h2 {{ font-size: clamp(30px, 8vw, 42px); }}
    .yv-title {{ font-size: clamp(27px, 7vw, 38px); }}
    .yv-subtitle {{ font-size: 17px; }}
    .yv-story {{ font-size: clamp(19px, 4.2vw, 23px); line-height: 1.62; }}
    .yv-story-block {{ font-size: clamp(19px, 4.5vw, 23px); line-height: 1.7; padding: 22px 20px; }}
    .yv-step {{ font-size: clamp(18px, 4.2vw, 21px); line-height: 1.55; }}
    .stButton > button {{ font-size: 18px !important; min-height: 3.35rem !important; }}
}}
</style>
""",
        unsafe_allow_html=True,
    )
