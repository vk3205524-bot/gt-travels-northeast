"""
Download any additional iconic high-res photos for Northeast top landmarks.
"""
import urllib.request
import urllib.parse
import json
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

TARGETS = [
    ("c:/Users/vk320/Downloads/tourism/images/assam/kaziranga-rhino.jpg", ["Rhinoceros unicornis Kaziranga", "Indian rhinoceros Kaziranga National Park", "Kaziranga rhino"]),
    ("c:/Users/vk320/Downloads/tourism/images/arunachal/tawang-monastery-exterior.jpg", ["Tawang Monastery exterior", "Tawang Gompa Arunachal", "Tawang Monastery landscape"]),
    ("c:/Users/vk320/Downloads/tourism/images/mizoram/reiek-mountain.jpg", ["Reiek Tlang", "Reiek mountain Mizoram"]),
    ("c:/Users/vk320/Downloads/tourism/images/tripura/neermahal-lake.jpg", ["Neermahal palace Tripura", "Neermahal Rudrasagar"]),
]

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
    for filepath, terms in TARGETS:
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filepath}")
            continue
        print(f"Downloading {os.path.basename(filepath)} ... ", end="", flush=True)
        for t in terms:
            url = search_wiki(t)
            if url and download(url, filepath):
                break

if __name__ == "__main__":
    main()
