# Webpage Summarizer using Large Language Models

A Python tool that creates summaries of web pages using Google's Gemini AI model. Think of it as the "Reader's Digest of the internet" - give it a URL, and it will respond with a concise summary!

## Features

- Extracts and cleans webpage content using BeautifulSoup
- Removes irrelevant elements (scripts, styles, images, inputs)
- Generates intelligent summaries using Google's Gemini 2.5 Flash model
- Supports markdown output for better formatting
- Includes proper headers for website compatibility

## Prerequisites

Before starting, you should have:
- Python 3.7 or higher
- A Google API key for Gemini
- Jupyter Lab (optional, for interactive development)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/webpage-summarizer.git
cd webpage-summarizer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Required Dependencies

Create a `requirements.txt` file with:
```
requests
python-dotenv
beautifulsoup4
ipython
openai
```

## Setup Instructions

### Getting Your Google API Key

1. Visit the [Google AI Studio](https://aistudio.google.com/)
2. Create a new project or select an existing one
3. Enable the Gemini API
4. Generate an API key
5. Add the key to your `.env` file

### Environment Setup

1. **For PC/Mac**: Set up your Python environment as described in the installation section
2. **For Jupyter Lab**: Launch Jupyter Lab from within the project root directory with your environment activated

```bash
jupyter lab
```

## Usage

### Basic Usage

```python
from webpage_summarizer import summarize, display_summary

# Get a text summary
summary = summarize("https://example.com")
print(summary)

# Display formatted summary in Jupyter
display_summary("https://example.com")
```

### Running the Script

```bash
python webpage_summarizer.py
```

### Class Usage

```python
from webpage_summarizer import Website

# Create a website object
website = Website("https://example.com")
print(website.title)
print(website.text)
```

## How It Works

1. **Website Class**: Fetches and processes webpage content
   - Uses requests with proper headers for compatibility
   - Extracts title and text content
   - Removes irrelevant HTML elements

2. **Prompt Engineering**: Creates structured prompts for the AI model
   - System prompt defines the AI's role and output format
   - User prompt includes website content and instructions

3. **AI Processing**: Uses Google's Gemini 2.5 Flash model
   - Analyzes webpage content
   - Generates concise summaries
   - Ignores navigation and irrelevant text

## Customization

### Changing the Output Language

Modify the system prompt in the code:
```python
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown in Spanish."
```

### Using Different Models

Change the model parameter in the `summarize` function:
```python
response = gemini.chat.completions.create(
    model = "gemini-2.5-flash-preview-05-20",  # Change this
    messages = messages_for(website)
)
```

## Examples

```python
# Summarize a news website
display_summary("https://cnn.com")

# Summarize a blog post
display_summary("https://medium.com/@author/article-title")

# Summarize a documentation page
display_summary("https://docs.python.org/3/")
```

## Error Handling

The tool includes basic error handling for:
- Missing page titles
- Failed HTTP requests
- API connection issues

## Limitations

- Some websites may block automated requests
- Very large pages may exceed API token limits
- Dynamic content loaded by JavaScript may not be captured

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Google's Gemini AI
- Web scraping powered by BeautifulSoup
- Based on the concept of creating a "Reader's Digest of the internet"

## Troubleshooting

### Common Issues

1. **API Key Not Working**: Ensure your Google API key is valid and has Gemini access enabled
2. **Import Errors**: Make sure all dependencies are installed in your virtual environment
3. **Website Access Denied**: Some websites block automated requests - try different URLs
4. **Jupyter Display Issues**: Ensure you're running in a Jupyter environment for markdown display

### Getting Help

If you encounter issues:
1. Check that your `.env` file is properly configured
2. Verify your internet connection
3. Test with different websites
4. Check the console output for error messages
