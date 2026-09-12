import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_page(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# 1. East Khasi Hills gov gallery (Don Bosco, Elephant Falls, Root Bridge)
ekh_html = fetch_page('https://eastkhasihills.gov.in/gallery/picturesque-scenery/')
print("East Khasi Hills length:", len(ekh_html))
# Find images in ekh
ekh_imgs = re.findall(r'https?://eastkhasihills\.gov\.in/wp-content/uploads/[^"\'>\s]+\.(?:jpg|jpeg|png)', ekh_html, re.IGNORECASE)
print("EKH images found:", len(ekh_imgs))
for img in set(ekh_imgs):
    print(" EKH:", img)

# 2. South Garo Hills gov page (Wari Chora)
sgh_html = fetch_page('https://southgarohills.gov.in/tourist-place/chora-wari/')
print("\nSouth Garo Hills length:", len(sgh_html))
sgh_imgs = re.findall(r'https?://southgarohills\.gov\.in/wp-content/uploads/[^"\'>\s]+\.(?:jpg|jpeg|png)', sgh_html, re.IGNORECASE)
print("SGH images found:", len(sgh_imgs))
for img in set(sgh_imgs):
    print(" SGH:", img)

# 3. Cherrapunji gallery (Dainthlen)
cherra_html = fetch_page('https://cherrapunji.com/gallery/')
print("\nCherrapunji.com length:", len(cherra_html))
cherra_imgs = re.findall(r'https?://cherrapunji\.com/[^"\'>\s]+\.(?:jpg|jpeg|png)', cherra_html, re.IGNORECASE)
for img in set(cherra_imgs)[:8]:
    print(" Cherrapunji:", img)

# 4. Holidify Wei Sawdong
holidify_ws_html = fetch_page('https://www.holidify.com/places/cherrapunjee/wei-sawdong-falls-photos-1270787.html')
print("\nHolidify Wei Sawdong length:", len(holidify_ws_html))
ws_imgs = re.findall(r'https?://images\.holidify\.com/images/[^"\'>\s]+\.(?:jpg|jpeg|png)', holidify_ws_html, re.IGNORECASE)
for img in set(ws_imgs)[:5]:
    print(" Holidify Wei Sawdong:", img)

# 5. Holidify Shillong (Ward's lake)
holidify_sh_html = fetch_page('https://www.holidify.com/places/shillong/photos.html')
print("\nHolidify Shillong length:", len(holidify_sh_html))
sh_imgs = re.findall(r'https?://images\.holidify\.com/images/[^"\'>\s]+\.(?:jpg|jpeg|png)', holidify_sh_html, re.IGNORECASE)
for img in set(sh_imgs)[:8]:
    print(" Holidify Shillong:", img)
