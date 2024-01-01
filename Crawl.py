import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl(url, depth, visited, output_dir):
    if depth == 0 or url in visited:
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        save_html(url, response.text, output_dir)

        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            crawl(next_url, depth - 1, visited, output_dir)

    except Exception as e:
        print(f"Error crawling {url}: {e}")

    finally:
        visited.add(url)

def save_html(url, content, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    parsed_url = urlparse(url)
    filename = parsed_url.netloc + parsed_url.path
    filename = filename.replace('/', '_')  
    filename = os.path.join(output_dir, filename + ".html")

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f'Saved HTML from {url} to {filename}')

if __name__ == "__main__":
    start_url = "https://example.com"  
    max_depth = 3  
    visited_urls = set()  
    output_directory = './html'  

    crawl(start_url, max_depth, visited_urls, output_directory)

