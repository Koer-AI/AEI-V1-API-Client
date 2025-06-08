# Example: Python Flask endpoint for receiving audio and uploading to S3 (pseudo-code)
from flask import Flask, request, jsonify
import boto3
import os
import uuid

app = Flask(__name__)

# Configure your S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)
S3_BUCKET_NAME = 'your-audio-survey-bucket'

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Generate a unique filename
    filename = f"survey_audio/{uuid.uuid4()}.webm"

    try:
        s3.upload_fileobj(audio_file, S3_BUCKET_NAME, filename)
        # Construct the public URL or a signed URL
        audio_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{filename}"
        # For signed URLs, you'd generate one:
        # audio_url = s3.generate_presigned_url('get_object', Params={'Bucket': S3_BUCKET_NAME, 'Key': filename}, ExpiresIn=3600) # URL valid for 1 hour

        return jsonify({"message": "Audio uploaded successfully", "audio_url": audio_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
