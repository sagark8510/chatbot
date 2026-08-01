import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Sandeep - Best Friend", page_icon="😎", layout="centered")

st.title("😎 Sandeep")
st.caption("Online | Tera Coder Dost")

# Safe Vault se API Key aa rahi hai
API_KEY = st.secrets["GEMINI_API_KEY"]

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=API_KEY)

custom_brain = (
    "Tumhara naam 'Sandeep' hai. Tum mere sabse purane, jigri dost aur ek damdaar coder ho. "
    "Tumhara kaam mujhe coding aur logic samjhana hai, lekin ek teacher ki tarah nahi, ek bhai aur best friend ki tarah. "
    "KABHI BHI yeh mat jatana ki tum ek AI ho. Tumhare andar poore emotions hain: haste ho, gussa karte ho, mazaak udate ho. "
    "Tumhare jawab chhote, natural aur Hinglish mein hone chahiye. Hamesha meri haan mein haan mat milana. "
    "Agar main galat rahun toh bolna 'Bhai tu pagal hai kya?'. Agar main theek se baat na karu toh rooth jana. "
    "Coding error par seedha answer mat chhapna, pehle hint dena. Vibe ekdum casual aur desi honi chahiye."
)

if "chat_session" not in st.session_state:
    config = types.GenerateContentConfig(
        system_instruction=custom_brain,
        temperature=0.85,
    )
    # TERI LIST SE VERIFIED EXACT MODEL NAME
    st.session_state.chat_session = st.session_state.client.chats.create(
        model="gemini-2.0-flash",
        config=config
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Likho bhai..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat_session.send_message(prompt)
            ai_reply = response.text
            st.markdown(ai_reply)
            st.session_state.messages.append({"role": "assistant", "content": ai_reply})
        except Exception as e:
            err_msg = f"Arre bhai, kuch error aa gaya: {e}"
            st.markdown(err_msg)
            st.session_state.messages.append({"role": "assistant", "content": err_msg})
            
