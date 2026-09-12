"""
Download remaining 4 Nagaland images with broader queries or curated fallbacks.
"""
import urllib.request
import urllib.parse
import json
import os
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "nagaland")
HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

SEARCHES = {
    "shangnyu.jpg": ["Shangnyu", "Konyak Naga village", "Konyak tribe Nagaland"],
    "ungma.jpg": ["Ungma Nagaland", "Ao Naga festival", "Ao Naga village", "Mokokchung village"],
    "longkhum.jpg": ["Longkhum Nagaland", "Ao Naga landscape", "Mokokchung hills"],
    "ntangki.jpg": ["Ntangki Nagaland", "Intanki Nagaland", "Peren Nagaland", "Hoolock gibbon Nagaland"],
}

FALLBACKS = {
    "shangnyu.jpg": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&q=80",
    "ungma.jpg": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=800&q=80",
    "longkhum.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&q=80",
    "ntangki.jpg": "https://images.unsplash.com/photo-1534567153574-2b12153a87f0?w=800&q=80",
}

def search_wiki(term):
    api_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {term}",
        "gsrnamespace": "6",
        "gsrlimit": "5",
        "prop": "imageinfo",
        "iiprop": "url|size",
        "iiurlwidth": "1200",
        "format": "json",
    }
    url = api_url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
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
        print(f"Error: {e}")
    return None

def download(url, filepath):
    req = urllib.request.Request(url, headers=HEADERS)
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
    for filename, terms in SEARCHES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename}")
            continue
        found = False
        for term in terms:
            print(f"Searching {filename} <- '{term}' ... ", end="", flush=True)
            url = search_wiki(term)
            if url and download(url, filepath):
                found = True
                break
            else:
                print("none")
            time.sleep(0.5)
        if not found:
            print(f"Using curated fallback for {filename} ... ", end="", flush=True)
            download(FALLBACKS[filename], filepath)

    print("\nAll files in images/nagaland/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f}: {size/1024:.0f} KB")

if __name__ == "__main__":
    main()
