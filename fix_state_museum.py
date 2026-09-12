"""Download state-museum.jpg from working wiki search or reliable unsplash link"""
import urllib.request
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Manipur_State_Museum.jpg/1200px-Manipur_State_Museum.jpg",
    headers={"User-Agent": "GTTravelsBot/1.0 (gttravels12345@gmail.com)"}
)

dest = r"c:\Users\vk320\Downloads\tourism\images\manipur\state-museum.jpg"

try:
    with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
        with open(dest, "wb") as f:
            f.write(resp.read())
    print(f"Downloaded state-museum.jpg successfully! ({os.path.getsize(dest)/1024:.0f} KB)")
except Exception as e:
    print(f"Wiki direct failed ({e}), trying alternative...")
    # Alternative URL
    fallback_url = "https://images.unsplash.com/photo-1572953109213-3be62398eb95?w=800&q=80"
    req2 = urllib.request.Request(fallback_url, headers={"User-Agent": "GTTravelsBot/1.0"})
    with urllib.request.urlopen(req2, context=ctx, timeout=20) as resp:
        with open(dest, "wb") as f:
            f.write(resp.read())
    print(f"Downloaded fallback state-museum.jpg! ({os.path.getsize(dest)/1024:.0f} KB)")
