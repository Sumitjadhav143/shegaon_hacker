import re
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
from gtts import gTTS

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configure Gemini API with the key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(
    history=[]
)

@app.route('/')
def index():
    return render_template('index.html')

# Route for /text to render text.html
@app.route("/text")
def text():
    return render_template("text.html")

# Route for /audio to render audio.html
@app.route("/audio")
def audio():
    return render_template("audio.html")

@app.route('/gemini-response', methods=['POST'])
def get_gemini_response():
    try:
        user_message = request.json['message']
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Send the user message to the Gemini model
        response = chat_session.send_message(user_message)

        # Get the response text from Gemini
        ai_response = response.text.strip()

        # Format the response (remove markdown-like symbols, you can expand this as needed)
        formatted_response = format_response(ai_response)

        return jsonify({"response": formatted_response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


def format_response(response_text):
    """
    This function is used to format the response by removing unwanted formatting like '**' for bold.
    You can expand it to handle other markdown or special formatting.
    """
    # Remove markdown-like formatting (example: **bold text**)
    response_text = re.sub(r'\*\*(.*?)\*\*', r'\1', response_text)  # Remove bold markdown
    response_text = re.sub(r'__(.*?)__', r'\1', response_text)  # Remove underline markdown

    # You can add more patterns here as needed

    # Optionally, you can clean up extra spaces or characters
    response_text = re.sub(r'\s+', ' ', response_text)  # Remove extra spaces

    # creating the audio file
    tts = gTTS(text=response_text,lang='en',lang_check=True)
    tts.save('C:\\Users\\SUMIT JADHAV\\Desktop\\shegaon\\static\\audio.mp3')

    return response_text


if __name__ == '__main__':
    app.run(debug=True)
