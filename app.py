import streamlit as st

st.set_page_config(page_title='YVORA Global', layout='wide')

LANGS = {
    'pt': 'Português',
    'en': 'English',
    'zh': '中文'
}

if 'lang' not in st.session_state:
    st.session_state.lang = 'pt'

st.markdown('''
<style>
html, body, [data-testid="stAppViewContainer"] {
    background: #faf6ef;
}
</style>
''', unsafe_allow_html=True)

col1, col2 = st.columns([6,1])

with col1:
    st.title('Experiência Tábua YVORA')

with col2:
    selected = st.selectbox(
        'Language',
        options=list(LANGS.keys()),
        format_func=lambda x: LANGS[x],
        index=list(LANGS.keys()).index(st.session_state.lang)
    )
    st.session_state.lang = selected

lang = st.session_state.lang

messages = {
    'pt': {
        'welcome': 'Bem-vindo à jornada sensorial YVORA.',
        'description': 'Explore carnes, queijos e harmonizações guiadas.'
    },
    'en': {
        'welcome': 'Welcome to the YVORA sensory journey.',
        'description': 'Explore meats, cheeses and guided pairings.'
    },
    'zh': {
        'welcome': '欢迎来到 YVORA 感官体验。',
        'description': '探索肉类、奶酪与风味搭配。'
    }
}

st.subheader(messages[lang]['welcome'])
st.write(messages[lang]['description'])

st.info('Estrutura global inicial criada com suporte multilíngue. Próximo passo: conectar os campos traduzidos da planilha.')
