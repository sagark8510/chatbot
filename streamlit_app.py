import streamlit as st
import requests

st.set_page_config(page_title="Model Finder", layout="centered")

st.title("🔍 Model Finder Bot")
st.write("Ruk bhai, Google ke server se seedha models ki list nikalte hain...")

try:
    # Teri secure API key
    API_KEY = st.secrets["GEMINI_API_KEY"]
    
    # Seedha Google API se models ki list maangna
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        st.success("✅ List mil gayi! Ye rahe wo models jo chat (generateContent) ke liye chalte hain:")
        
        # Sirf wahi models dikhayega jo tere kaam ke hain
        for model in data.get("models", []):
            if "generateContent" in model.get("supportedGenerationMethods", []):
                # Naam mein se 'models/' hata kar saaf naam print karega
                model_name = model["name"].replace("models/", "")
                st.code(model_name)
    else:
        st.error(f"Error aa gaya API fetch karne mein: {response.text}")
        
except Exception as e:
    st.error(f"Secrets ya API mein koi dikkat hai: {e}")
    
