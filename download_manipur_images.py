"""
Download Manipur destination images from Wikimedia Commons / official galleries.
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "manipur")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

# 1. Exact or high probability file titles
EXACT_FILES = {
    "loktak-lake.jpg": "File:Loktak lake, Manipur.jpg",
    "keibul-lamjao.jpg": "File:Keibul Lamjao National Park Manipur.jpg",
    "sangai-deer.jpg": "File:Sangai Manipur.jpg",
    "kangla-fort.jpg": "File:Kangla Fort, Imphal.jpg",
    "ima-keithel.jpg": "File:Ima Keithel market, Imphal, Manipur.jpg",
    "govindajee-temple.jpg": "File:Shree Govindajee Temple Imphal.jpg",
    "shirui-lily.jpg": "File:Shirui Lily.jpg",
    "ina-memorial.jpg": "File:INA Memorial, Moirang.jpg",
}

# 2. Categories
CATEGORIES = {
    "loktak-lake.jpg": "Loktak Lake",
    "keibul-lamjao.jpg": "Keibul Lamjao National Park",
    "kangla-fort.jpg": "Kangla",
    "ima-keithel.jpg": "Ima Market",
    "imphal-war-cemetery.jpg": "Imphal War Cemetery",
    "ukhrul.jpg": "Ukhrul",
    "andro-village.jpg": "Andro, Manipur",
}

# 3. Search queries
SEARCH_TERMS = {
    "loktak-lake.jpg": ["Loktak Lake Manipur", "Loktak Phumdis"],
    "sendra-island.jpg": ["Sendra Island Loktak", "Sendra Loktak Manipur", "Loktak Lake resort"],
    "keibul-lamjao.jpg": ["Keibul Lamjao National Park", "Keibul Lamjao"],
    "sangai-deer.jpg": ["Sangai deer Manipur", "Rucervus eldii eldii Manipur", "Sangai deer"],
    "ina-memorial.jpg": ["INA Memorial Moirang", "Indian National Army Moirang Manipur", "Moirang INA"],
    "kangla-fort.jpg": ["Kangla Fort Imphal Manipur", "Kangla Gate Imphal"],
    "ima-keithel.jpg": ["Ima Keithel Imphal", "Ima Market Manipur", "Mothers Market Imphal"],
    "govindajee-temple.jpg": ["Govindajee Temple Imphal", "Shree Govindajee Manipur"],
    "imphal-war-cemetery.jpg": ["Imphal War Cemetery", "Imphal WWII Cemetery"],
    "state-museum.jpg": ["Manipur State Museum Imphal", "State Museum Imphal"],
    "singda-dam.jpg": ["Singda Dam Manipur", "Singda Dam Imphal"],
    "shirui-hills.jpg": ["Shirui Kashong Ukhrul", "Shirui Hills Manipur", "Sirui Hills"],
    "shirui-lily.jpg": ["Lilium mackliniae", "Shirui Lily Manipur", "Siroy Lily"],
    "khangkhui-caves.jpg": ["Khangkhui Cave Ukhrul", "Khangkhui Mangsor Cave"],
    "ukhrul.jpg": ["Ukhrul Manipur landscape", "Ukhrul town"],
    "khongjom-memorial.jpg": ["Khongjom War Memorial Manipur", "Khongjom Memorial Thoubal"],
    "moreh-border.jpg": ["Moreh Manipur border", "Moreh town Manipur"],
    "andro-village.jpg": ["Andro Manipur", "Mutua Museum Andro"],
    "thoubal.jpg": ["Thoubal Manipur landscape", "Thoubal river Manipur"],
}

FALLBACKS = {
    "sendra-island.jpg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80",
    "singda-dam.jpg": "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=800&q=80",
    "khangkhui-caves.jpg": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&q=80",
    "thoubal.jpg": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80",
    "state-museum.jpg": "https://images.unsplash.com/photo-1564399579-3fe2b9db3e5c?w=800&q=80",
    "moreh-border.jpg": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=800&q=80",
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
    print("Downloading Manipur Tourism Images from Wikimedia Commons")
    print("=" * 60)

    for filename, queries in SEARCH_TERMS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename}")
            continue

        # Try exact file first if available
        found = False
        if filename in EXACT_FILES:
            title = EXACT_FILES[filename]
            print(f"  {filename} <- {title} ... ", end="", flush=True)
            url = get_wiki_file_url(title)
            if url and download(url, filepath):
                found = True

        # Try category
        if not found and filename in CATEGORIES:
            cat = CATEGORIES[filename]
            print(f"  {filename} <- Category:{cat} ... ", end="", flush=True)
            url = get_category_image(cat)
            if url and download(url, filepath):
                found = True

        # Try search queries
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

    print("\nAll files in images/manipur/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f}: {size/1024:.0f} KB")

if __name__ == "__main__":
    main()
