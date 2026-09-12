"""
Download Assam destination images from Wikimedia Commons.
Uses category API to get best images from user-provided Commons categories,
and direct file API for specific known files.
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "assam")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

# --- Direct known file titles from Wikimedia Commons ---
KNOWN_FILES = {
    "rang-ghar.jpg": "File:Rang Ghar The first Indian pavilion.jpg",
    "charaideo.jpg": "File:Charaideo Moidams image ,Assam.jpg",
    "haflong.jpg": "File:Synod view point, Haflong.jpg",
}

# --- Category-based searches (pick best image from each category) ---
CATEGORY_SEARCHES = {
    "kaziranga.jpg": "Kaziranga National Park",
    "manas.jpg": "Manas National Park",
    "pobitora.jpg": "Pobitora Wildlife Sanctuary",
    "dibru-saikhowa.jpg": "Dibru-Saikhowa National Park",
    "nameri.jpg": "Nameri National Park",
    "kamakhya.jpg": "Kamakhya Temple",
    "majuli.jpg": "Majuli",
    "hajo.jpg": "Hajo, Assam",
    "sualkuchi.jpg": "Sualkuchi",
    "umrangso.jpg": "Umrangso",
    "dima-hasao.jpg": "Dima Hasao district",
    "guwahati.jpg": "Guwahati",
    "dibrugarh.jpg": "Dibrugarh",
    "jorhat.jpg": "Jorhat",
    "tezpur.jpg": "Tezpur",
    "silchar.jpg": "Silchar",
    "brahmaputra.jpg": "Brahmaputra in Assam",
    "umananda.jpg": "Umananda Island",
}

# --- Fallback search terms ---
FALLBACK_SEARCHES = {
    "sivasagar.jpg": "Sivasagar Assam",
}

def get_wiki_file_url(file_title, width=1200):
    """Get direct URL for a specific Wikimedia Commons file."""
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
        print(f"    API error: {e}")
    return None


def get_category_image(category_name, width=1200):
    """Get the best (largest) image from a Wikimedia Commons category."""
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
        print(f"    Category error: {e}")
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
    """Download image from URL."""
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
    print("Downloading Assam Tourism Images from Wikimedia Commons")
    print("=" * 60)

    downloaded = 0
    failed = []

    # Phase 1: Known file titles
    print("\n--- Phase 1: Direct file titles ---")
    for filename, file_title in KNOWN_FILES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename} (exists)")
            downloaded += 1
            continue
        print(f"  {filename} <- {file_title} ... ", end="", flush=True)
        url = get_wiki_file_url(file_title)
        if url:
            if download(url, filepath):
                downloaded += 1
            else:
                failed.append(filename)
        else:
            print("  NOT FOUND")
            failed.append(filename)
        time.sleep(0.5)

    # Phase 2: Category-based (from user's provided links)
    print("\n--- Phase 2: Category galleries ---")
    for filename, category in CATEGORY_SEARCHES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename} (exists)")
            downloaded += 1
            continue
        print(f"  {filename} <- Category:{category} ... ", end="", flush=True)
        url = get_category_image(category)
        if url:
            if download(url, filepath):
                downloaded += 1
            else:
                failed.append(filename)
        else:
            print("  NO IMAGE IN CATEGORY, trying search...")
            url = search_wiki(category)
            if url:
                if download(url, filepath):
                    downloaded += 1
                else:
                    failed.append(filename)
            else:
                print("  NO RESULTS")
                failed.append(filename)
        time.sleep(0.5)

    # Phase 3: Fallback searches
    print("\n--- Phase 3: Fallback searches ---")
    for filename, search_term in FALLBACK_SEARCHES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename} (exists)")
            downloaded += 1
            continue
        print(f"  {filename} <- '{search_term}' ... ", end="", flush=True)
        url = search_wiki(search_term)
        if url:
            if download(url, filepath):
                downloaded += 1
            else:
                failed.append(filename)
        else:
            print("  NO RESULTS")
            failed.append(filename)
        time.sleep(0.5)

    # Phase 4: Retry failed with broader search
    retry_items = list(set(failed))
    if retry_items:
        print("\n--- Phase 4: Retry failed ---")
        for filename in retry_items:
            filepath = os.path.join(OUTPUT_DIR, filename)
            if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
                continue
            search = filename.replace(".jpg", "").replace("-", " ").title() + " Assam"
            print(f"  {filename} <- '{search}' ... ", end="", flush=True)
            url = search_wiki(search)
            if url:
                if download(url, filepath):
                    downloaded += 1
                    failed.remove(filename)
            else:
                print("  NO RESULTS")
            time.sleep(0.5)

    # Summary
    print("\n" + "=" * 60)
    print(f"Downloaded: {downloaded}")
    still_missing = [f for f in set(failed) if not (os.path.exists(os.path.join(OUTPUT_DIR, f)) and os.path.getsize(os.path.join(OUTPUT_DIR, f)) > 5000)]
    if still_missing:
        print(f"Still missing: {still_missing}")

    print("\nFiles in images/assam/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        status = "OK" if size > 5000 else "SMALL"
        print(f"  {f}: {size/1024:.0f} KB [{status}]")


if __name__ == "__main__":
    main()
