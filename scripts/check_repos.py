#!/usr/bin/env python3
import urllib.request
import urllib.error
import re
import sys
import time
from urllib.parse import urlparse

def extract_github_urls(file_path):
    """Extract GitHub URLs from the README file"""
    urls = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find all GitHub URLs
        pattern = r'https://github\.com/[^\s\)]+(?!/actions)'
        matches = re.findall(pattern, content)
        for match in matches:
            # Clean up the URL (remove trailing punctuation)
            cleaned_url = re.sub(r'[.,;)\]]+$', '', match)
            urls.append(cleaned_url)
    return list(set(urls))  # Remove duplicates

def check_github_repo(url):
    """Check if a GitHub repository is accessible"""
    try:
        # Create request with headers
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        )

        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                return True, "OK"
            else:
                return False, f"Error ({response.status})"

    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, "Not Found (404)"
        elif e.code == 403:
            return None, "Forbidden (403) - Rate Limited or Private"
        else:
            return False, f"HTTP Error ({e.code})"
    except urllib.error.URLError as e:
        return False, f"URL Error: {str(e)}"
    except Exception as e:
        return False, f"Request failed: {str(e)}"

def main():
    readme_path = '/Users/mingcheng/Temp/awesome-ospo/README.md'
    urls = extract_github_urls(readme_path)

    print(f"Found {len(urls)} unique GitHub URLs to check:")
    print()

    dead_urls = []
    uncertain_urls = []

    for i, url in enumerate(urls):
        print(f"Checking {i+1}/{len(urls)}: {url}")
        is_accessible, status = check_github_repo(url)

        if is_accessible is False:
            print(f"  ❌ DEAD: {status}")
            dead_urls.append((url, status))
        elif is_accessible is None:
            print(f"  ⚠️  UNCERTAIN: {status}")
            uncertain_urls.append((url, status))
        else:
            print(f"  ✅ OK")

        # Add a small delay to avoid rate limiting
        time.sleep(0.5)

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    if dead_urls:
        print(f"\nDEAD REPOSITORIES ({len(dead_urls)}):")
        for url, status in dead_urls:
            print(f"  - {url} ({status})")

    if uncertain_urls:
        print(f"\nUNCERTAIN REPOSITORIES ({len(uncertain_urls)}):")
        for url, status in uncertain_urls:
            print(f"  - {url} ({status})")

    if not dead_urls and not uncertain_urls:
        print("\n✅ All repositories are accessible!")

if __name__ == "__main__":
    main()
