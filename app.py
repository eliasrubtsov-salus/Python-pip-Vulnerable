"""
Vulnerable Flask Application for Testing
WARNING: Contains intentional security vulnerabilities for testing purposes only
DO NOT deploy to production!
"""

from flask import Flask, request, render_template_string
import requests
import yaml
from PIL import Image
import io

app = Flask(__name__)

# Vulnerable: Using render_template_string with user input (Jinja2 SSTI)
@app.route('/')
def index():
    name = request.args.get('name', 'World')
    template = f'<h1>Hello {name}!</h1>'
    return render_template_string(template)

# Vulnerable: YAML unsafe load
@app.route('/parse_yaml', methods=['POST'])
def parse_yaml():
    yaml_data = request.data.decode('utf-8')
    try:
        # CVE-2020-14343: Arbitrary code execution via yaml.load
        data = yaml.load(yaml_data, Loader=yaml.Loader)
        return {'status': 'parsed', 'data': str(data)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

# Vulnerable: SQL injection potential with old sqlparse
@app.route('/query')
def query():
    user_query = request.args.get('q', '')
    # This would be vulnerable if actually connected to a database
    return {'query': user_query, 'status': 'received'}

# Vulnerable: Image processing with old Pillow version
@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return {'error': 'No image provided'}
    
    image_file = request.files['image']
    try:
        # Old Pillow versions have buffer overflow vulnerabilities
        img = Image.open(io.BytesIO(image_file.read()))
        return {'status': 'processed', 'size': img.size}
    except Exception as e:
        return {'error': str(e)}

# Vulnerable: Making external requests with old requests library
@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    try:
        # CVE-2023-32681: Proxy-Authorization header leak
        response = requests.get(url, timeout=5)
        return {'status': response.status_code, 'content_length': len(response.content)}
    except Exception as e:
        return {'error': str(e)}

# Vulnerable: Cookie handling with old Flask version
@app.route('/set_cookie')
def set_cookie():
    response = app.make_response('Cookie set')
    # CVE-2023-30861: Cookie parsing vulnerability in old Flask
    response.set_cookie('session', request.args.get('value', 'test'))
    return response

if __name__ == '__main__':
    # Running in debug mode (another vulnerability)
    app.run(debug=True, host='0.0.0.0', port=5000)
