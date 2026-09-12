"""
Download Nagaland destination images from Wikimedia Commons.
Uses specific file titles and category members provided by user.
"""
import urllib.request
import urllib.parse
import json
import os
import time
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "nagaland")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

# 1. Exact file titles from user's links
EXACT_FILES = {
    "kisama.jpg": "File:Kisama Heritage Village, Nagaland, 2024.jpg",
    "khonoma.jpg": "File:Khonoma village, Nagaland, India.jpg",
    "dzukou-valley.jpg": "File:Dzukou valley in the Nagaland-Manipur border.jpg",
    "longwa.jpg": "File:Headhhunter at Longwa, Nagaland.jpg",
    "wokha-doyang.jpg": "File:Doyang reservoir and its suroundings in Nagaland JEG4572.JPG",
    "mokokchung.jpg": "File:Mokokchung town.jpg",
    "shilloi-lake.jpg": "File:Shilloi lake Phek Nagaland.jpg",
}

# 2. Alternative file titles
ALT_FILES = {
    "dzukou-valley.jpg": "File:Dzukou Valley1.jpg",
    "longwa.jpg": "File:A headhunter in longwa village, nagaland.jpg",
    "wokha-doyang.jpg": "File:Doyang Dam wokha Nagaland.jpg",
    "shilloi-lake.jpg": "File:Shilloi lake, Meluri.jpg",
    "kohima.jpg": "File:View of Kohima.jpg",
    "dimapur.jpg": "File:Kachari Ruins Dimapur.jpg",
}

# 3. Category based lookups
CATEGORIES = {
    "dimapur.jpg": "Dimapur",
    "kohima.jpg": "Kohima",
    "kisama.jpg": "Kisama Heritage Village",
    "khonoma.jpg": "Khonoma",
    "pfutsero.jpg": "Pfütsero",
    "mon.jpg": "Mon district",
}

# 4. Search terms for remaining places
SEARCH_TERMS = {
    "dimapur.jpg": "Kachari Ruins Dimapur Nagaland",
    "kohima.jpg": "Kohima Nagaland landscape",
    "kisama.jpg": "Kisama Heritage Village Nagaland",
    "khonoma.jpg": "Khonoma village Nagaland",
    "dzukou-valley.jpg": "Dzukou Valley Nagaland",
    "mon.jpg": "Mon district Nagaland",
    "longwa.jpg": "Longwa village Mon Nagaland",
    "shangnyu.jpg": "Shangnyu Mon Nagaland",
    "wokha-doyang.jpg": "Doyang reservoir Wokha Nagaland",
    "mokokchung.jpg": "Mokokchung Nagaland",
    "ungma.jpg": "Ungma village Mokokchung Nagaland",
    "longkhum.jpg": "Longkhum village Mokokchung Nagaland",
    "ntangki.jpg": "Ntangki National Park Nagaland",
    "pfutsero.jpg": "Pfutsero Nagaland",
    "shilloi-lake.jpg": "Shilloi Lake Phek Nagaland",
}

def get_wiki_file_url(file_title, width=1200):
    """Get direct thumbnail URL for a Wikimedia Commons file."""
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
        print(f"    API error for {file_title}: {e}")
    return None

def get_category_image(category_name, width=1200):
    """Get the largest image from a category."""
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
        print(f"    Category error for {category_name}: {e}")
    return None

def search_wiki(search_term, width=1200):
    """Search Wikimedia Commons for an image."""
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
        print(f"    Search error: {e}")
    return None

def download(url, filepath):
    """Download image to path."""
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
    print("Downloading Nagaland Tourism Images from Wikimedia Commons")
    print("=" * 60)

    all_targets = list(SEARCH_TERMS.keys())
    downloaded = 0
    failed = []

    # Phase 1: Exact titles
    print("\n--- Phase 1: Exact Wikimedia files ---")
    for filename, title in EXACT_FILES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename}")
            downloaded += 1
            continue
        print(f"  {filename} <- {title} ... ", end="", flush=True)
        url = get_wiki_file_url(title)
        if url and download(url, filepath):
            downloaded += 1
        else:
            print("  Not found, will fallback")
        time.sleep(0.5)

    # Phase 2: Alt titles
    print("\n--- Phase 2: Alternative file titles ---")
    for filename, title in ALT_FILES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            continue
        print(f"  {filename} <- {title} ... ", end="", flush=True)
        url = get_wiki_file_url(title)
        if url and download(url, filepath):
            downloaded += 1
        else:
            print("  Not found, will fallback")
        time.sleep(0.5)

    # Phase 3: Category members
    print("\n--- Phase 3: Category search ---")
    for filename, cat in CATEGORIES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            continue
        print(f"  {filename} <- Category:{cat} ... ", end="", flush=True)
        url = get_category_image(cat)
        if url and download(url, filepath):
            downloaded += 1
        else:
            print("  Not found, will search")
        time.sleep(0.5)

    # Phase 4: Search for anything remaining
    print("\n--- Phase 4: Search fallbacks ---")
    for filename, query in SEARCH_TERMS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            continue
        print(f"  {filename} <- '{query}' ... ", end="", flush=True)
        url = search_wiki(query)
        if url and download(url, filepath):
            downloaded += 1
        else:
            print("  NO RESULTS")
            failed.append(filename)
        time.sleep(0.5)

    # Summary
    print("\n" + "=" * 60)
    print("\nFiles in images/nagaland/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        status = "OK" if size > 5000 else "SMALL"
        print(f"  {f}: {size/1024:.0f} KB [{status}]")

if __name__ == "__main__":
    main()
