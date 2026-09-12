"""
Update all pages with real, authentic Northeast India photos for each state and famous location.
"""
import re

INDEX_FILE = r"c:\Users\vk320\Downloads\tourism\index.html"
PACKAGES_FILE = r"c:\Users\vk320\Downloads\tourism\packages.html"
ABOUT_FILE = r"c:\Users\vk320\Downloads\tourism\about.html"
BLOG_FILE = r"c:\Users\vk320\Downloads\tourism\blog.html"
CONTACT_FILE = r"c:\Users\vk320\Downloads\tourism\contact.html"
DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

# ==============================================================================
# 1. Update index.html
# ==============================================================================
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    idx_content = f.read()

# Update Hero background
idx_content = re.sub(
    r'<section class="hero"[^>]*>',
    r'<section class="hero" style="background-image: linear-gradient(rgba(10, 22, 40, 0.55), rgba(10, 22, 40, 0.65)), url(\'images/meghalaya/double-decker.jpg\');">',
    idx_content
)

# Update Meghalaya Card
idx_content = idx_content.replace(
    '<img src="https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=800&q=80" alt="Meghalaya">',
    '<img src="images/meghalaya/double-decker.jpg" alt="Double Decker Living Root Bridge, Meghalaya">'
)

# Update Arunachal Card
idx_content = idx_content.replace(
    '<img src="images/arunachal/tawang-monastery.jpg" alt="Arunachal Pradesh">',
    '<img src="images/arunachal/tawang-monastery-exterior.jpg" alt="Tawang Monastery, Arunachal Pradesh">'
)

# Update Assam Card
idx_content = idx_content.replace(
    '<img src="images/assam/kaziranga.jpg" alt="Assam">',
    '<img src="images/assam/kaziranga-rhino.jpg" alt="One-Horned Rhino in Kaziranga, Assam">'
)

# Update Nagaland Card
idx_content = idx_content.replace(
    '<img src="images/nagaland/kisama.jpg" alt="Nagaland">',
    '<img src="images/nagaland/dzukou-valley.jpg" alt="Dzükou Valley, Nagaland">'
)

# Update Mizoram Card
idx_content = idx_content.replace(
    '<img src="images/mizoram/solomons-temple.jpg" alt="Mizoram">',
    '<img src="images/mizoram/tuirihiau-falls.jpg" alt="Tuirihiau Falls, Mizoram">'
)

# Update Tripura Card
idx_content = idx_content.replace(
    '<img src="images/tripura/ujjayanta-palace.jpg" alt="Tripura">',
    '<img src="images/tripura/neermahal.jpg" alt="Neermahal Water Palace, Tripura">'
)

# Update Featured Packages on index.html
OLD_PACKAGES_HTML = '''                <!-- Package 1 -->
                <div class="package-card">
                    <div class="package-badge">Bestseller</div>
                    <div class="package-img">
                        <img src="https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=600&q=80" alt="Meghalaya Explorer">
                    </div>
                    <div class="package-content">
                        <div class="package-duration"><i class="far fa-clock"></i> 6 Days</div>
                        <h3>Meghalaya Explorer</h3>
                        <p class="package-price"><strong>₹19,999</strong> <small>per person</small></p>
                        <a href="packages.html" class="btn btn-primary btn-block">View Details</a>
                    </div>
                </div>
                <!-- Package 2 -->
                <div class="package-card">
                    <div class="package-badge package-badge-premium" style="background: var(--secondary); color: var(--primary);">Premium</div>
                    <div class="package-img">
                        <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=80" alt="Complete Northeast Circuit">
                    </div>
                    <div class="package-content">
                        <div class="package-duration"><i class="far fa-clock"></i> 14 Days</div>
                        <h3>Complete Northeast Circuit</h3>
                        <p class="package-price"><strong>₹54,999</strong> <small>per person</small></p>
                        <a href="packages.html" class="btn btn-primary btn-block">View Details</a>
                    </div>
                </div>
                <!-- Package 3 -->
                <div class="package-card">
                    <div class="package-badge">Popular</div>
                    <div class="package-img">
                        <img src="https://images.unsplash.com/photo-1551632811-561732d1e306?w=600&q=80" alt="Sikkim & Gangtok Delight">
                    </div>
                    <div class="package-content">
                        <div class="package-duration"><i class="far fa-clock"></i> 7 Days</div>
                        <h3>Sikkim & Gangtok Delight</h3>
                        <p class="package-price"><strong>₹24,999</strong> <small>per person</small></p>
                        <a href="packages.html" class="btn btn-primary btn-block">View Details</a>
                    </div>
                </div>'''

NEW_PACKAGES_HTML = '''                <!-- Package 1 -->
                <div class="package-card">
                    <div class="package-badge">Bestseller</div>
                    <div class="package-img">
                        <img src="images/meghalaya/krang-shuri.jpg" alt="Krang Shuri Falls, Meghalaya">
                    </div>
                    <div class="package-content">
                        <div class="package-duration"><i class="far fa-clock"></i> 6 Days</div>
                        <h3>Meghalaya Explorer</h3>
                        <p class="package-price"><strong>₹19,999</strong> <small>per person</small></p>
                        <a href="packages.html" class="btn btn-primary btn-block">View Details</a>
                    </div>
                </div>
                <!-- Package 2 -->
                <div class="package-card">
                    <div class="package-badge package-badge-premium" style="background: var(--secondary); color: var(--primary);">Premium</div>
                    <div class="package-img">
                        <img src="images/arunachal/sela-pass.jpg" alt="Sela Pass, Arunachal Pradesh">
                    </div>
                    <div class="package-content">
                        <div class="package-duration"><i class="far fa-clock"></i> 14 Days</div>
                        <h3>Complete Northeast Circuit</h3>
                        <p class="package-price"><strong>₹54,999</strong> <small>per person</small></p>
                        <a href="packages.html" class="btn btn-primary btn-block">View Details</a>
                    </div>
                </div>
                <!-- Package 3 -->
                <div class="package-card">
                    <div class="package-badge">Popular</div>
                    <div class="package-img">
                        <img src="images/sikkim/gurudongmar-lake.jpg" alt="Gurudongmar Lake, Sikkim">
                    </div>
                    <div class="package-content">
                        <div class="package-duration"><i class="far fa-clock"></i> 7 Days</div>
                        <h3>Sikkim & Gangtok Delight</h3>
                        <p class="package-price"><strong>₹24,999</strong> <small>per person</small></p>
                        <a href="packages.html" class="btn btn-primary btn-block">View Details</a>
                    </div>
                </div>'''

idx_content = idx_content.replace(OLD_PACKAGES_HTML, NEW_PACKAGES_HTML)

# Update Travel Gallery on index.html
OLD_GALLERY_HTML = '''            <div class="gallery-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 1rem;">
                <a href="https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=600&q=80" alt="Waterfall" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
                <a href="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=80" alt="Mountains" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
                <a href="https://images.unsplash.com/photo-1432405972618-c6b0c0d60318?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1432405972618-c6b0c0d60318?w=600&q=80" alt="River" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
                <a href="https://images.unsplash.com/photo-1465056836900-5e3e7fdb96e4?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1465056836900-5e3e7fdb96e4?w=600&q=80" alt="Forest" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
                <a href="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&q=80" alt="Monastery" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
                <a href="https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=600&q=80" alt="Tea Garden" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
                <a href="https://images.unsplash.com/photo-1585409677983-0f6c41ca9c3b?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1585409677983-0f6c41ca9c3b?w=600&q=80" alt="Valley" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
                <a href="https://images.unsplash.com/photo-1518002171953-a080ee817e1f?w=1200&q=80" class="gallery-item">
                    <img src="https://images.unsplash.com/photo-1518002171953-a080ee817e1f?w=600&q=80" alt="Lake" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                </a>
            </div>'''

NEW_GALLERY_HTML = '''            <div class="gallery-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.25rem;">
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/meghalaya/double-decker.jpg" alt="Double Decker Living Root Bridge, Meghalaya" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Living Root Bridge, Meghalaya
                    </div>
                </div>
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/sikkim/gurudongmar-lake.jpg" alt="Gurudongmar Lake, Sikkim" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Gurudongmar Lake, Sikkim
                    </div>
                </div>
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/arunachal/sela-pass.jpg" alt="Sela Pass & Lake, Arunachal Pradesh" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Sela Pass, Arunachal
                    </div>
                </div>
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/assam/kaziranga-rhino.jpg" alt="One-Horned Rhino, Kaziranga Assam" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Kaziranga Rhino Safari, Assam
                    </div>
                </div>
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/nagaland/dzukou-valley.jpg" alt="Dzükou Valley, Nagaland" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Dzükou Valley, Nagaland
                    </div>
                </div>
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/manipur/loktak-lake.jpg" alt="Loktak Floating Lake, Manipur" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Loktak Floating Lake, Manipur
                    </div>
                </div>
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/mizoram/tuirihiau-falls.jpg" alt="Tuirihiau Waterfall, Mizoram" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Tuirihiau Falls, Mizoram
                    </div>
                </div>
                <div class="gallery-item" style="position: relative; border-radius: 10px; overflow: hidden; height: 240px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <img src="images/tripura/neermahal.jpg" alt="Neermahal Water Palace, Tripura" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 0.75rem 1rem; background: linear-gradient(transparent, rgba(10,22,40,0.85)); color: white; font-weight: 600; font-size: 0.95rem;">
                        Neermahal Palace, Tripura
                    </div>
                </div>
            </div>'''

idx_content = idx_content.replace(OLD_GALLERY_HTML, NEW_GALLERY_HTML)

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Updated index.html successfully!")


# ==============================================================================
# 2. Update destinations.html Hero
# ==============================================================================
with open(DEST_FILE, "r", encoding="utf-8") as f:
    dest_content = f.read()

dest_content = re.sub(
    r'<header class="page-hero"[^>]*>',
    r'<header class="page-hero" style="background-image: linear-gradient(rgba(10, 22, 40, 0.6), rgba(10, 22, 40, 0.6)), url(\'images/meghalaya/double-decker.jpg\');">',
    dest_content
)

with open(DEST_FILE, "w", encoding="utf-8") as f:
    f.write(dest_content)

print("Updated destinations.html hero!")


# ==============================================================================
# 3. Update packages.html
# ==============================================================================
with open(PACKAGES_FILE, "r", encoding="utf-8") as f:
    pkg_content = f.read()

# Update hero
pkg_content = re.sub(
    r'<header class="page-hero"[^>]*>',
    r'<header class="page-hero" style="background-image: linear-gradient(rgba(10, 22, 40, 0.6), rgba(10, 22, 40, 0.6)), url(\'images/arunachal/sela-pass.jpg\');">',
    pkg_content
)

# Replace any stock images in packages.html with real ones
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=600&q=80', 'images/meghalaya/krang-shuri.jpg')
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&q=80', 'images/arunachal/sela-pass.jpg')
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1551632811-561732d1e306?w=600&q=80', 'images/sikkim/gurudongmar-lake.jpg')
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=600&q=80', 'images/assam/kaziranga-rhino.jpg')
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1504457047772-27faf1c00561?w=600&q=80', 'images/nagaland/dzukou-valley.jpg')
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1518002171953-a080ee817e1f?w=600&q=80', 'images/manipur/loktak-lake.jpg')
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600&q=80', 'images/mizoram/tuirihiau-falls.jpg')
pkg_content = pkg_content.replace('https://images.unsplash.com/photo-1548013146-72479768bada?w=600&q=80', 'images/tripura/neermahal.jpg')

with open(PACKAGES_FILE, "w", encoding="utf-8") as f:
    f.write(pkg_content)

print("Updated packages.html!")


# ==============================================================================
# 4. Update about.html
# ==============================================================================
with open(ABOUT_FILE, "r", encoding="utf-8") as f:
    abt_content = f.read()

abt_content = re.sub(
    r'<header class="page-hero"[^>]*>',
    r'<header class="page-hero" style="background-image: linear-gradient(rgba(10, 22, 40, 0.6), rgba(10, 22, 40, 0.6)), url(\'images/meghalaya/laitlum-canyons.jpg\');">',
    abt_content
)

abt_content = abt_content.replace(
    'https://images.unsplash.com/photo-1432405972618-c6b0c0d60318?w=800&q=80',
    'images/meghalaya/double-decker.jpg'
)

with open(ABOUT_FILE, "w", encoding="utf-8") as f:
    f.write(abt_content)

print("Updated about.html!")


# ==============================================================================
# 5. Update blog.html
# ==============================================================================
with open(BLOG_FILE, "r", encoding="utf-8") as f:
    blg_content = f.read()

blg_content = re.sub(
    r'<header class="page-hero"[^>]*>',
    r'<header class="page-hero" style="background-image: linear-gradient(rgba(10, 22, 40, 0.6), rgba(10, 22, 40, 0.6)), url(\'images/meghalaya/krang-shuri.jpg\');">',
    blg_content
)

blg_content = blg_content.replace('https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=800&q=80', 'images/meghalaya/double-decker.jpg')
blg_content = blg_content.replace('https://images.unsplash.com/photo-1535941339077-2dd1c7963162?w=800&q=80', 'images/assam/kaziranga-rhino.jpg')
blg_content = blg_content.replace('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&q=80', 'images/arunachal/tawang-monastery-exterior.jpg')
blg_content = blg_content.replace('https://images.unsplash.com/photo-1551632811-561732d1e306?w=800&q=80', 'images/sikkim/gurudongmar-lake.jpg')
blg_content = blg_content.replace('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80', 'images/nagaland/kisama.jpg')

with open(BLOG_FILE, "w", encoding="utf-8") as f:
    f.write(blg_content)

print("Updated blog.html!")


# ==============================================================================
# 6. Update contact.html
# ==============================================================================
with open(CONTACT_FILE, "r", encoding="utf-8") as f:
    cnt_content = f.read()

cnt_content = re.sub(
    r'<header class="page-hero"[^>]*>',
    r'<header class="page-hero" style="background-image: linear-gradient(rgba(10, 22, 40, 0.6), rgba(10, 22, 40, 0.6)), url(\'images/meghalaya/umiam-lake.jpg\');">',
    cnt_content
)

with open(CONTACT_FILE, "w", encoding="utf-8") as f:
    f.write(cnt_content)

print("Updated contact.html!")
