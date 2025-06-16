# backend/server.py (Secure Version)

import os # Import os for environment variable handling
import requests # Import requests for making HTTP requests
from flask import Flask, request, jsonify # Import Flask for creating the web server
from flask_cors import CORS # Import CORS for handling cross-origin requests

# ---Change 1: Import load_dotenv to load environment variables from a .env file---
from dotenv import load_dotenv # Import load_dotenv to load environment variables from a .env file

# ---Change 2: Ensure the .env file is loaded to access the OpenAI API key securely---
# Load environment variables from the .env file
load_dotenv()

# Create an instance of a Flask application
app = Flask(__name__)

# Use CORS to allow cross-origin requests from the frontend
CORS(app)

@app.route('/api/generate', methods=['POST'])
def generate_description():
    """
    Handles the API request to generate a product description.
    """
    data = request.get_json()
    product_name = data.get('productName')
    keywords = data.get('keywords')

    # --- THIS IS THE SECURE WAY TO HANDLE THE API KEY ---
    # The key is loaded from the .env file and is not in the source code.
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        # If the API key is not found, return a server error
        return jsonify({'error': 'OpenAI API key not found in .env file.'}), 500

    # The rest of the code is the same
    prompt = f'Write a short, catchy, and professional product description for a "{product_name}" that highlights these keywords: "{keywords}".'

    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Content-Type': 'application/json',
                # The API key from os.getenv() is securely used here
                'Authorization': f'Bearer {api_key}'
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 100,
            }
        )
        
        response.raise_for_status()

        completion = response.json()
        description = completion['choices'][0]['message']['content'].strip()
        
        return jsonify({'description': description})

    except requests.exceptions.RequestException as error:
        print(f'Error in /api/generate: {error}')
        return jsonify({'error': 'Failed to generate description.'}), 500

# Start the server
if __name__ == '__main__':
    app.run(port=5001)