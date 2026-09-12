import urllib.request
import urllib.parse
import json
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

wiki_files = [
    ('umiam-lake', 'File:Umiam_lake_1,_shillong.jpg'),
    ('cathedral-shillong', 'File:Cathedral_of_Mary_Help_of_Christians.jpg'),
    ('laitlum-canyons', 'File:Laitlum,_Shillong_in_2026.jpg'),
    ('arwah-cave', 'File:Arwah_Cave.jpg'),
    ('nohkalikai', 'File:Nohkalikai.jpg'),
    ('mawsmai-cave', 'File:Mawsmai_Cave_in_Meghalaya,_India.jpg'),
    ('seven-sisters', 'File:Seven_Sisters_Falls.jpg'),
    ('mawlynnong', 'File:Mawlynnong.jpg'),
    ('riwai-root-bridge', 'File:RIWAI_natures_bridge.jpg'),
    ('dawki-umngot', 'File:Umngot_river,_Dawki.jpg'),
    ('phe-phe-falls', 'File:Phe_Phe_falls.jpg')
]

print("--- Resolving Wikimedia Commons Direct URLs ---")
resolved_urls = {}

for name, filename in wiki_files:
    try:
        api_url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(filename)}&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json'
        req = urllib.request.Request(api_url, headers={'User-Agent': 'GTTravelsBot/1.0 (contact@gttravels.com)'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for k, v in pages.items():
                if 'imageinfo' in v:
                    # Prefer thumburl (1200px) or full url
                    img_url = v['imageinfo'][0].get('thumburl') or v['imageinfo'][0].get('url')
                    resolved_urls[name] = img_url
                    print(f"[OK] {name} -> {img_url[:80]}...")
                else:
                    print(f"[NOT FOUND] {name} for {filename}")
    except Exception as e:
        print(f"[ERROR] {name}: {e}")

# If Laitlum failed with 2026, let's search Laitlum
if 'laitlum-canyons' not in resolved_urls:
    try:
        print("Searching fallback for Laitlum...")
        search_api = 'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=Laitlum&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json'
        req = urllib.request.Request(search_api, headers={'User-Agent': 'GTTravelsBot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for k, v in pages.items():
                if 'imageinfo' in v:
                    resolved_urls['laitlum-canyons'] = v['imageinfo'][0].get('thumburl') or v['imageinfo'][0].get('url')
                    print(f"[FALLBACK OK] laitlum-canyons -> {resolved_urls['laitlum-canyons'][:80]}...")
                    break
    except Exception as e:
        print(f"Laitlum search error: {e}")

print("\nTotal resolved from Wikimedia:", len(resolved_urls))
