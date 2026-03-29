# AI Document Analyzer

An AI-powered tool that reads documents and answers questions about their content using Python and Claude API.

## Features

- Load any text document for analysis
- Ask questions about the document content in natural language
- Conversation memory — follow-up questions understand context
- Multi-document support — analyze multiple files in one session
- Saves analysis logs with timestamps

## Use Cases

- Analyze school IT policies and extract key requirements
- Summarize long documents quickly
- Find specific information across policy documents
- Review staff communications and extract action items

## Tech Stack

- Python 3
- Anthropic Claude API
- python-dotenv (environment variable management)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/damian80/ai-document-analyzer.git
cd ai-document-analyzer
```

2. Install dependencies:
```bash
pip3 install anthropic python-dotenv
```

3. Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```

4. Run the analyzer:
```bash
python3 "AI Document Analyzer.py"
```

## Usage

```
Enter file path (or 'quit' to exit): school_policy.txt
Document loaded! Ask me anything about it. Type 'done' for next document.

You: Summarize this document
Analyzer: This document outlines the IT Acceptable Use Policy...

You: Can students install software?
Analyzer: No, according to the policy all software must be installed by the IT department...

You: done
Document closed.

Enter file path (or 'quit' to exit): quit
Analysis saved!
```

## Author

Built by Damian Ciasnocha as part of an AI Engineering portfolio.
