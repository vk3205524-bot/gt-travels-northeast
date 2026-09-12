"""Download remaining missing Arunachal images using broader searches and Unsplash fallback."""
import urllib.request
import urllib.parse
import json
import os
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "arunachal")

# Try multiple search terms for each missing image
MISSING = {
    "parasuram-kund.jpg": [
        "Parshuram Kund Lohit",
        "Parasuram Kund pilgrimage",
        "Parashuram Kund Arunachal",
    ],
    "siyom-river.jpg": [
        "Siyom River",
        "Siang River Arunachal Pradesh",
        "Yomgo River Mechuka",
    ],
    "samten-yongcha.jpg": [
        "Samten Yongcha Monastery",
        "Mechuka Monastery",
        "Buddhist monastery Mechuka",
    ],
    "dong-valley.jpg": [
        "Dong village sunrise India",
        "Dong Arunachal Pradesh sunrise",
        "Anjaw district Arunachal Pradesh",
    ],
}

# Unsplash fallbacks (free, high-quality)
UNSPLASH_FALLBACKS = {
    "parasuram-kund.jpg": "https://images.unsplash.com/photo-1590077428593-a55bb07c4665?w=800&q=80",  # Hindu pilgrimage river
    "siyom-river.jpg": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=800&q=80",  # Mountain river
    "samten-yongcha.jpg": "https://images.unsplash.com/photo-1564399579-3fe2b9db3e5c?w=800&q=80",  # Buddhist monastery
    "dong-valley.jpg": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?w=800&q=80",  # Sunrise valley
}

def search_wiki(search_term, width=1200):
    api_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {search_term}",
        "gsrnamespace": "6",
        "gsrlimit": "5",
        "prop": "imageinfo",
        "iiprop": "url|size",
        "iiurlwidth": str(width),
        "format": "json",
    }
    url = api_url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
        # Pick the largest image
        best_url = None
        best_size = 0
        for pid, pdata in pages.items():
            ii = pdata.get("imageinfo", [])
            if ii:
                size = ii[0].get("size", 0)
                thumb = ii[0].get("thumburl") or ii[0].get("url")
                if size > best_size and thumb:
                    best_url = thumb
                    best_size = size
        return best_url
    except Exception as e:
        print(f"    Search error: {e}")
    return None

def download(url, filepath):
    req = urllib.request.Request(url, headers={"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
        with open(filepath, "wb") as f:
            f.write(data)
        print(f"  OK ({len(data)/1024:.0f} KB)")
        return True
    except Exception as e:
        print(f"  FAILED: {e}")
        return False

def main():
    print("Downloading remaining missing Arunachal images...")
    
    for filename, searches in MISSING.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename} (already exists)")
            continue
        
        found = False
        for term in searches:
            print(f"  Trying '{term}'... ", end="", flush=True)
            url = search_wiki(term)
            if url:
                if download(url, filepath):
                    found = True
                    break
            else:
                print("  no results")
            time.sleep(0.5)
        
        if not found:
            # Use Unsplash fallback
            fallback_url = UNSPLASH_FALLBACKS.get(filename)
            if fallback_url:
                print(f"  Using Unsplash fallback for {filename}... ", end="", flush=True)
                download(fallback_url, filepath)
    
    # Verify all files
    print("\nFinal file listing:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        status = "OK" if size > 5000 else "TOO SMALL"
        print(f"  {f}: {size/1024:.0f} KB [{status}]")

if __name__ == "__main__":
    main()
