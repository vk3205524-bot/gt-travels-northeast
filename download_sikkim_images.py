"""
Download Sikkim destination images from Wikimedia Commons.
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "sikkim")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

# 1. Exact or high probability file titles from user's links
EXACT_FILES = {
    "gurudongmar-lake.jpg": "File:Gurudongmar Lake Sikkim, India (edit).jpg",
    "zero-point.jpg": "File:Zero point at Sikkim.jpg",
    "rabdentse-ruins.jpg": "File:Rabdentse ruins.jpg",
    "buddha-park-ravangla.jpg": "File:Buddha Park of Ravangla, Sikkim.jpg",
    "samdruptse.jpg": "File:The monument of Guru Padma Sambhava or Samdruptse.jpg",
    "temi-tea-garden.jpg": "File:Temi Tea Garden.JPG",
}

# 2. Alternative file titles
ALT_FILES = {
    "gurudongmar-lake.jpg": "File:Gurudongmar Lake, Sikkim , India.jpg",
    "rabdentse-ruins.jpg": "File:Ruins of Rabdentse, second capital of Sikkim near Pelling, West Sikkim 02.jpg",
    "samdruptse.jpg": "File:Samdruptse Sikkim.jpg",
}

# 3. Categories from user's links
CATEGORIES = {
    "gangtok.jpg": "Gangtok",
    "lachen.jpg": "Lachen",
    "lachung.jpg": "Lachung",
    "yumthang-valley.jpg": "Yumthang_Valley_of_Flowers",
    "rumtek-monastery.jpg": "Rumtek_Monastery",
    "tsomgo-lake.jpg": "Tsomgo_Lake",
    "nathula-pass.jpg": "Nathu_La",
    "pelling-skywalk.jpg": "Chenrezig_statue_and_skywalk",
    "pemayangtse.jpg": "Pemayangtse_Monastery",
    "khecheopalri-lake.jpg": "Khecheopalri_Lake",
    "yuksom.jpg": "Yuksom",
    "temi-tea-garden.jpg": "Temi_Tea_Garden",
    "buddha-park-ravangla.jpg": "Buddha_Park_of_Ravangla",
    "char-dham-namchi.jpg": "Char_Dham",
}

# 4. Search queries
SEARCH_TERMS = {
    "gurudongmar-lake.jpg": ["Gurudongmar Lake Sikkim", "Gurudongmar Lake"],
    "lachen.jpg": ["Lachen Sikkim village", "Lachen North Sikkim"],
    "lachung.jpg": ["Lachung Sikkim village", "Lachung North Sikkim"],
    "yumthang-valley.jpg": ["Yumthang Valley Sikkim", "Yumthang Valley of Flowers"],
    "zero-point.jpg": ["Zero Point Sikkim", "Yumesamdong Sikkim"],
    "gangtok.jpg": ["Gangtok city view", "MG Marg Gangtok"],
    "rumtek-monastery.jpg": ["Rumtek Monastery Sikkim", "Dharma Chakra Centre Rumtek"],
    "tsomgo-lake.jpg": ["Tsomgo Lake Sikkim", "Changu Lake Sikkim"],
    "baba-mandir.jpg": ["Baba Mandir Sikkim", "Baba Harbhajan Singh Temple Sikkim", "Nathu La Baba Mandir"],
    "nathula-pass.jpg": ["Nathu La Pass Sikkim", "Nathu La border Sikkim"],
    "pelling-skywalk.jpg": ["Pelling Skywalk Sikkim", "Chenrezig statue Pelling"],
    "rabdentse-ruins.jpg": ["Rabdentse ruins Pelling", "Rabdentse Sikkim"],
    "pemayangtse.jpg": ["Pemayangtse Monastery Sikkim", "Pemayangtse Pelling"],
    "khecheopalri-lake.jpg": ["Khecheopalri Lake Sikkim", "Khecheopalri wishing lake"],
    "yuksom.jpg": ["Yuksom Sikkim coronation throne", "Yuksom West Sikkim"],
    "temi-tea-garden.jpg": ["Temi Tea Garden Sikkim", "Temi Tea Estate"],
    "buddha-park-ravangla.jpg": ["Buddha Park Ravangla Sikkim", "Tathagata Tsal Ravangla"],
    "char-dham-namchi.jpg": ["Char Dham Namchi Sikkim", "Siddhesvara Dhaam Namchi", "Namchi Shiva statue"],
    "samdruptse.jpg": ["Samdruptse Namchi Sikkim", "Guru Padmasambhava Samdruptse"],
}

FALLBACKS = {
    "baba-mandir.jpg": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?w=800&q=80",
    "zero-point.jpg": "https://images.unsplash.com/photo-1517824806704-9040b037703b?w=800&q=80",
    "lachen.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&q=80",
    "yuksom.jpg": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80",
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
    print("Downloading Sikkim Tourism Images from Wikimedia Commons")
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
        if not found and filename in FALLBACKS:
            print(f"  {filename} <- fallback ... ", end="", flush=True)
            download(FALLBACKS[filename], filepath)

    print("\nAll files in images/sikkim/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f}: {size/1024:.0f} KB")

if __name__ == "__main__":
    main()
