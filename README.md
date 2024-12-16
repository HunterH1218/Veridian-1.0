# Veridian - AI-Powered Search and Response System

Veridian is an intelligent system that combines web search capabilities with AI-powered text processing to provide informative responses to user queries.

## Features

- Smart query processing to determine if web search is needed
- Automated Google search functionality
- Web content extraction and summarization
- Conversational AI responses for non-search queries
- Memory retention for context awareness

## Technical Components

- **Search Junction**: Determines if a query requires web search
- **Query Generator**: Optimizes user queries for search
- **Google Search**: Performs web searches and extracts content
- **Summarize Model**: Condenses search results into concise responses
- **Veridian Base Model**: Handles conversational responses

## Dependencies

- Google Generative AI (Gemini)
- BeautifulSoup4
- Requests

## Usage

1. Make sure you have a Gemini API key set in your environment variables
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Run the main script:
```bash
python main.py
```
4. Enter your queries at the prompt and receive AI-powered responses


## Example Usage

```
> What is the capital of France?
> Tell me about the latest AI developments
> How does photosynthesis work?
```

The system will automatically determine whether to search the web or provide a direct response.

## Contributing
We welcome contributions! Please fork the repository and submit a pull request for any bug fixes or enhancements.

