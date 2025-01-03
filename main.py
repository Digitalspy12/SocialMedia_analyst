# don't forget to add open api key in langflow and Authentication token in .env file
import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "22fb6b75-6045-4708-8145-b940ac57271f"
FLOW_ID = "65fb470f-44e9-4d49-96d9-7b0da3c2fba8"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "SocialMediabot"


def run_flow(message: str,) -> dict:
    
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Social Media Analysis ")
    st.header("Model use is openai  ")
   

    message = st.text_area("Message", placeholder="Ask something...")

    if st.button("Analysis"):
        if not message.strip():
            st.error("Please enter a message")
            return

        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
