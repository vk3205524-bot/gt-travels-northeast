import urllib.request
import urllib.parse
import json

files = [
    'File:Krang_Suri_falls.jpg',
    'File:Krang_Suri_Falls,_Amlarem,_Meghalaya.jpg',
    'File:Wari_Chora.jpg',
    'File:Wari_chora,_South_garo_hills.jpg',
    'File:Wari_Chora,_Meghalaya.jpg',
    'File:Nartiang_Monoliths.jpg',
    'File:Nartiang_monoliths.jpg',
    'File:Shnongpdeng_village.jpg',
    'File:Shnongpdeng.jpg'
]

for fn in files:
    try:
        api_url = f'https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(fn)}&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json'
        req = urllib.request.Request(api_url, headers={'User-Agent': 'GTTravelsBot/1.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for k, v in pages.items():
                if 'imageinfo' in v:
                    print(f"FOUND {fn} -> {v['imageinfo'][0].get('thumburl') or v['imageinfo'][0].get('url')}")
    except Exception as e:
        print(fn, e)
