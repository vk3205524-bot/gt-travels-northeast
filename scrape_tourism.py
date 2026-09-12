import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_page(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Check EKH
ekh_html = fetch_page('https://eastkhasihills.gov.in/gallery/picturesque-scenery/')
all_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', ekh_html, re.IGNORECASE)
print("EKH all <img> srcs:", len(all_imgs))
for s in list(set(all_imgs))[:12]:
    print("  EKH img:", s)

# Check cherrapunji
cherra_html = fetch_page('https://cherrapunji.com/gallery/')
cherra_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', cherra_html, re.IGNORECASE)
print("Cherrapunji <img> srcs:", len(cherra_imgs))
for s in list(set(cherra_imgs))[:12]:
    print("  Cherra img:", s)

# Check Meghalaya Tourism
megh_html = fetch_page('https://www.meghalayatourism.in/explore/about-meghalaya/image-video-gallery/')
megh_imgs = re.findall(r'https?://[^"\'>\s]+\.(?:jpg|jpeg|png)', megh_html, re.IGNORECASE)
print("Meghalaya tourism imgs:", len(megh_imgs))
for s in list(set(megh_imgs))[:15]:
    if 'gallery' in s or 'upload' in s:
        print("  Meghalaya tourism:", s)
