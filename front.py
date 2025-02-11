import streamlit as st
import requests

# FastAPI endpoint URL
FASTAPI_URL = "http://127.0.0.1:8000/predict"

# Streamlit app title
st.title("Emotion Prediction App")

# Input field for user comment
comment = st.text_area("Enter a Facebook comment:", placeholder="Type your comment here...")

# Submit button
if st.button("Predict Emotion"):
    if comment.strip() == "":
        st.warning("Please enter a valid comment before submitting.")
    else:
        # Send a POST request to FastAPI
        try:
            response = requests.post(FASTAPI_URL, json={"comment": comment})
            if response.status_code == 200:
                result = response.json()
                #st.success("Prediction Successful!")
                #st.write(f"**Comment:** {result['comment']}")
                #st.write(f"**Preprocessed Comment:** {result['preprocessed_comment']}")
                st.write(f"**Predicted Emotion:** {result['predicted_emotion']}")
            else:
                st.error(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to the backend: {e}")


#Footer 

# Center-align the markdown text using HTML
st.markdown(
    """
    <div style="text-align: center;">
        <strong>Developed by Deepali Pateriya </strong>
    </div>
    """,
    unsafe_allow_html=True
)
