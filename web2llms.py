#!/usr/bin/env python3
"""
Web to LLMs.txt Converter
A CLI tool that converts web page content to Markdown and structures it in llms.txt format.
"""

import argparse
import requests
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import os
from datetime import datetime


class Web2LLMsConverter:
    def __init__(self):
        self.html2text_converter = html2text.HTML2Text()
        self.html2text_converter.ignore_links = False
        self.html2text_converter.ignore_images = True
        self.html2text_converter.body_width = 0  # No line wrapping
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def fetch_page_content(self, url):
        """Fetch and parse content from a web page."""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract title
            title_tag = soup.find('title')
            title = title_tag.get_text().strip() if title_tag else urlparse(url).netloc
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "header", "footer"]):
                script.decompose()
            
            # Get the main content
            html_content = str(soup)
            
            return {
                'title': title,
                'html': html_content,
                'url': url,
                'success': True
            }
        except requests.RequestException as e:
            return {
                'title': f"Failed to fetch: {url}",
                'error': str(e),
                'url': url,
                'success': False
            }
        except Exception as e:
            return {
                'title': f"Error processing: {url}",
                'error': str(e),
                'url': url,
                'success': False
            }

    def html_to_markdown(self, html_content):
        """Convert HTML content to Markdown."""
        try:
            markdown_content = self.html2text_converter.handle(html_content)
            return markdown_content.strip()
        except Exception as e:
            return f"Error converting HTML to Markdown: {str(e)}"

    def create_llms_txt_structure(self, page_data_list, project_name="Web Content Collection"):
        """Create the llms.txt structured output."""
        
        # Count successful fetches
        successful_pages = [page for page in page_data_list if page['success']]
        failed_pages = [page for page in page_data_list if not page['success']]
        
        # Start building the llms.txt content
        llms_content = []
        
        # H1 title (required)
        llms_content.append(f"# {project_name}")
        llms_content.append("")
        
        # Blockquote summary (required)
        summary = f"A collection of {len(successful_pages)} web pages converted to Markdown format"
        if failed_pages:
            summary += f", with {len(failed_pages)} failed fetches"
        summary += f". Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
        
        llms_content.append(f"> {summary}")
        llms_content.append("")
        
        # Additional context
        if failed_pages:
            llms_content.append("**Note:** Some URLs could not be fetched due to network errors or access restrictions.")
            llms_content.append("")
        
        # Create sections for successful pages
        if successful_pages:
            llms_content.append("## Converted Web Pages")
            llms_content.append("")
            
            for page in successful_pages:
                # Convert HTML to Markdown
                markdown_content = self.html_to_markdown(page['html'])
                
                # Add page section
                llms_content.append(f"### {page['title']}")
                llms_content.append("")
                llms_content.append(f"**Source:** {page['url']}")
                llms_content.append("")
                llms_content.append(markdown_content)
                llms_content.append("")
                llms_content.append("---")
                llms_content.append("")
        
        # Add failed URLs section if any
        if failed_pages:
            llms_content.append("## Failed to Fetch")
            llms_content.append("")
            for page in failed_pages:
                llms_content.append(f"- **{page['url']}**: {page['error']}")
            llms_content.append("")
        
        return "\n".join(llms_content)

    def save_to_file(self, content, filename="llms.txt"):
        """Save content to a file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, f"Content saved to {filename}"
        except Exception as e:
            return False, f"Error saving file: {str(e)}"

    def process_urls(self, urls, project_name="Web Content Collection", output_file="llms.txt"):
        """Main processing function."""
        print(f"Processing {len(urls)} URLs...")
        
        page_data_list = []
        
        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] Fetching: {url}")
            page_data = self.fetch_page_content(url)
            page_data_list.append(page_data)
            
            if page_data['success']:
                print(f"  ✓ Success: {page_data['title']}")
            else:
                print(f"  ✗ Failed: {page_data['error']}")
        
        print("\nGenerating llms.txt structure...")
        llms_content = self.create_llms_txt_structure(page_data_list, project_name)
        
        print(f"Saving to {output_file}...")
        success, message = self.save_to_file(llms_content, output_file)
        
        if success:
            print(f"✓ {message}")
        else:
            print(f"✗ {message}")
            
        return success


def main():
    parser = argparse.ArgumentParser(
        description="Convert web pages to Markdown in llms.txt format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python web2llms.py https://example.com https://github.com
  python web2llms.py -f urls.txt -o my_llms.txt -n "My Project"
  python web2llms.py --url-file urls.txt --project-name "Documentation Collection"
        """
    )
    
    # URL input options
    parser.add_argument('urls', nargs='*', help='URLs to convert (space-separated)')
    parser.add_argument('-f', '--url-file', help='File containing URLs (one per line)')
    
    # Output options
    parser.add_argument('-o', '--output', default='llms.txt', help='Output filename (default: llms.txt)')
    parser.add_argument('-n', '--project-name', default='Web Content Collection', 
                       help='Project name for H1 title (default: "Web Content Collection")')
    
    args = parser.parse_args()
    
    # Collect URLs from arguments and/or file
    urls = []
    
    if args.urls:
        urls.extend(args.urls)
    
    if args.url_file:
        try:
            with open(args.url_file, 'r', encoding='utf-8') as f:
                file_urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                urls.extend(file_urls)
        except FileNotFoundError:
            print(f"Error: URL file '{args.url_file}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading URL file: {e}")
            sys.exit(1)
    
    if not urls:
        print("Error: No URLs provided. Use command line arguments or --url-file option.")
        parser.print_help()
        sys.exit(1)
    
    # Validate URLs
    valid_urls = []
    for url in urls:
        if url.startswith(('http://', 'https://')):
            valid_urls.append(url)
        else:
            print(f"Warning: Skipping invalid URL: {url}")
    
    if not valid_urls:
        print("Error: No valid URLs found.")
        sys.exit(1)
    
    # Process URLs
    converter = Web2LLMsConverter()
    success = converter.process_urls(valid_urls, args.project_name, args.output)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()