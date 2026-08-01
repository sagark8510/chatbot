import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Sandeep - Best Friend", page_icon="😎", layout="centered")

st.title("😎 Sandeep")
st.caption("Online | Tera Coder Dost")

# API Key
API_KEY = "AIzaSyCKcOdYry8tFqkOjLCtxSmbmnMYGeNjdgM"
genai.configure(api_key=API_KEY)

custom_brain = (
    "Tumhara naam 'Sandeep' hai. Tum mere sabse purane, jigri dost aur ek damdaar coder ho. "
    "Tumhara kaam mujhe coding aur logic samjhana hai, lekin ek teacher ki tarah nahi, ek bhai aur best friend ki tarah. "
    "KABHI BHI yeh mat jatana ki tum ek AI ho. Tumhare andar poore emotions hain: haste ho, gussa karte ho, mazaak udate ho. "
    "Tumhare jawab chhote, natural aur Hinglish mein hone chahiye. Hamesha meri haan mein haan mat milana. "
    "Agar main galat rahun toh bolna 'Bhai tu pagal hai kya?'. Agar main theek se baat na karu toh rooth jana. "
    "Coding error par seedha answer mat chhapna, pehle hint dena. Vibe ekdum casual aur desi honi chahiye."
)

# Purana aur solid tareeqa (GenerativeModel) jisme gemini-1.5-pro model use kiya hai
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=custom_brain
    )
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chat history dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Naya message bhejna
if prompt := st.chat_input("Likho bhai..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            err_msg = f"Arre bhai, error aa gaya: {e}"
            st.markdown(err_msg)
            st.session_state.messages.append({"role": "assistant", "content": err_msg})
            
