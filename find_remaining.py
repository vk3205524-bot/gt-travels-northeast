import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}

# Let's inspect meghalayatourism.in main page and search for image URLs
req = urllib.request.Request('https://www.meghalayatourism.in/', headers=headers)
with urllib.request.urlopen(req, timeout=12) as r:
    home_html = r.read().decode('utf-8', errors='ignore')

web_assets = re.findall(r'https://meghtour\.web-assets\.org/[^"\'>\s]+', home_html)
print("Meghalaya tourism web-assets on home:", len(web_assets))
for a in set(web_assets):
    if any(k in a.lower() for k in ['krang', 'shuri', 'shnong', 'wari', 'nartiang', 'jaintia', 'garo', 'dawki']):
        print("  Asset match:", a)

# Let's also check South Garo Hills for Wari Chora
try:
    req = urllib.request.Request('https://southgarohills.gov.in/', headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        sgh = r.read().decode('utf-8', errors='ignore')
        sgh_imgs = re.findall(r'https://cdn\.s3waas\.gov\.in/[^"\'>\s]+', sgh)
        print("SGH cdn images:", len(sgh_imgs))
        for img in set(sgh_imgs)[:8]:
            print("  SGH:", img)
except Exception as e:
    print("SGH error:", e)
