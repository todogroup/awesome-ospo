#!/usr/bin/env python3
import urllib.request
import urllib.error
import re
import sys
import time
from urllib.parse import urlparse

def extract_all_urls(file_path):
    """Extract all URLs from the README file"""
    urls = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find all HTTP and HTTPS URLs
        pattern = r'https?://[^\s\)\]]+(?<![.,;:)])'
        matches = re.findall(pattern, content)
        for match in matches:
            # Clean up the URL (remove trailing punctuation)
            cleaned_url = re.sub(r'[.,;:)\]]+$', '', match)
            urls.append(cleaned_url)
    return list(set(urls))  # Remove duplicates

def check_url_availability(url):
    """Check if a URL is accessible"""
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
        elif e.code == 301 or e.code == 302:
            return True, f"Redirect ({e.code})"
        else:
            return False, f"HTTP Error ({e.code})"
    except urllib.error.URLError as e:
        return False, f"URL Error: {str(e)}"
    except Exception as e:
        return False, f"Request failed: {str(e)}"

def main():
    readme_path = '/Users/mingcheng/Temp/awesome-ospo/README.md'
    urls = extract_all_urls(readme_path)

    print(f"Found {len(urls)} unique URLs to check:")
    print()

    dead_urls = []
    uncertain_urls = []
    working_urls = []

    for i, url in enumerate(urls):
        print(f"Checking {i+1}/{len(urls)}: {url}")
        is_accessible, status = check_url_availability(url)

        if is_accessible is False:
            print(f"  ❌ DEAD: {status}")
            dead_urls.append((url, status))
        elif is_accessible is None:
            print(f"  ⚠️  UNCERTAIN: {status}")
            uncertain_urls.append((url, status))
        else:
            print(f"  ✅ OK: {status}")
            working_urls.append((url, status))

        # Add a small delay to avoid rate limiting
        time.sleep(0.5)

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)

    print(f"\nWORKING URLS ({len(working_urls)}):")
    for url, status in working_urls[:5]:  # Show first 5
        print(f"  ✅ {url} ({status})")
    if len(working_urls) > 5:
        print(f"  ... and {len(working_urls) - 5} more working URLs")

    if dead_urls:
        print(f"\n🚨 DEAD URLs ({len(dead_urls)}):")
        for url, status in dead_urls:
            print(f"  ❌ {url} ({status})")

    if uncertain_urls:
        print(f"\n⚠️  UNCERTAIN URLs ({len(uncertain_urls)}):")
        for url, status in uncertain_urls:
            print(f"  ⚠️  {url} ({status})")

    if not dead_urls and not uncertain_urls:
        print("\n✅ All URLs are accessible!")

    # Print results that need action
    if dead_urls:
        print(f"\n{'='*80}")
        print("URLs THAT NEED TO BE MARKED WITH STRIKETHROUGH:")
        print("="*80)
        for url, status in dead_urls:
            print(f"- {url}")

if __name__ == "__main__":
    main()
