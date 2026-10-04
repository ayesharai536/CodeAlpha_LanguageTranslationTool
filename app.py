import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="AI Language Translator", page_icon="🌐")

st.title("🌐 Language Translation Tool")
st.write("Kisi bhi text ko doosri zubaan mein translate karein.")

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Urdu": "ur",
    "Hindi": "hi",
    "Arabic": "ar"
}

source_lang = st.selectbox("Select Source Language:", ["Auto Detect"] + list(languages.keys()))
target_lang = st.selectbox("Select Target Language:", list(languages.keys()), index=0)

input_text = st.text_area("Yahan text likhein:", height=150)

if st.button("Translate"):
    if input_text.strip():
        try:
            src_code = "auto" if source_lang == "Auto Detect" else languages[source_lang]
            tgt_code = languages[target_lang]
            
            translated = GoogleTranslator(source=src_code, target=tgt_code).translate(input_text)
            
            st.success("Translation complete!")
            st.text_area("Translated Result:", value=translated, height=150)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch text likhein.")