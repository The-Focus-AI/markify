# Markify

A Python web service that converts web pages to Markdown format.

## Installation

### Development Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/markify.git
   cd markify
   ```

2. Set up the development environment:
   ```bash
   mise run setup-dev
   ```

### Production Installation

1. Install the package:
   ```bash
   pip install markify
   ```

## Usage

### Running the Development Server

```bash
mise run dev
```

### Running the Production Server

```bash
markify
```

### API Usage

#### Convert from URL

Send a POST request to `/tomarkdown` with a JSON body containing a URL:

```bash
curl -X POST http://localhost:${PORT:-5001}/tomarkdown \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

You can also use a GET request with a URL parameter:

```bash
curl "http://localhost:${PORT:-5001}/tomarkdown?url=https://example.com"
```

#### Convert HTML Directly

Send a POST request to `/html2markdown` with raw HTML content in the request body:

```bash
curl -X POST http://localhost:${PORT:-5001}/html2markdown \
  -H "Content-Type: text/html" \
  -d '<h1>Hello World</h1><p>This is a test</p>'
```

Or send the contents of an HTML file:

```bash
curl -X POST http://localhost:${PORT:-5001}/html2markdown \
  -H "Content-Type: text/html" \
  --data-binary @your-file.html
```

The server runs on port 5001 by default, but this can be configured by setting the `PORT` environment variable. In the Docker container, it runs on port 8080.

### Response Format

For URL conversions and direct HTML conversions, the response will be the markdown text directly in the response body. In case of errors, you'll receive a JSON error response:

```json
{
  "error": "Error message here"
}
```

## Development

### Available Commands

- `mise run setup-dev`: Set up the development environment
- `mise run install`: Install dependencies
- `mise run dev`: Run the development server
- `mise run info`: Print project information

### Code Style

This project uses:

- Black for code formatting
- isort for import sorting
- flake8 for linting

Run the following to format code:

```bash
black .
isort .
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
