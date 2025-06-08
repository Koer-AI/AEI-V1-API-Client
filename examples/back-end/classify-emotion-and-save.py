import requests
import os

def classify_emotion_from_audio(audio_file_url: str, your_email: str, your_api_key: str) -> dict:
    """
    Sends an audio file URL to the voice emotion API for classification.

    Args:
        audio_file_url: The public or signed URL of the audio file.
        your_email: Your registered email for API authentication.
        your_api_key: Your API key for authentication.

    Returns:
        A dictionary containing the API response (emotion classification) or an error.
    """
    # --- IMPORTANT: REPLACE WITH YOUR ACTUAL VALUES ---
    AEI_V1_API_ENDPOINT = "https://api.yourcompany.com/v1/classify-emotion" # Your actual API endpoint goes here
    # ---------------------------------------------------

    headers = {
        "Email": your_email,
        "Authorization": your_api_key
    }

    print(f"\nSending request to AEI-V1 API...")
    print(f"Headers: {headers}")
    print(f"Audio URL: {audio_file_url}")

    try:
        response = requests.post(
            AEI_V1_API_ENDPOINT,
            headers=headers,
            params={"audio_path_or_url": audio_file_url}
        )

        if response.status_code == 200:
            print("\n--- API Response (Success) ---")
            return response.json()
        else:
            print(f"\n--- API Error (Status Code: {response.status_code}) ---")
            print("Response Text:", response.text)
            try:
                print("Response JSON:", response.json())
                return {"error": response.json()}
            except requests.exceptions.JSONDecodeError:
                return {"error": response.text}
    except requests.exceptions.RequestException as e:
        print(f"\n--- Network/Request Error ---")
        print(e)
        return {"error": str(e)}

# --- Example Usage (to be integrated after audio upload) ---
if __name__ == "__main__":
    # This would typically be the URL returned from your audio upload service
    SAMPLE_AUDIO_URL = "YOUR_PUBLIC_OR_SIGNED_AUDIO_FILE_URL_HERE"
    YOUR_EMAIL_CONFIG = os.environ.get("YOUR_API_EMAIL", "your_registered_email@example.com")
    YOUR_API_KEY_CONFIG = os.environ.get("YOUR_API_KEY", "YOUR_API_KEY_HERE")

    if SAMPLE_AUDIO_URL != "YOUR_PUBLIC_OR_SIGNED_AUDIO_FILE_URL_HERE" and \
       YOUR_EMAIL_CONFIG != "your_registered_email@example.com" and \
       YOUR_API_KEY_CONFIG != "YOUR_API_KEY_HERE":
        emotion_result = classify_emotion_from_audio(
            SAMPLE_AUDIO_URL,
            YOUR_EMAIL_CONFIG,
            YOUR_API_KEY_CONFIG
        )
        print("\nEmotion Classification Result:", emotion_result)
    else:
        print("\nPlease configure SAMPLE_AUDIO_URL, YOUR_EMAIL_CONFIG, and YOUR_API_KEY_CONFIG for testing.")

# Example: Pseudo-code for storing emotion data in a database
def save_survey_response_with_emotion(
    survey_id: str,
    participant_id: str,
    question_id: str,
    audio_url: str,
    emotion_data: dict
):
    """
    Saves the survey response along with the emotion classification data to your database.
    """
    # This would involve your ORM or direct database calls (e.g., SQLAlchemy, Django ORM)
    print(f"Saving response for Survey: {survey_id}, Participant: {participant_id}")
    print(f"Question: {question_id}, Audio URL: {audio_url}")
    print(f"Emotion Data: {emotion_data}")

    # Example: In a SQL database, you might have a table like:
    # CREATE TABLE survey_responses (
    #     id INT PRIMARY KEY AUTO_INCREMENT,
    #     survey_id VARCHAR(255),
    #     participant_id VARCHAR(255),
    #     question_id VARCHAR(255),
    #     audio_url TEXT,
    #     dominant_emotion VARCHAR(50),
    #     emotion_scores JSON, -- Store full JSON for detailed analysis
    #     timestamp DATETIME
    # );

    # Logic to insert/update your database
    # For example:
    # db_connection.execute(
    #     "INSERT INTO survey_responses (survey_id, participant_id, question_id, audio_url, dominant_emotion, emotion_scores, timestamp) VALUES (?, ?, ?, ?, ?, ?, NOW())",
    #     (survey_id, participant_id, question_id, audio_url, emotion_data.get('dominant_emotion'), json.dumps(emotion_data),)
    # )
    print("Data saved to database (pseudo-code).")

# Example of how you'd call this after API classification
if __name__ == "__main__":
    # Assuming you have the emotion_result from classify_emotion_from_audio
    # and other survey context
    sample_emotion_result = {
        "dominant_emotion": "HAPPY",
    }

    if sample_emotion_result:
        save_survey_response_with_emotion(
            survey_id="SURVEY_XYZ",
            participant_id="PARTICIPANT_123",
            question_id="Q_AUDIO_1",
            audio_url="https://your-s3-bucket/survey_audio/12345.webm",
            emotion_data=sample_emotion_result
        )
