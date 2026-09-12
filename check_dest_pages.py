import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request('https://eastkhasihills.gov.in/gallery/picturesque-scenery/', headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

# find all gallery elements with captions or titles
matches = re.findall(r'<a[^>]+href=["\'](https://cdn\.s3waas\.gov\.in/[^"\']+)["\'][^>]*title=["\']([^"\']*)["\']', html)
if not matches:
    matches = re.findall(r'title=["\']([^"\']*)["\'][^>]*<img[^>]+src=["\']([^"\']+)["\']', html)

print("Matches found in EKH:", len(matches))
for m in matches:
    print(m)

# Also check Meghalaya Tourism for Krang Shuri, Shnongpdeng, Nartiang
for url, label in [
    ('https://www.meghalayatourism.in/destinations/krang-suri-falls/', 'Krang Shuri'),
    ('https://www.meghalayatourism.in/destinations/shnongpdeng/', 'Shnongpdeng'),
    ('https://www.meghalayatourism.in/destinations/nartiang-monoliths/', 'Nartiang')
]:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            page = r.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', page)
            print(f"\n{label} page images:")
            for img in imgs[:5]:
                print(f"  {img}")
    except Exception as e:
        print(f"Error for {label}: {e}")
