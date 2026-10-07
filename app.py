import streamlit as st
from PIL import Image
from src.animal_recognition import AnimalRecognizer
from src.tourism_assistant import TourismAssistant

st.set_page_config(page_title="AI Animal Recognition & Tourism Assistant", page_icon="🦁", layout="wide")
st.title("🦁 AI Animal Recognition & Tourism Assistant")
st.caption("AI-powered wildlife recognition and Rwanda tourism information")

@st.cache_resource
def get_model():
    return AnimalRecognizer()

@st.cache_resource
def get_assistant():
    return TourismAssistant("data/animals.json")

tab1, tab2 = st.tabs(["🦁 Animal Recognition", "🇷🇼 Tourism Assistant"])

with tab1:
    st.subheader("Upload an animal image")
    file = st.file_uploader("Choose JPG, JPEG or PNG", type=["jpg","jpeg","png"])
    if file:
        image=Image.open(file).convert("RGB")
        left,right=st.columns(2)
        with left: st.image(image, caption="Uploaded image", use_container_width=True)
        with right:
            try:
                with st.spinner("Analyzing image..."):
                    results=get_model().predict(image)
                best=results[0]
                st.success(f"Detected: {best['label'].title()}")
                st.metric("Confidence", f"{best['score']*100:.2f}%")
                st.write("### Top predictions")
                for r in results:
                    st.write(f"**{r['label'].title()}** — {r['score']*100:.2f}%")
                info=get_model().animal_info(best["label"])
                if info:
                    st.divider()
                    st.subheader(info["common_name"])
                    st.write(info["description"])
                    st.write("**Habitat:**",info["habitat"])
                    st.write("**Conservation:**",info["conservation_status"])
                    st.write("**Rwanda location:**",info["rwanda_locations"])
                    st.write("**Tourism tip:**",info["tourism_tip"])
            except Exception as e:
                st.error("The AI model could not be loaded.")
                st.code(str(e))
                st.info("Run: pip install -r requirements.txt")

with tab2:
    st.subheader("🇷🇼 Rwanda Tourism Assistant")
    q=st.text_input("Ask a question", placeholder="Where can I see gorillas?")
    if q:
        assistant=get_assistant()
        answer,sources=assistant.answer(q)
        st.markdown(answer)
        if sources: st.caption("Knowledge areas: "+", ".join(sources))
        image=assistant.image_for_question(q)
        if image:
            st.image(image["url"], caption=sources[0], use_container_width=True)
            st.markdown(
                f'Photo: {image["credit"]} — '
                f'[{image["license"]}]({image["license_url"]}) '
                f'([source]({image["source_url"]})).'
            )
