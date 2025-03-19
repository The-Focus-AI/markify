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

Send a POST request to `/tomarkdown` with a JSON body containing a URL:

```bash
curl -X POST http://localhost:${PORT:-5001}/tomarkdown \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

The server runs on port 5001 by default, but this can be configured by setting the `PORT` environment variable. In the Docker container, it runs on port 8080.

### Response Format

```json
{
  "path": "/tmp/example123456.md",
  "text": "# Example Domain\n\nThis domain is..."
}
```

The `path` field contains the path to the temporary file where the markdown was saved, and the `text` field contains the actual markdown content.

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
