from fastapi import FastAPI
from pydantic import BaseModel
import re
import random

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Emotion Prediction API!"}

# Define input schema
class CommentInput(BaseModel):
    comment: str

# Preprocessing function
def preprocess_comment(comment: str):
    """
    Cleans the input comment.
    
    Args:
        comment (str): Input comment text.
    
    Returns:
        str: Preprocessed comment.
    """
    comment = re.sub(r'http\S+', '', comment)  # Remove URLs
    comment = re.sub(r'[^a-zA-Z\s]', '', comment)  # Remove special characters
    comment = comment.lower().strip()  # Lowercase and strip whitespaces
    return comment

# Mock prediction function
def predict_emotion_mock(preprocessed_comment: str):
    """
    Simulates a prediction for the emotion of a comment.

    Args:
        preprocessed_comment (str): The preprocessed comment text.

    Returns:
        str: Predicted emotion.
    """
    # Define the possible emotions
    emotions = ['Anger', 'Fear', 'Joy', 'Love', 'Sadness', 'Surprise']

    # Simulate prediction logic
    if len(preprocessed_comment.split()) < 3:
        return 'Anger'  # Short comments likely to express anger
    elif "happy" in preprocessed_comment or "joy" in preprocessed_comment:
        return 'Joy'
    elif "love" in preprocessed_comment:
        return 'Love'
    elif "sad" in preprocessed_comment or "unhappy" in preprocessed_comment:
        return 'Sadness'
    elif "scared" in preprocessed_comment or "fear" in preprocessed_comment:
        return 'Fear'
    elif "wow" in preprocessed_comment or "amazing" in preprocessed_comment:
        return 'Surprise'
    else:
        # Return a random emotion if no other condition matches
        return random.choice(emotions)

# API to predict emotion
@app.post("/predict")
async def predict_emotion(data: CommentInput):
    """
    API endpoint to predict emotion based on the input comment.

    Args:
        data (CommentInput): Input data containing the comment.

    Returns:
        dict: Original comment, preprocessed comment, and predicted emotion.
    """
    # Preprocess the comment
    processed_comment = preprocess_comment(data.comment)

    # Mock prediction
    predicted_emotion = predict_emotion_mock(processed_comment)

    return {
        "comment": data.comment,
        "preprocessed_comment": processed_comment,
        "predicted_emotion": predicted_emotion
    }

# Run the app (only for local development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
