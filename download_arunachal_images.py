"""
Download Arunachal Pradesh destination images from Wikimedia Commons.
Uses the MediaWiki API to resolve direct image URLs, then downloads them.
"""
import urllib.request
import urllib.parse
import json
import os
import time
import ssl

# Disable SSL verification for problematic certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "arunachal")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Map: filename -> Wikimedia Commons file title
# These are verified Wikimedia Commons file names
WIKI_IMAGES = {
    # Tawang Circuit
    "tawang-monastery.jpg": "File:Tawang Monastery.jpg",
    "sela-pass.jpg": "File:Sela Pass, Arunachal Pradesh.jpg",
    "bum-la-pass.jpg": "File:Bum la pass.JPG",
    "nuranang-falls.jpg": "File:Nuranang Falls.jpg",
    "dirang.jpg": "File:Dirang Dzong.jpg",
    "bomdila.jpg": "File:Bomdila Monastery.JPG",
    # Ziro Valley
    "ziro-valley.jpg": "File:Ziro Valley Arunachal Pradesh.jpg",
    "apatani-village.jpg": "File:Apatani tribal woman.jpg",
    "talley-valley.jpg": "File:Talley Valley Wildlife Sanctuary.jpg",
    "itanagar.jpg": "File:Ita Fort, Itanagar.jpg",
    # Mechuka
    "mechuka-valley.jpg": "File:Mechuka valley, Arunachal Pradesh, India.jpg",
    "pasighat.jpg": "File:Pasighat City Skyline.jpg",
    # Eastern / Golden Pagoda
    "golden-pagoda.jpg": "File:Golden Pagoda Namsai.jpg",
    "mayodia-pass.jpg": "File:Mayodia Pass.jpg",
    "parasuram-kund.jpg": "File:Parshuram Kund.jpg",
}

# Alternative search terms if exact files don't exist
FALLBACK_SEARCHES = {
    "madhuri-lake.jpg": "Madhuri Lake Tawang",
    "siyom-river.jpg": "Siyom River Mechuka",
    "samten-yongcha.jpg": "Samten Yongcha Monastery Mechuka",
    "aalo.jpg": "Along Arunachal Pradesh",
    "dong-valley.jpg": "Dong Valley Arunachal Pradesh",
    "roing.jpg": "Roing Arunachal Pradesh",
    "namsai.jpg": "Namsai Arunachal Pradesh",
}

def get_wiki_image_url(file_title, width=1200):
    """Get direct URL for a Wikimedia Commons image."""
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": file_title,
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": str(width),
        "format": "json",
    }
    url = api_url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"
    })
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            if page_id == "-1":
                return None
            imageinfo = page_data.get("imageinfo", [])
            if imageinfo:
                # Prefer thumbnail (resized) URL, fallback to original
                return imageinfo[0].get("thumburl") or imageinfo[0].get("url")
    except Exception as e:
        print(f"  API error for {file_title}: {e}")
    return None

def search_wiki_image(search_term, width=1200):
    """Search Wikimedia Commons for an image matching the search term."""
    api_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {search_term}",
        "gsrnamespace": "6",
        "gsrlimit": "3",
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": str(width),
        "format": "json",
    }
    url = api_url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"
    })
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_data in pages.items():
            imageinfo = page_data.get("imageinfo", [])
            if imageinfo:
                return imageinfo[0].get("thumburl") or imageinfo[0].get("url")
    except Exception as e:
        print(f"  Search error for '{search_term}': {e}")
    return None

def download_image(url, filepath):
    """Download an image from URL to filepath."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"
    })
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
        with open(filepath, "wb") as f:
            f.write(data)
        size_kb = len(data) / 1024
        print(f"  OK  ({size_kb:.0f} KB)")
        return True
    except Exception as e:
        print(f"  DOWNLOAD FAILED: {e}")
        return False

def main():
    print("=" * 60)
    print("Downloading Arunachal Pradesh Images from Wikimedia Commons")
    print("=" * 60)
    
    downloaded = 0
    failed = []
    
    # Phase 1: Download from known Wikimedia file titles
    print("\n--- Phase 1: Known Wikimedia file titles ---")
    for filename, file_title in WIKI_IMAGES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename} (already exists)")
            downloaded += 1
            continue
        
        print(f"Resolving {filename} <- {file_title} ... ", end="", flush=True)
        url = get_wiki_image_url(file_title)
        if url:
            if download_image(url, filepath):
                downloaded += 1
            else:
                failed.append(filename)
        else:
            print("  NOT FOUND on Wiki, will try search...")
            failed.append(filename)
        time.sleep(0.5)  # Rate limiting
    
    # Phase 2: Search-based fallbacks
    print("\n--- Phase 2: Search-based downloads ---")
    for filename, search_term in FALLBACK_SEARCHES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename} (already exists)")
            downloaded += 1
            continue
        
        print(f"Searching {filename} <- '{search_term}' ... ", end="", flush=True)
        url = search_wiki_image(search_term)
        if url:
            if download_image(url, filepath):
                downloaded += 1
            else:
                failed.append(filename)
        else:
            print("  NO RESULTS")
            failed.append(filename)
        time.sleep(0.5)
    
    # Phase 3: Retry failed Phase 1 items with search
    retry = [f for f in failed if f in WIKI_IMAGES]
    if retry:
        print("\n--- Phase 3: Retry failed items with search ---")
        for filename in retry:
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
                continue
            # Extract search term from filename
            search = filename.replace(".jpg", "").replace("-", " ").title() + " Arunachal Pradesh"
            print(f"Searching {filename} <- '{search}' ... ", end="", flush=True)
            url = search_wiki_image(search)
            if url:
                if download_image(url, filepath):
                    downloaded += 1
                    failed.remove(filename)
            else:
                print("  NO RESULTS")
            time.sleep(0.5)
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Downloaded: {downloaded}")
    if failed:
        still_missing = [f for f in failed if not (os.path.exists(os.path.join(OUTPUT_DIR, f)) and os.path.getsize(os.path.join(OUTPUT_DIR, f)) > 5000)]
        if still_missing:
            print(f"Still missing: {still_missing}")
    
    # List all files
    print("\nFiles in images/arunachal/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f} ({size/1024:.0f} KB)")

if __name__ == "__main__":
    main()
