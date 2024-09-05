from flask import Flask, redirect, url_for, request, render_template, session
import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


@app.route('/translator',methods=['GET'])
def index():
    return render_template('index_translator.html')


@app.route('/translator', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    if os.getenv('FLASK_ENV') == 'development':
        # Load environment variables from .env file if running locally
        load_dotenv()  # Only loads if .env file exists
        key = os.getenv('KEY')
        endpoint = os.getenv('ENDPOINT')
        location = os.getenv('LOCATION')
    else:
        # Assume running in production and fetching from environment (Key Vault during deployment)
        key = os.getenv('KEY')  # These should be set by GitHub Actions during deployment
        endpoint = os.getenv('ENDPOINT')
        location = os.getenv('LOCATION')


    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language
    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{ 'text': original_text }]

    # Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    # Retrieve the JSON response
    translator_response = translator_request.json()
    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results_translator.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )

def load_blogs():
    with open('blogs.json', 'r') as file:
        return json.load(file)
    
@app.route('/')
def home():
    blogs = load_blogs()
    return render_template('index_blog.html', blogs=blogs)

@app.route('/blog/<int:id>')
def blog(id):
    blogs = load_blogs()
    blog = next((b for b in blogs if b['id'] == id), None)
    if blog:
        return render_template('blog.html', blog=blog)
    return "Blog not found", 404


if __name__ == '__main__':
    app.run(debug=True)