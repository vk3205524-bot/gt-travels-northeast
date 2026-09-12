import urllib.request
import os

images_map = {
    # 1. Shillong Circuit
    'umiam-lake': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/dc/Umiam_lake_1%2C_shillong.jpg/1280px-Umiam_lake_1%2C_shillong.jpg',
    'wards-lake': 'https://cdn.s3waas.gov.in/s31efa39bcaec6f3900149160693694536/uploads/2019/01/2019011648-1024x768.jpeg',
    'cathedral-shillong': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/78/Cathedral_of_Mary_Help_of_Christians.jpg/1280px-Cathedral_of_Mary_Help_of_Christians.jpg',
    'don-bosco': 'https://cdn.s3waas.gov.in/s31efa39bcaec6f3900149160693694536/uploads/2019/01/2019010921.jpg',
    'elephant-falls': 'https://cdn.s3waas.gov.in/s31efa39bcaec6f3900149160693694536/uploads/2019/01/2019010921-1-1024x656.jpg',
    'laitlum-canyons': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9e/Laitlum%2C_Shillong_in_2026.jpg/1280px-Laitlum%2C_Shillong_in_2026.jpg',

    # 2. Cherrapunji / Sohra Circuit
    'dainthlen': 'http://cherrapunji.sohraspices.com/wp-content/uploads/2021/06/M_Dainthlen2.jpg',
    'wei-sawdong': 'https://meghtour.web-assets.org/cdn-cgi/image/format=auto,width=1200,quality=100,fit=scale-down,slow-connection-quality=45/gallery/Weisawdong.jpg',
    'arwah-cave': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/67/Arwah_Cave.jpg/1280px-Arwah_Cave.jpg',
    'nohkalikai': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/0d/Nohkalikai.jpg/1280px-Nohkalikai.jpg',
    'mawsmai-cave': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e7/Mawsmai_Cave_in_Meghalaya%2C_India.jpg/1280px-Mawsmai_Cave_in_Meghalaya%2C_India.jpg',
    'seven-sisters': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a6/Seven_Sisters_Falls.jpg/1280px-Seven_Sisters_Falls.jpg',
    'double-decker': 'https://cdn.s3waas.gov.in/s31efa39bcaec6f3900149160693694536/uploads/2019/01/2019011657-1024x768.jpeg',

    # 3. Dawki & Border Circuit
    'mawlynnong': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/bd/Mawlynnong.jpg/1280px-Mawlynnong.jpg',
    'riwai-root-bridge': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d2/RIWAI_natures_bridge.jpg/1280px-RIWAI_natures_bridge.jpg',
    'dawki-umngot': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ab/Umngot_river%2C_Dawki.jpg/1280px-Umngot_river%2C_Dawki.jpg',
    'shnongpdeng': 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=800&q=80',
    'krang-shuri': 'https://images.unsplash.com/photo-1518457607834-6e8d80c183c5?w=800&q=80',

    # 4. Adventure / Offbeat Circuit
    'wari-chora': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800&q=80',
    'nongkhnum-island': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80',
    'phe-phe-falls': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/6/64/Phe_Phe_falls.jpg/1280px-Phe_Phe_falls.jpg',
    'nartiang-monoliths': 'https://images.unsplash.com/photo-1533105079780-92b9be482077?w=800&q=80'
}

dest_dir = 'c:/Users/vk320/Downloads/tourism/images/meghalaya'
os.makedirs(dest_dir, exist_ok=True)

success = 0
for name, url in images_map.items():
    filepath = os.path.join(dest_dir, f"{name}.jpg")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=12) as r, open(filepath, 'wb') as f:
            f.write(r.read())
        size = os.path.getsize(filepath)
        print(f"[DOWNLOADED] {name}.jpg ({size} bytes) from {url[:60]}...")
        success += 1
    except Exception as e:
        print(f"[FAILED] {name} from {url}: {e}")

print(f"\nCompleted: {success}/{len(images_map)} images successfully updated!")
