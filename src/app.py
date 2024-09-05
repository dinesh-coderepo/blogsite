from flask import Flask, redirect, url_for, request, render_template, session, send_from_directory
import requests, os, uuid, json
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from dotenv import load_dotenv
from flask import url_for

app = Flask(__name__)

class ImagePathProcessor(Treeprocessor):
    def __init__(self, md, folder):
        super().__init__(md)
        self.folder = folder

    def run(self, root):
        for element in root.iter('img'):
            src = element.get('src')
            if src:
                element.set('src', url_for('blog_image', folder=self.folder, filename=src, _external=True))

class ImagePathExtension(Extension):
    def __init__(self, folder):
        self.folder = folder
        super().__init__()

    def extendMarkdown(self, md):
        md.treeprocessors.register(ImagePathProcessor(md, self.folder), 'imagepath', 15)

# Add these imports at the top of your file
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

@app.route('/translator',methods=['GET'])
def index():
    return render_template('index_translator.html')


@app.route('/translator', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']


    # Load environment variables from .env file if running locally
    load_dotenv()  # Only loads if .env file exists
    key = os.getenv('KEY')
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

def load_blog_posts():
    posts = []
    blog_posts_dir = os.path.join(app.root_path, 'blog_posts')
    for folder in os.listdir(blog_posts_dir):
        post_dir = os.path.join(blog_posts_dir, folder)
        if os.path.isdir(post_dir):
            content_path = os.path.join(post_dir, 'content.md')
            if os.path.exists(content_path):
                with open(content_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    md = markdown.Markdown(extensions=['meta', ImagePathExtension(folder)])
                    html_content = md.convert(content)
                    meta = md.Meta
                    
                    image_files = [f for f in os.listdir(post_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
                    
                    posts.append({
                        'id': folder,
                        'title': meta.get('title', [''])[0],
                        'subheading': meta.get('subheading', [''])[0],
                        'date': meta.get('date', [''])[0],
                        'content': html_content,
                        'image_files': image_files
                    })
    return sorted(posts, key=lambda x: x['date'], reverse=True)

    
@app.route('/')
def home():
    blogs = load_blog_posts()
    return render_template('index_blog.html', blogs=blogs)

@app.route('/blog/<string:folder>')
def blog(folder):
    posts = load_blog_posts()
    post = next((p for p in posts if p['id'] == folder), None)
    if post:
        return render_template('blog.html', blog=post)
    return "Blog not found", 404

@app.route('/blog/<string:folder>/<path:filename>')
def blog_image(folder, filename):
    print(f"Serving image: {filename} from folder: {folder}")  # Debugging line
    image_path = os.path.join(app.root_path, 'blog_posts', folder, filename)
    print(f"Full image path: {image_path}")  # Debugging line
    if os.path.exists(image_path):
        return send_from_directory(os.path.join(app.root_path, 'blog_posts', folder), filename)
    else:
        print(f"Image not found: {image_path}")  # Debugging line
        return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=True)