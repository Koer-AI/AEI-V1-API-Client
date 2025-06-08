import requests
import time
import os

# --- IMPORTANT: REPLACE WITH YOUR ACTUAL VALUES ---
# This URL should point to your own hosted audio file (public or temporary signed).
AUDIO_FILE_URL = "YOUR_PUBLIC_OR_SIGNED_AUDIO_FILE_URL_HERE"
YOUR_EMAIL = "your_registered_email@example.com"
YOUR_API_KEY = "YOUR_API_KEY_HERE" # Replace with your actual API key
# ---------------------------------------------------

# AEI-V1 API Endpoint (Pseudo Endpoint for documentation)
AEI_V1_API_ENDPOINT = "https://api.yourcompany.com/v1/classify-emotion" # Your actual API endpoint goes here

# Prepare headers for authentication
headers = {
    "Email": YOUR_EMAIL,
    "Authorization": YOUR_API_KEY
}

print(f"\nSending request to AEI-V1 API...")
print(f"Headers: {headers}")
print(f"Audio URL: {AUDIO_FILE_URL}")

# Make the POST request with the audio URL as a query parameter
response = requests.post(
    AEI_V1_API_ENDPOINT,
    headers=headers,
    params={"audio_path_or_url": AUDIO_FILE_URL}
)

# Process the response
if response.status_code == 200:
    print("\n--- API Response (Success) ---")
    print(response.json())
else:
    print(f"\n--- API Error (Status Code: {response.status_code}) ---")
    print("Response Text:", response.text)
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        pass # Not a JSON response, just print text
