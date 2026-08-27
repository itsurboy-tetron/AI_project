import streamlit as st
import easyocr
import numpy as np
from PIL import Image
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO

st.set_page_config(page_title="Multilingual Document Reader", layout="centered")

# ---------------------------
# Load OCR reader (cached so it doesn't reload on every rerun)
# ---------------------------
@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'])  # add more codes e.g. ['en', 'hi'] if needed

reader = load_reader()

# ---------------------------
# Language options for translation / speech
# ---------------------------
LANGUAGES = {
    "Nepali": "ne",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
}

st.title("\U0001F4C4 Multilingual Document Reader")
st.write("Upload a photo of a document, sign, or menu — get it read aloud in your chosen language.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
camera_file = st.camera_input("Or capture from camera")

image_file = uploaded_file or camera_file

if image_file:
    image = Image.open(image_file).convert("RGB")
    st.image(image, caption="Selected Image", use_container_width=True)

    # ---------------------------
    # Stage 1: OCR (Vision)
    # ---------------------------
    st.subheader("1\uFE0F\u20E3 Extracted Text")
    with st.spinner("Reading text from image..."):
        image_np = np.array(image)
        results = reader.readtext(image_np)
        extracted_text = " ".join([res[1] for res in results]).strip()

    if not extracted_text:
        st.warning("No text detected — try a clearer or closer image.")
    else:
        st.text_area("OCR Output (editable before translating)", extracted_text, height=120, key="ocr_text")

        # ---------------------------
        # Stage 2: Translation (NLP)
        # ---------------------------
        st.subheader("2\uFE0F\u20E3 Translate")
        target_lang_name = st.selectbox("Translate to:", list(LANGUAGES.keys()))
        target_lang_code = LANGUAGES[target_lang_name]

        text_to_translate = st.session_state.get("ocr_text", extracted_text)

        if st.button("Translate & Read Aloud"):
            with st.spinner("Translating..."):
                translated = GoogleTranslator(source='auto', target=target_lang_code).translate(text_to_translate)
            st.write(f"**{target_lang_name}:**", translated)

            # ---------------------------
            # Stage 3: Text-to-Speech (Speech)
            # ---------------------------
            st.subheader("3\uFE0F\u20E3 Listen")
            with st.spinner("Generating audio..."):
                tts = gTTS(text=translated, lang=target_lang_code)
                mp3_bytes = BytesIO()
                tts.write_to_fp(mp3_bytes)
                mp3_bytes.seek(0)
            st.audio(mp3_bytes.read(), format="audio/mp3")
