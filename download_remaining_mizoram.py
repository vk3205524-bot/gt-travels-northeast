"""
Download remaining Mizoram images safely without Unicode printing issues.
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "mizoram")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

REMAINING = {
    "rih-dil.jpg": ["Rih Dil", "Rih Lake Mizoram", "Rih dil"],
    "lianchhiari-tlang.jpg": ["Lianchiari lunglen tlang", "Lianchhiari Tlang", "Dungtlang Champhai"],
    "murlen-park.jpg": ["Murlen National Park", "Murlen Mizoram"],
    "lunglei.jpg": ["Lunglei", "Lunglei town Mizoram"],
    "lawngtlai.jpg": ["Lawngtlai", "Lawngtlai Mizoram"],
    "phawngpui-peak.jpg": ["Phawngpui national park", "Phawngpui Mizoram", "Blue Mountain Mizoram"],
    "dampa-reserve.jpg": ["Dampa Tiger Reserve", "Dampa Wildlife Sanctuary"],
}

FALLBACKS = {
    "dampa-reserve.jpg": "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=800&q=80",
    "murlen-park.jpg": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=800&q=80",
    "lawngtlai.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&q=80",
    "lianchhiari-tlang.jpg": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80",
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
        pass
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
    for filename, terms in REMAINING.items():
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
            time.sleep(0.4)

        if not found and filename in FALLBACKS:
            print(f"Fallback {filename} ... ", end="", flush=True)
            download(FALLBACKS[filename], filepath)

    print("\nAll files in images/mizoram/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f}: {size/1024:.0f} KB")

if __name__ == "__main__":
    main()
