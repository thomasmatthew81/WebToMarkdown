#!/usr/bin/env python3
"""
Markdown to HTML Converter
A CLI tool that converts Markdown to beautiful HTML with image extraction.
"""

import argparse
import requests
import sys
import os
from datetime import datetime
import re
import base64
import hashlib
from pathlib import Path
import markdown
from PIL import Image
from io import BytesIO


class MarkdownToHtmlConverter:
    """Convert Markdown to beautiful HTML with image extraction."""
    
    def __init__(self, assets_dir="assets"):
        self.assets_dir = assets_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.image_counter = 0
        self.extracted_images = []
    
    def get_css_template(self):
        """Return beautiful CSS styling for the HTML."""
        return """
        <style>
            * {
                box-sizing: border-box;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 900px;
                margin: 0 auto;
                padding: 2rem;
                background: #f5f5f5;
            }
            .content {
                background: white;
                padding: 3rem;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1, h2, h3, h4, h5, h6 {
                margin-top: 2rem;
                margin-bottom: 1rem;
                font-weight: 600;
                line-height: 1.3;
                color: #1a1a1a;
            }
            h1 {
                font-size: 2.5rem;
                border-bottom: 3px solid #3b82f6;
                padding-bottom: 0.5rem;
                margin-top: 0;
            }
            h2 {
                font-size: 2rem;
                border-bottom: 2px solid #e5e7eb;
                padding-bottom: 0.3rem;
            }
            h3 { font-size: 1.5rem; }
            h4 { font-size: 1.25rem; }
            p {
                margin-bottom: 1rem;
                text-align: justify;
            }
            img {
                max-width: 100%;
                height: auto;
                border-radius: 4px;
                margin: 1.5rem 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            code {
                background: #f3f4f6;
                padding: 0.2rem 0.4rem;
                border-radius: 3px;
                font-family: 'Courier New', Courier, monospace;
                font-size: 0.9em;
                color: #e83e8c;
            }
            pre {
                background: #1e293b;
                color: #e2e8f0;
                padding: 1.5rem;
                border-radius: 6px;
                overflow-x: auto;
                margin: 1.5rem 0;
            }
            pre code {
                background: transparent;
                padding: 0;
                color: inherit;
                font-size: 0.9rem;
            }
            blockquote {
                border-left: 4px solid #3b82f6;
                padding-left: 1.5rem;
                margin: 1.5rem 0;
                color: #6b7280;
                font-style: italic;
                background: #f9fafb;
                padding: 1rem 1.5rem;
                border-radius: 0 4px 4px 0;
            }
            a {
                color: #3b82f6;
                text-decoration: none;
                border-bottom: 1px solid transparent;
                transition: border-color 0.2s;
            }
            a:hover {
                border-bottom-color: #3b82f6;
            }
            ul, ol {
                margin-bottom: 1rem;
                padding-left: 2rem;
            }
            li {
                margin-bottom: 0.5rem;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                margin: 1.5rem 0;
                background: white;
            }
            th, td {
                border: 1px solid #e5e7eb;
                padding: 0.75rem;
                text-align: left;
            }
            th {
                background: #f3f4f6;
                font-weight: 600;
            }
            tr:hover {
                background: #f9fafb;
            }
            hr {
                border: none;
                border-top: 2px solid #e5e7eb;
                margin: 2rem 0;
            }
            .meta {
                color: #6b7280;
                font-size: 0.9rem;
                border-top: 1px solid #e5e7eb;
                margin-top: 3rem;
                padding-top: 1rem;
            }
        </style>
        """
    
    def extract_image_from_base64(self, base64_data, image_format=None):
        """Extract image from base64 data URI and save to file."""
        try:
            if ',' in base64_data:
                header, data = base64_data.split(',', 1)
                if not image_format and 'image/' in header:
                    image_format = header.split('image/')[-1].split(';')[0]
            else:
                data = base64_data
            
            image_bytes = base64.b64decode(data)
            
            if not image_format:
                img = Image.open(BytesIO(image_bytes))
                image_format = img.format.lower() if img.format else 'png'
            
            image_hash = hashlib.md5(image_bytes).hexdigest()[:12]
            filename = f"image_{image_hash}.{image_format}"
            filepath = os.path.join(self.assets_dir, filename)
            
            os.makedirs(self.assets_dir, exist_ok=True)
            
            with open(filepath, 'wb') as f:
                f.write(image_bytes)
            
            self.extracted_images.append(filepath)
            return filename
            
        except Exception as e:
            print(f"  ✗ Error extracting base64 image: {e}")
            return None
    
    def download_external_image(self, url):
        """Download external image and save to assets folder."""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            content_type = response.headers.get('content-type', '')
            if 'image' not in content_type:
                print(f"  ! Skipping non-image URL: {url}")
                return None
            
            image_format = content_type.split('/')[-1].split(';')[0]
            if image_format == 'jpeg':
                image_format = 'jpg'
            
            image_hash = hashlib.md5(response.content).hexdigest()[:12]
            filename = f"image_{image_hash}.{image_format}"
            filepath = os.path.join(self.assets_dir, filename)
            
            os.makedirs(self.assets_dir, exist_ok=True)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            self.extracted_images.append(filepath)
            print(f"  ✓ Downloaded: {url[:50]}... → {filename}")
            return filename
            
        except Exception as e:
            print(f"  ✗ Failed to download {url}: {e}")
            return None
    
    def copy_local_image(self, image_path, base_path="."):
        """Copy local image to assets folder."""
        try:
            source_path = os.path.join(base_path, image_path) if not os.path.isabs(image_path) else image_path
            
            if not os.path.exists(source_path):
                print(f"  ✗ Local image not found: {source_path}")
                return None
            
            filename = os.path.basename(image_path)
            filepath = os.path.join(self.assets_dir, filename)
            
            os.makedirs(self.assets_dir, exist_ok=True)
            
            with open(source_path, 'rb') as src, open(filepath, 'wb') as dst:
                dst.write(src.read())
            
            self.extracted_images.append(filepath)
            print(f"  ✓ Copied: {image_path} → {filename}")
            return filename
            
        except Exception as e:
            print(f"  ✗ Failed to copy {image_path}: {e}")
            return None
    
    def process_images_in_markdown(self, markdown_content, base_path="."):
        """Extract all images from markdown and return updated markdown."""
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        def replace_image(match):
            alt_text = match.group(1)
            image_src = match.group(2)
            
            if image_src.startswith('data:image'):
                filename = self.extract_image_from_base64(image_src)
            elif image_src.startswith(('http://', 'https://')):
                filename = self.download_external_image(image_src)
            else:
                filename = self.copy_local_image(image_src, base_path)
            
            if filename:
                return f'![{alt_text}]({self.assets_dir}/{filename})'
            else:
                return match.group(0)
        
        return re.sub(image_pattern, replace_image, markdown_content)
    
    def convert_to_html(self, markdown_content, title="Converted Document", base_path="."):
        """Convert markdown to beautiful HTML with extracted images."""
        print("Processing images in markdown...")
        processed_markdown = self.process_images_in_markdown(markdown_content, base_path)
        
        print("Converting markdown to HTML...")
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'fenced_code'])
        html_body = md.convert(processed_markdown)
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {self.get_css_template()}
</head>
<body>
    <div class="content">
        {html_body}
        <div class="meta">
            <p>Generated on {timestamp}</p>
            {f'<p>Extracted {len(self.extracted_images)} image(s)</p>' if self.extracted_images else ''}
        </div>
    </div>
</body>
</html>"""
        
        return html_template
    
    def convert_file(self, markdown_file, output_html=None, title=None, assets_dir=None):
        """Convert markdown file to HTML."""
        try:
            if assets_dir:
                self.assets_dir = assets_dir
            
            base_path = os.path.dirname(os.path.abspath(markdown_file))
            
            with open(markdown_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            if not title:
                title = os.path.splitext(os.path.basename(markdown_file))[0].replace('_', ' ').title()
            
            if not output_html:
                output_html = os.path.splitext(markdown_file)[0] + '.html'
            
            html_content = self.convert_to_html(markdown_content, title, base_path)
            
            with open(output_html, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return True, output_html
            
        except FileNotFoundError:
            return False, f"Markdown file not found: {markdown_file}"
        except Exception as e:
            return False, f"Error converting file: {str(e)}"


def main():
    parser = argparse.ArgumentParser(
        description="Convert Markdown to beautiful HTML with image extraction",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python md2html.py document.md
  python md2html.py README.md -o index.html -t "My Project"
  python md2html.py content.md --assets-dir images --title "Documentation"
        """
    )
    
    parser.add_argument('markdown_file', help='Markdown file to convert')
    parser.add_argument('-o', '--output', help='Output HTML filename (default: same as input with .html extension)')
    parser.add_argument('-t', '--title', help='HTML page title (default: derived from filename)')
    parser.add_argument('-a', '--assets-dir', default='assets', help='Directory for extracted images (default: assets)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.markdown_file):
        print(f"Error: Markdown file '{args.markdown_file}' not found.")
        sys.exit(1)
    
    print(f"Converting {args.markdown_file} to HTML...")
    
    converter = MarkdownToHtmlConverter(assets_dir=args.assets_dir)
    success, result = converter.convert_file(
        args.markdown_file,
        output_html=args.output,
        title=args.title,
        assets_dir=args.assets_dir
    )
    
    if success:
        print(f"✓ HTML saved to: {result}")
        if converter.extracted_images:
            print(f"✓ Extracted {len(converter.extracted_images)} image(s) to {args.assets_dir}/")
        print("\nDone!")
    else:
        print(f"✗ {result}")
        sys.exit(1)


if __name__ == "__main__":
    main()
