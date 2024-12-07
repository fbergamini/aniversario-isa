import requests
import base64

# Define the API endpoint and key
url = "https://api.sync.so/v2/generate"
api_key = "13ee7731-504d-4757-923d-99a2eda72fd9"

# Function to read a local file and convert it to a base64 string
def file_to_base64(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

# Paths to local video and audio files
video_path = "video.mp4"
audio_path = "audio.mp4"

# Read and encode local files
video_base64 = file_to_base64(video_path)
audio_base64 = file_to_base64(audio_path)

# Construct the payload
payload = {
    "model": "lipsync-1.8.0",
    "input": [
        {
            "type": "video",
            "data": video_base64
        },
        {
            "type": "audio",
            "data": audio_base64
        }
    ],
    "options": {"pads": [0, 5, 0, 0], "output_format": "mp4", "sync_mode": "bounce"},
}

# Set the headers
headers = {
    "x-api-key": api_key,
    "Content-Type": "application/json"
}

# Send the request
response = requests.post(url, json=payload, headers=headers)

# Print the response
print(response.text)
