"""
Download Mizoram tourism images from Wikimedia Commons.
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

# 1. Exact file titles from user's links
EXACT_FILES = {
    "solomons-temple.jpg": "File:Solomon's Temple, Mizoram.jpg",
    "reiek-peak.jpg": "File:Reiek tlang in Mizoram, india - panoramio.jpg",
    "hmuifang.jpg": "File:Hmunchung tlang, Sialsuk, Mizoram, India - panoramio.jpg",
    "vantawng-falls.jpg": "File:Vantawng Falls, Mizoram.jpg",
    "tuirihiau-falls.jpg": "File:Tuirihiau waterfall 01.jpg",
    "champhai-valley.jpg": "File:Champhai, Aizawl.jpg",
    "rih-dil.jpg": "File:ரிடில்_ஏரி.jpg",
    "lianchhiari-tlang.jpg": "File:Lianchiari lunglen tlang.jpg",
    "lunglei.jpg": "File:Lunglei.jpg",
    "phawngpui-peak.jpg": "File:Phawngpui national park.jpg",
}

# 2. Alternative file titles
ALT_FILES = {
    "solomons-temple.jpg": "File:Solomon's Temple, Mizoram, 2025.jpg",
    "tuirihiau-falls.jpg": "File:Tuirihiau falls.jpg",
    "rih-dil.jpg": "File:Rih dil.jpg",
}

# 3. Categories
CATEGORIES = {
    "solomons-temple.jpg": "Solomon's Temple, Aizawl",
    "lunglei.jpg": "Lunglei",
    "lawngtlai.jpg": "Lawngtlai",
    "murlen-park.jpg": "Murlen National Park",
}

# 4. Search terms
SEARCH_TERMS = {
    "solomons-temple.jpg": ["Solomon's Temple Aizawl", "Solomon Temple Mizoram"],
    "reiek-peak.jpg": ["Reiek Tlang Mizoram", "Reiek peak Mizoram", "Reiek mountain"],
    "hmuifang.jpg": ["Hmuifang Mizoram", "Hmuifang Tlang", "Sialsuk Mizoram"],
    "aizawl-city.jpg": ["Aizawl city view", "Durtlang Hills Aizawl", "Aizawl skyline"],
    "falkawn-village.jpg": ["Falkawn village Mizoram", "Mizo heritage village", "Falkawn"],
    "vantawng-falls.jpg": ["Vantawng Falls Mizoram", "Vantawng Khawhthla"],
    "tuirihiau-falls.jpg": ["Tuirihiau Falls Mizoram", "Tuirihiau waterfall"],
    "thenzawl-golf.jpg": ["Thenzawl Mizoram", "Thenzawl Golf Resort", "Thenzawl town"],
    "chawngchilhi-cave.jpg": ["Chawngchilhi Puk Mizoram", "Mizoram cave", "Thenzawl handloom"],
    "champhai-valley.jpg": ["Champhai Mizoram", "Champhai valley"],
    "rih-dil.jpg": ["Rih Dil lake", "Rih Dil Mizoram", "Rih Lake"],
    "lianchhiari-tlang.jpg": ["Lianchhiari Lunglen Tlang", "Dungtlang Champhai"],
    "murlen-park.jpg": ["Murlen National Park Mizoram", "Murlen rainforest"],
    "lunglei.jpg": ["Lunglei Mizoram", "Lunglei town"],
    "lawngtlai.jpg": ["Lawngtlai Mizoram", "Lai Autonomous Council"],
    "phawngpui-peak.jpg": ["Phawngpui peak Mizoram", "Blue Mountain Mizoram", "Phawngpui National Park"],
    "dampa-reserve.jpg": ["Dampa Tiger Reserve Mizoram", "Dampa Sanctuary Mamit"],
}

FALLBACKS = {
    "thenzawl-golf.jpg": "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?w=800&q=80",
    "chawngchilhi-cave.jpg": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&q=80",
    "dampa-reserve.jpg": "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=800&q=80",
    "falkawn-village.jpg": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=800&q=80",
    "aizawl-city.jpg": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80",
}

def get_wiki_file_url(file_title, width=1200):
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
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
        for pid, pdata in pages.items():
            if pid == "-1":
                return None
            ii = pdata.get("imageinfo", [])
            if ii:
                return ii[0].get("thumburl") or ii[0].get("url")
    except Exception as e:
        pass
    return None

def get_category_image(category_name, width=1200):
    api_url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "generator": "categorymembers",
        "gcmtitle": f"Category:{category_name}",
        "gcmtype": "file",
        "gcmlimit": "10",
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "iiurlwidth": str(width),
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
                mime = ii[0].get("mime", "")
                if "image" not in mime or "svg" in mime:
                    continue
                w = ii[0].get("width", 0)
                h = ii[0].get("height", 0)
                area = w * h
                if area > best_size:
                    best_size = area
                    best_url = ii[0].get("thumburl") or ii[0].get("url")
        return best_url
    except Exception as e:
        pass
    return None

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
    print("=" * 60)
    print("Downloading Mizoram Tourism Images from Wikimedia Commons")
    print("=" * 60)

    for filename, queries in SEARCH_TERMS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename}")
            continue

        found = False
        # Exact files
        if filename in EXACT_FILES:
            title = EXACT_FILES[filename]
            print(f"  {filename} <- {title} ... ", end="", flush=True)
            url = get_wiki_file_url(title)
            if url and download(url, filepath):
                found = True

        # Alt files
        if not found and filename in ALT_FILES:
            title = ALT_FILES[filename]
            print(f"  {filename} <- {title} ... ", end="", flush=True)
            url = get_wiki_file_url(title)
            if url and download(url, filepath):
                found = True

        # Categories
        if not found and filename in CATEGORIES:
            cat = CATEGORIES[filename]
            print(f"  {filename} <- Category:{cat} ... ", end="", flush=True)
            url = get_category_image(cat)
            if url and download(url, filepath):
                found = True

        # Search terms
        if not found:
            for q in queries:
                print(f"  {filename} <- '{q}' ... ", end="", flush=True)
                url = search_wiki(q)
                if url and download(url, filepath):
                    found = True
                    break
                else:
                    print("none")
                time.sleep(0.4)

        # Fallback
        if not found:
            if filename in FALLBACKS:
                print(f"  {filename} <- fallback ... ", end="", flush=True)
                download(FALLBACKS[filename], filepath)

    print("\nAll files in images/mizoram/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f}: {size/1024:.0f} KB")

if __name__ == "__main__":
    main()
