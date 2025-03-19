import os
import tempfile
import requests
from flask import Flask, request, jsonify, render_template_string
from markdownify import markdownify as md

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    def fetch_url_content(url):
        """Fetch content from a URL."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text

    def save_to_temp_file(content, suffix='.html'):
        """Save content to a temporary file."""
        fd, temp_path = tempfile.mkstemp(suffix=suffix)
        with os.fdopen(fd, 'w') as f:
            f.write(content)
        return temp_path

    def to_markdown(url):
        """Convert URL content to markdown."""
        try:
            # Fetch the content
            content = fetch_url_content(url)
            
            # Convert HTML to markdown
            return md(content)
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch URL: {str(e)}")
        except Exception as e:
            raise Exception(f"Error processing content: {str(e)}")

    @app.route('/')
    def index():
        """Landing page with link to markdownify."""
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Markify - URL to Markdown Converter</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 2rem;
                    line-height: 1.6;
                }
                h1 {
                    color: #2c3e50;
                    border-bottom: 2px solid #eee;
                    padding-bottom: 0.5rem;
                }
                .container {
                    background: #f8f9fa;
                    padding: 2rem;
                    border-radius: 8px;
                    margin-top: 2rem;
                }
                code {
                    background: #e9ecef;
                    padding: 0.2rem 0.4rem;
                    border-radius: 4px;
                    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
                }
                pre {
                    background: #e9ecef;
                    padding: 1rem;
                    border-radius: 4px;
                    overflow-x: auto;
                }
                a {
                    color: #0366d6;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <h1>Markify</h1>
            <p>A simple service that converts web pages to Markdown format.</p>
            
            <div class="container">
                <h2>API Usage</h2>
                <p>Send a POST request to <code>/tomarkdown</code> with a JSON body containing a URL:</p>
                <pre>curl -X POST http://localhost:5001/tomarkdown \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'</pre>
                
                <p>Or use GET request with a URL parameter:</p>
                <pre>curl "http://localhost:5001/tomarkdown?url=https://example.com"</pre>
            </div>

            <div class="container">
                <h2>About</h2>
                <p>This service is built using <a href="https://github.com/matthewwithanm/python-markdownify" target="_blank">markdownify</a>, a Python library that converts HTML to Markdown.</p>
            </div>
        </body>
        </html>
        '''
        return render_template_string(html)

    @app.route('/tomarkdown', methods=['GET', 'POST'])
    def convert_to_markdown():
        """API endpoint to convert URL to markdown."""
        if request.method == 'GET':
            url = request.args.get('url')
        else:
            data = request.json
            url = data.get('url') if data else None
        
        if not url:
            return jsonify({"error": "URL is required"}), 400
        
        try:
            markdown_text = to_markdown(url)
            return markdown_text
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

def main():
    """Run the application."""
    app = create_app()
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)

if __name__ == '__main__':
    main() 