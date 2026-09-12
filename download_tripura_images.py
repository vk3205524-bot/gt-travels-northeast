"""
Download Tripura tourism destination images from Wikimedia Commons.
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "tripura")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}

# 1. Categories from user's provided links
CATEGORIES = {
    "ujjayanta-palace.jpg": "Ujjayanta_Palace",
    "neermahal.jpg": "Neermahal",
    "rudrasagar-lake.jpg": "Rudrasagar_Lake",
    "sepahijala.jpg": "Sepahijala_Wildlife_Sanctuary",
    "heritage-park.jpg": "Heritage_Park,_Agartala",
    "tripura-sundari.jpg": "Tripura_Sundari_Temple",
    "kalyan-sagar.jpg": "Kalyan_Sagar",
    "chabimura.jpg": "Chabimura",
    "unakoti.jpg": "Unakoti",
    "jampui-hills.jpg": "Jampui_Hills",
    "agartala.jpg": "Agartala",
    "pilak.jpg": "Pilak",
    "trishna-sanctuary.jpg": "Trishna_Wildlife_Sanctuary",
    "dumboor-lake.jpg": "Dumbur_Lake",
    "udaipur-tripura.jpg": "Udaipur,_Tripura",
}

# 2. Search queries
SEARCH_TERMS = {
    "ujjayanta-palace.jpg": ["Ujjayanta Palace Agartala", "Ujjayanta Palace Tripura"],
    "neermahal.jpg": ["Neermahal Tripura", "Neermahal Palace Melaghar"],
    "rudrasagar-lake.jpg": ["Rudrasagar Lake Tripura", "Rudrasagar Lake Neermahal"],
    "sepahijala.jpg": ["Sepahijala Wildlife Sanctuary", "Sepahijala Tripura"],
    "heritage-park.jpg": ["Heritage Park Agartala", "Heritage Park Tripura"],
    "tripura-sundari.jpg": ["Tripura Sundari Temple Udaipur", "Matabari Tripura"],
    "kalyan-sagar.jpg": ["Kalyan Sagar Udaipur Tripura", "Kalyan Sagar Matabari"],
    "chabimura.jpg": ["Chabimura rock carvings", "Chabimura Gomti Tripura", "Chakhwmung"],
    "unakoti.jpg": ["Unakoti rock carvings Tripura", "Unakotiswara Kal Bhairava", "Unakoti Shiva"],
    "jampui-hills.jpg": ["Jampui Hills Tripura", "Jampui Hills sunrise"],
    "agartala.jpg": ["Agartala city Tripura", "Agartala view"],
    "pilak.jpg": ["Pilak Tripura Buddhist", "Pilak archaeological site", "Pilak Jolaibari"],
    "trishna-sanctuary.jpg": ["Trishna Wildlife Sanctuary Tripura", "Trishna Bison Sanctuary"],
    "dumboor-lake.jpg": ["Dumboor Lake Tripura", "Dumbur Lake Narkel Kunja", "Dumbur Lake"],
    "udaipur-tripura.jpg": ["Udaipur Tripura temples", "Udaipur Tripura city of lakes"],
}

FALLBACKS = {
    "heritage-park.jpg": "https://images.unsplash.com/photo-1519331379826-f10be5486c6f?w=800&q=80",
    "rudrasagar-lake.jpg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80",
    "kalyan-sagar.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800&q=80",
}

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
    print("Downloading Tripura Tourism Images from Wikimedia Commons")
    print("=" * 60)

    for filename, queries in SEARCH_TERMS.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"SKIP {filename}")
            continue

        found = False
        # Category lookup
        if filename in CATEGORIES:
            cat = CATEGORIES[filename]
            print(f"  {filename} <- Category:{cat} ... ", end="", flush=True)
            url = get_category_image(cat)
            if url and download(url, filepath):
                found = True

        # Search queries
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

    print("\nAll files in images/tripura/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  {f}: {size/1024:.0f} KB")

if __name__ == "__main__":
    main()
