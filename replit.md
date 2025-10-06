# Overview

This project contains two CLI tools for content conversion:

## Web2LLMs (web2llms.py)
A command-line interface (CLI) tool designed to convert web page content into Markdown format and structure it according to the llms.txt specification. The tool fetches web pages, extracts their content, converts HTML to clean Markdown, and formats the output for optimal consumption by Large Language Models (LLMs).

**Status:** Completed and fully functional. The CLI accepts multiple URLs as input and generates properly formatted llms.txt files with structured content.

## Markdown to HTML Converter (md2html.py)
A command-line tool that converts Markdown files into beautifully styled HTML pages with automatic image extraction. The tool processes images from base64 data URIs, external URLs, and local file paths, saves them to an assets directory, and links them properly in the generated HTML.

**Status:** Completed and fully functional. The CLI converts markdown files with beautiful CSS styling and handles all image types.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Architecture
The project consists of two independent CLI tools, each in its own file:

### web2llms.py
Single-file, class-based architecture with `Web2LLMsConverter` class that handles web scraping and llms.txt generation.

### md2html.py  
Single-file, class-based architecture with `MarkdownToHtmlConverter` class that handles markdown parsing and HTML generation with image extraction.

## Content Processing Pipeline
The system implements a multi-stage content processing pipeline:
1. **Web Fetching**: Uses the `requests` library with session management for HTTP requests
2. **HTML Parsing**: Leverages `BeautifulSoup` for DOM manipulation and content extraction
3. **Content Cleaning**: Removes unnecessary elements like scripts, styles, navigation, headers, and footers
4. **Markdown Conversion**: Utilizes `html2text` library to convert cleaned HTML to Markdown format
5. **LLMs.txt Formatting**: Structures the output according to llms.txt specifications

## Configuration Decisions
- **No Line Wrapping**: Sets body_width to 0 to preserve original formatting
- **Link Preservation**: Maintains links in the Markdown output while ignoring images
- **User Agent Spoofing**: Uses a browser-like User-Agent string to avoid bot detection
- **Session Management**: Implements persistent HTTP sessions for better performance

## Error Handling Strategy
The architecture includes timeout mechanisms (30-second request timeout) and HTTP status validation to handle network-related failures gracefully.

# External Dependencies

## Core Libraries

### web2llms.py
- **requests**: HTTP client library for web page fetching and session management
- **html2text**: HTML to Markdown conversion engine with configurable output formatting
- **beautifulsoup4**: HTML parsing and DOM manipulation library for content extraction

### md2html.py
- **markdown**: Python Markdown parser with extensions for tables, code highlighting, and more
- **Pillow**: Python Imaging Library for processing base64 images and image format detection
- **pygments**: Syntax highlighting library for code blocks in HTML output
- **requests**: HTTP client library for downloading external images

## System Dependencies
- **argparse**: Built-in Python module for command-line argument parsing
- **datetime**: Built-in Python module for timestamp generation
- **sys/os**: Built-in Python modules for system operations and file handling
- **re**: Built-in Python module for regular expression pattern matching
- **base64**: Built-in Python module for base64 encoding/decoding
- **hashlib**: Built-in Python module for generating hash-based filenames

The application is designed to be lightweight with minimal external dependencies, focusing on reliability and ease of deployment.