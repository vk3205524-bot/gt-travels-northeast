import urllib.parse
import os

spots = [
    # SHILLONG & SURROUNDS
    {
        'id': 'umiam-lake',
        'title': 'Umiam Lake (Barapani)',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Scenic Lake & Boating',
        'img': 'images/meghalaya/umiam-lake.jpg',
        'loc': 'East Khasi Hills (15 km from Shillong)',
        'desc': 'Massive azure reservoir surrounded by sylvan pine hills, famous for watersports, speedboating, and sunset views along NH6.',
        'chips': ['Water Sports', 'Speedboating', 'Sunset Views', 'Houseboat']
    },
    {
        'id': 'laitlum-canyons',
        'title': 'Laitlum Canyons',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Gorges & Canyon View',
        'img': 'images/meghalaya/laitlum-canyons.jpg',
        'loc': 'East Khasi Hills (22 km from Shillong)',
        'desc': 'Known as the "End of the World" — breathtaking amphitheater green canyons plunging sheer into the lush Rasong river valley.',
        'chips': ['Valley Trek', '360° Panorama', 'Drone Spot', 'Pine Valleys']
    },
    {
        'id': 'elephant-falls',
        'title': 'Elephant Falls',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Waterfall',
        'img': 'images/meghalaya/elephant-falls.jpg',
        'loc': 'Upper Shillong (12 km from Police Bazar)',
        'desc': 'Three-tiered cascading waterfall nestled in ferns and mossy rocks, named by the British after an elephant-shaped monolith.',
        'chips': ['3 Cascading Tiers', 'Fern Walkway', 'Family Friendly']
    },
    {
        'id': 'wards-lake',
        'title': 'Ward’s Lake (Nan Polok)',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Heritage Lake',
        'img': 'images/meghalaya/wards-lake.jpg',
        'loc': 'Central Shillong (near Raj Bhavan)',
        'desc': 'Century-old British-era horseshoe lake with a picture-perfect wooden bridge, blooming cherry blossoms, and swan paddle boats.',
        'chips': ['Wooden Bridge', 'Paddle Boating', 'Cherry Blossoms']
    },
    {
        'id': 'shillong-peak',
        'title': 'Shillong Peak & Viewpoint',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Highest Summit',
        'img': 'images/meghalaya/shillong-peak.jpg',
        'loc': 'Upper Shillong (10 km from City)',
        'desc': 'The highest summit in the Khasi Hills (1,965 meters), offering an unmatched bird\'s-eye panorama of Shillong city and cloudscapes.',
        'chips': ['1,965m Summit', 'City View', 'Telescope Point']
    },
    {
        'id': 'don-bosco',
        'title': 'Don Bosco Museum',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Cultural Museum',
        'img': 'images/meghalaya/don-bosco.jpg',
        'loc': 'Mawlai, Shillong',
        'desc': 'Asia\'s acclaimed 7-storey hexagonal museum preserving authentic indigenous traditions, tribal attire, and art of all 8 Northeast states.',
        'chips': ['7 Exhibit Floors', 'Sky Walk View', 'Tribal Weapons']
    },
    {
        'id': 'cathedral-shillong',
        'title': 'Cathedral of Mary Help of Christians',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Gothic Church',
        'img': 'images/meghalaya/cathedral-shillong.jpg',
        'loc': 'Laitumkhrah, Shillong',
        'desc': 'Grand Roman Catholic cathedral featuring towering sky-blue spires, stained glass artwork, and a peaceful high-altitude campus.',
        'chips': ['High Gothic Spires', 'Stained Glass', 'Laitumkhrah Hub']
    },
    {
        'id': 'police-bazar',
        'title': 'Police Bazar (PB)',
        'circuit': 'shillong',
        'circuit_label': 'Shillong Circuit',
        'tag': 'Market & Food Hub',
        'img': 'images/meghalaya/police-bazar.jpg',
        'loc': 'Central Shillong',
        'desc': 'The buzzing commercial heart of Shillong — vibrant Khasi culinary stalls, fruit vendors, handicraft bazaars, and evening shopping.',
        'chips': ['Street Food', 'Handicraft Stalls', 'Night Bazaar']
    },

    # SOHRA / CHERRAPUNJI
    {
        'id': 'nohkalikai',
        'title': 'Nohkalikai Falls',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Tallest Plunge',
        'img': 'images/meghalaya/nohkalikai.jpg',
        'loc': 'Cherrapunji (7 km from town)',
        'desc': 'India’s tallest plunge waterfall (1,115 ft), diving dramatically from limestone plateaus into an intense emerald-green plunge pool.',
        'chips': ['1,115 ft Plunge', 'Emerald Lagoon', 'Legendary Story']
    },
    {
        'id': 'double-decker',
        'title': 'Double Decker Living Root Bridge',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Bio-Engineering Wonder',
        'img': 'images/meghalaya/double-decker.jpg',
        'loc': 'Nongriat Village, Sohra (Trek required)',
        'desc': 'World-famous two-tier suspension bridge hand-woven from living rubber tree roots across centuries by indigenous Khasi villagers.',
        'chips': ['UNESCO Tentative', '3,500 Steps Trek', 'Natural Pools']
    },
    {
        'id': 'wei-sawdong',
        'title': 'Wei Sawdong Falls',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Three-Tier Cascade',
        'img': 'images/meghalaya/wei-sawdong.jpg',
        'loc': 'Cherrapunji (near Dainthlen)',
        'desc': 'Fairy-tale three-tiered stepped waterfall plunging into round natural jade pools surrounded by dense rainforest foliage.',
        'chips': ['3 Step Cascade', 'Turquoise Pools', 'Bamboo Trek']
    },
    {
        'id': 'dainthlen',
        'title': 'Dainthlen Falls',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Waterfall & Canyon',
        'img': 'images/meghalaya/dainthlen.jpg',
        'loc': 'Cherrapunji Plateau',
        'desc': 'Sweeping waterfall that drops off a flat rocky plateau into deep canyons; steeped in the ancient Khasi legend of the giant serpent Thlen.',
        'chips': ['Flat Rock Potholes', 'Canyon Rim', 'Serpent Legend']
    },
    {
        'id': 'seven-sisters',
        'title': 'Seven Sisters Falls (Nohsngithiang)',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Multi-Stream Fall',
        'img': 'images/meghalaya/seven-sisters.jpg',
        'loc': 'Mawsmai, Cherrapunji',
        'desc': 'Seven distinct streams tumbling in unison down a 1,000-foot limestone cliff wall with sunset views overlooking the Bangladesh border.',
        'chips': ['7 Parallel Streams', 'Sunset View', 'Border Vista']
    },
    {
        'id': 'mawsmai-cave',
        'title': 'Mawsmai Limestone Cave',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Illuminated Cave',
        'img': 'images/meghalaya/mawsmai-cave.jpg',
        'loc': 'Cherrapunji (6 km from town)',
        'desc': 'Spectacular prehistoric limestone cave network with internal lighting, displaying ancient stalactites, stalagmites, and chambers.',
        'chips': ['Lit Passages', 'Stalactites', 'Family Friendly']
    },
    {
        'id': 'arwah-cave',
        'title': 'Arwah Prehistoric Cave',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Fossil Cave',
        'img': 'images/meghalaya/arwah-cave.jpg',
        'loc': 'Lawsohtun, Cherrapunji',
        'desc': 'Vast limestone caverns featuring millions-of-years-old marine crustacean fossils clearly embedded inside rock walls and canyon overlooks.',
        'chips': ['Marine Fossils', 'Underground Stream', 'Forest Boardwalk']
    },
    {
        'id': 'rainbow-falls',
        'title': 'Rainbow Falls',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Turquoise Lagoon',
        'img': 'images/meghalaya/rainbow-falls.jpg',
        'loc': 'Nongriat (1.5 hrs beyond Double Decker)',
        'desc': 'A hidden sapphire lagoon and thundering fall where overhead sunlight creates an everlasting rainbow over mist and crystal boulders.',
        'chips': ['Perpetual Rainbow', 'Wild Swimming', 'Adventure Trek']
    },
    {
        'id': 'garden-of-caves',
        'title': 'Garden of Caves (Ka Bri Ki Synrang)',
        'circuit': 'sohra',
        'circuit_label': 'Sohra Circuit',
        'tag': 'Nature Park & Falls',
        'img': 'images/meghalaya/garden-of-caves.jpg',
        'loc': 'Laitryngew (near Sohra)',
        'desc': 'Enchanted natural sanctuary featuring 7 natural waterfalls, bamboo paths, ancient warrior caves, and tranquil freshwater springs.',
        'chips': ['7 Waterfalls', 'Bamboo Walkways', 'King\'s Cave']
    },

    # DAWKI & MAWLYNNONG
    {
        'id': 'dawki-umngot',
        'title': 'Umngot River (Dawki Glass Boating)',
        'circuit': 'dawki',
        'circuit_label': 'Dawki Circuit',
        'tag': 'Crystal Clear River',
        'img': 'images/meghalaya/dawki-umngot.jpg',
        'loc': 'West Jaintia / Indo-Bangla Border',
        'desc': 'Globally renowned crystal-clear river where boats appear to float effortlessly mid-air above riverbed pebbles and emerald water.',
        'chips': ['Floating Boat Illusion', 'Suspension Bridge', 'Crystal Water']
    },
    {
        'id': 'shnongpdeng',
        'title': 'Shnongpdeng Adventure Village',
        'circuit': 'dawki',
        'circuit_label': 'Dawki Circuit',
        'tag': 'Riverside Camping',
        'img': 'images/meghalaya/shnongpdeng.jpg',
        'loc': '8 km upstream from Dawki',
        'desc': 'Pristine riverside camping hub on the Umngot; enjoy riverside bonfire tents, kayaking, cliff diving, snorkeling, and bamboo walks.',
        'chips': ['Beach Camping', 'Kayaking', 'Cliff Diving', 'Snorkeling']
    },
    {
        'id': 'mawlynnong',
        'title': 'Mawlynnong (Asia’s Cleanest Village)',
        'circuit': 'dawki',
        'circuit_label': 'Dawki Circuit',
        'tag': 'Eco Heritage Village',
        'img': 'images/meghalaya/mawlynnong.jpg',
        'loc': 'East Khasi Hills (near Dawki)',
        'desc': 'Crowned Asia\'s Cleanest Village; celebrated for 100% literacy, bamboo cone dustbins, flowering pathways, and thatched cottages.',
        'chips': ['100% Eco-Clean', 'Skywalk Treehouse', 'Floral Pathways']
    },
    {
        'id': 'riwai-root-bridge',
        'title': 'Riwai Single Living Root Bridge',
        'circuit': 'dawki',
        'circuit_label': 'Dawki Circuit',
        'tag': 'Accessible Root Bridge',
        'img': 'images/meghalaya/riwai-root-bridge.jpg',
        'loc': 'Riwai (just 2 km from Mawlynnong)',
        'desc': 'Magnificent living root bridge spanning a quiet river; accessible via a gentle 10-minute paved walk without strenuous trekking.',
        'chips': ['Easy 10-min Walk', 'River Pool', 'Family Friendly']
    },
    {
        'id': 'borhill-falls',
        'title': 'Borhill Falls (Bophill)',
        'circuit': 'dawki',
        'circuit_label': 'Dawki Circuit',
        'tag': 'Border Waterfall',
        'img': 'images/meghalaya/borhill-falls.jpg',
        'loc': 'Pynursla-Dawki Highway',
        'desc': 'Roaring roadside waterfall gushing down the mountain cliff, spraying fresh mist right beside the road overlooking Bangladesh.',
        'chips': ['Roadside View', 'Powerful Spray', 'Border Highway']
    },
    {
        'id': 'tamabil-border',
        'title': 'Tamabil Border Zero Point',
        'circuit': 'dawki',
        'circuit_label': 'Dawki Circuit',
        'tag': 'International Border',
        'img': 'images/meghalaya/tamabil-border.jpg',
        'loc': 'Dawki Border',
        'desc': 'International land trade post and border viewpoint connecting India and Bangladesh with panoramic views of the Sylhet plains.',
        'chips': ['Zero Point', 'Sylhet Plains', 'Friendship Gate']
    },

    # JAINTIA HILLS
    {
        'id': 'krang-shuri',
        'title': 'Krang Shuri Falls',
        'circuit': 'jaintia',
        'circuit_label': 'Jaintia Hills Circuit',
        'tag': 'Turquoise Paradise',
        'img': 'images/meghalaya/krang-shuri.jpg',
        'loc': 'Amlarem, West Jaintia Hills',
        'desc': 'Breathtaking natural waterfall plunging into a brilliant sky-blue swimming pool surrounded by polished stone trails and campsites.',
        'chips': ['Turquoise Water', 'Swimming with Jackets', 'Boating & Camping']
    },
    {
        'id': 'phe-phe-falls',
        'title': 'Phe Phe Falls (Paradise Falls)',
        'circuit': 'jaintia',
        'circuit_label': 'Jaintia Hills Circuit',
        'tag': 'Two-Tier Cascade',
        'img': 'images/meghalaya/phe-phe-falls.jpg',
        'loc': 'Shutter Village, West Jaintia Hills',
        'desc': 'Hidden gem two-tier waterfall cascading into an ultra-deep azure natural swimming pool reached via river kayak and grassland trek.',
        'chips': ['Two-Tier Plunge', 'Kayak Crossing', 'Azure Basin']
    },
    {
        'id': 'nartiang-monoliths',
        'title': 'Nartiang Monoliths & Durga Temple',
        'circuit': 'jaintia',
        'circuit_label': 'Jaintia Hills Circuit',
        'tag': 'Ancient Megaliths',
        'img': 'images/meghalaya/nartiang-monoliths.jpg',
        'loc': 'Nartiang, Jaintia Hills',
        'desc': 'World’s largest cluster of ancient megalithic stones planted by Jaintia royalty, alongside a 500-year-old historic Shakti Peeth temple.',
        'chips': ['World\'s Tallest Menhir', '500-Yr Temple', 'Jaintia Royalty']
    },
    {
        'id': 'tyrshi-falls',
        'title': 'Tyrshi Falls',
        'circuit': 'jaintia',
        'circuit_label': 'Jaintia Hills Circuit',
        'tag': 'Stepped Falls',
        'img': 'images/meghalaya/tyrshi-falls.jpg',
        'loc': 'Near Jowai, West Jaintia Hills',
        'desc': 'Graceful stepped waterfall reached via a scenic arched stone footbridge overlooking the vast green Pynthorwah paddy valley.',
        'chips': ['Stone Arched Bridge', 'Paddy Valley View', 'Tranquil']
    },
    {
        'id': 'thadlaskein-lake',
        'title': 'Thadlaskein Lake',
        'circuit': 'jaintia',
        'circuit_label': 'Jaintia Hills Circuit',
        'tag': 'Historical Pine Lake',
        'img': 'images/meghalaya/thadlaskein-lake.jpg',
        'loc': 'Wahiajer, Jaintia Hills (on NH6)',
        'desc': 'Centuries-old man-made lake dug by Jaintia warrior Sajar Nangli using arrowheads; bordered by rolling pine forests and picnic spots.',
        'chips': ['Warrior Legend', 'Pine Groves', 'Boating']
    },

    # GARO HILLS & OFFBEAT
    {
        'id': 'wari-chora',
        'title': 'Wari Chora Hidden Slot Canyon',
        'circuit': 'garo',
        'circuit_label': 'Garo Hills & Offbeat',
        'tag': 'Slot Canyon Paradise',
        'img': 'images/meghalaya/wari-chora.jpg',
        'loc': 'South Garo Hills',
        'desc': 'Otherworldly narrow canyon on the emerald Rongdik river flanked by 100-foot mossy rock walls and cascading slot waterfalls.',
        'chips': ['Canyon Rafting', 'Emerald Rongdik', 'Ultimate Offbeat']
    },
    {
        'id': 'balpakram',
        'title': 'Balpakram National Park',
        'circuit': 'garo',
        'circuit_label': 'Garo Hills & Offbeat',
        'tag': 'Land of Perpetual Winds',
        'img': 'images/meghalaya/balpakram.jpg',
        'loc': 'South Garo Hills (near Baghmara)',
        'desc': 'The "Grand Canyon of Meghalaya" — sheer gorges, rare carnivorous pitcher plants, wild elephants, and mystical Garo spiritual lore.',
        'chips': ['Meghalaya Grand Canyon', 'Pitcher Plants', 'Wild Elephants']
    },
    {
        'id': 'siju-cave',
        'title': 'Siju River Cave (Dobakkol)',
        'circuit': 'garo',
        'circuit_label': 'Garo Hills & Offbeat',
        'tag': 'Subterranean River Cave',
        'img': 'images/meghalaya/siju-cave.jpg',
        'loc': 'South Garo Hills (near Simsang)',
        'desc': 'India’s third-longest cave system featuring an underground knee-deep river, massive limestone chambers, and bat colonies.',
        'chips': ['Underground River', 'Bat Colonies', 'Wild Caving']
    },
    {
        'id': 'nokrek',
        'title': 'Nokrek Biosphere Reserve',
        'circuit': 'garo',
        'circuit_label': 'Garo Hills & Offbeat',
        'tag': 'UNESCO Biosphere',
        'img': 'images/meghalaya/nokrek.jpg',
        'loc': 'West Garo Hills (highest summit)',
        'desc': 'Protected UNESCO virgin biosphere and summit (1,412m); prime habitat for red pandas, Asian elephants, and wild gene citrus.',
        'chips': ['Red Panda Habitat', 'Virgin Rainforest', 'Citrus Sanctuary']
    },
    {
        'id': 'nongkhnum-island',
        'title': 'Nongkhnum River Island & Weinia Falls',
        'circuit': 'garo',
        'circuit_label': 'West Khasi Circuit',
        'tag': 'River Island & Falls',
        'img': 'images/meghalaya/nongkhnum-island.jpg',
        'loc': 'West Khasi Hills (near Nongstoin)',
        'desc': 'Second-largest river island in Asia featuring white sand river beaches, pine forest walks, and the roaring horseshoe Weinia Falls.',
        'chips': ['Asia\'s 2nd Largest Island', 'Weinia Falls', 'White Sand Beaches']
    },
    {
        'id': 'mawlyngbna',
        'title': 'Mawlyngbna Adventure Hub',
        'circuit': 'garo',
        'circuit_label': 'Southwest Khasi Circuit',
        'tag': 'Adventure & Fossils',
        'img': 'images/meghalaya/mawlyngbna.jpg',
        'loc': 'Southwest Khasi Hills (Mawsynram)',
        'desc': 'Pristine adventure playground featuring dinosaur-era sea fossils, natural split-rock canyon walks, ziplining, and natural jacuzzis.',
        'chips': ['Split Rock Canyons', 'Sea Fossils', 'Natural Jacuzzi']
    },
    {
        'id': 'kyllang-rock',
        'title': 'Kyllang Rock Dome',
        'circuit': 'garo',
        'circuit_label': 'West Khasi Circuit',
        'tag': 'Granite Dome Monolith',
        'img': 'images/meghalaya/kyllang-rock.jpg',
        'loc': 'Mairang, West Khasi Hills',
        'desc': 'A giant single-block red granite monolith dome rising over 1,000 feet above surrounding pine forests with top-view hiking trails.',
        'chips': ['Red Granite Monolith', '360° Hilltop View', 'Gentle Hike']
    },
    {
        'id': 'mawsynram',
        'title': 'Mawsynram & Mawjymbuin Cave',
        'circuit': 'garo',
        'circuit_label': 'Southwest Khasi Circuit',
        'tag': 'Wettest Place on Earth',
        'img': 'images/meghalaya/mawsynram.jpg',
        'loc': 'Southwest Khasi Hills',
        'desc': 'The officially recognized wettest place on Earth with perpetual cloud cover and a sacred cave housing a natural stalagmite Shiva Lingam.',
        'chips': ['Wettest Spot on Earth', 'Natural Shiva Lingam', 'Misty Valleys']
    }
]

html_cards = []
for s in spots:
    chips_html = ''.join([f'<span class="spot-highlight-chip">{c}</span>' for c in s['chips']])
    wa_msg = f'Hi GT Travels! I am interested in visiting {s["title"]} in Meghalaya. Please share cab/tour details.'
    wa_url = 'https://wa.me/919612946960?text=' + urllib.parse.quote(wa_msg)
    
    card = f'''          <!-- {s['title']} -->
          <div class="spot-card" data-circuit="{s['circuit']}">
            <div class="spot-image-box">
              <img src="{s['img']}" alt="{s['title']}" loading="lazy">
              <span class="spot-circuit-badge">{s['circuit_label']}</span>
              <span class="spot-tag-badge">{s['tag']}</span>
            </div>
            <div class="spot-content">
              <div>
                <h4 class="spot-title">{s['title']}</h4>
                <div class="spot-location"><i class="fas fa-map-marker-alt"></i> {s['loc']}</div>
                <p class="spot-desc">{s['desc']}</p>
                <div class="spot-highlights">
                  {chips_html}
                </div>
              </div>
              <div class="spot-footer">
                <a href="{wa_url}" target="_blank" class="spot-btn-cab"><i class="fab fa-whatsapp"></i> Book Cab / Tour</a>
                <a href="contact.html" class="spot-btn-details">Enquire</a>
              </div>
            </div>
          </div>'''
    html_cards.append(card)

full_cards_str = '\n'.join(html_cards)

section_html = f'''      <!-- Meghalaya Destination Showcase -->
      <div class="state-section animate-on-scroll" id="meghalaya" style="margin-bottom: 5rem;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">✦ GT TRAVELS HOME BASE</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Meghalaya <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">— The Abode of Clouds</span></h3>
              <p style="max-width: 750px; font-size: 1rem; color: #475569;">Explore 35+ stunning tourist attractions across Meghalaya with verified photographs. Filter by circuit or search to plan your taxi tour with GT Travels Shillong.</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20book%20a%20full%20Meghalaya%20tour%20package" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Meghalaya Plan</a>
          </div>
        </div>

        <!-- Controls: Search & Circuit Filter Pills -->
        <div class="meghalaya-controls">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 1rem;">
            <div class="meghalaya-search-wrapper">
              <i class="fas fa-search"></i>
              <input type="text" id="meghalayaSearch" class="meghalaya-search-input" placeholder="Search any spot (e.g., Wei Sawdong, Krang Shuri, Dawki, Wari Chora, Root Bridge)..." oninput="filterMeghalaya()">
            </div>
            <div id="spotCountDisplay" style="font-size: 0.9rem; font-weight: 600; color: var(--secondary);">Showing {len(spots)} places</div>
          </div>
          <div class="meghalaya-pills">
            <button class="meghalaya-pill active" data-circuit="all" onclick="filterMeghalaya('all', this)"><i class="fas fa-globe-asia"></i> All Spots ({len(spots)})</button>
            <button class="meghalaya-pill" data-circuit="shillong" onclick="filterMeghalaya('shillong', this)"><i class="fas fa-city"></i> Shillong & East Khasi (8)</button>
            <button class="meghalaya-pill" data-circuit="sohra" onclick="filterMeghalaya('sohra', this)"><i class="fas fa-cloud-rain"></i> Sohra / Cherrapunji (9)</button>
            <button class="meghalaya-pill" data-circuit="dawki" onclick="filterMeghalaya('dawki', this)"><i class="fas fa-water"></i> Dawki & Mawlynnong (6)</button>
            <button class="meghalaya-pill" data-circuit="jaintia" onclick="filterMeghalaya('jaintia', this)"><i class="fas fa-gem"></i> Jaintia Hills (5)</button>
            <button class="meghalaya-pill" data-circuit="garo" onclick="filterMeghalaya('garo', this)"><i class="fas fa-compass"></i> Garo Hills & Offbeat (8)</button>
          </div>
        </div>

        <!-- Tourist Spots Grid -->
        <div class="meghalaya-spots-grid">
{full_cards_str}
        </div>
      </div>'''

# Now read destinations.html, replace the old Meghalaya section
with open('c:/Users/vk320/Downloads/tourism/destinations.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
old_meghalaya_pattern = r'<!-- Meghalaya -->[\s\S]*?<!-- Sikkim -->'
new_replacement = section_html + '\n\n      <!-- Sikkim -->'

if re.search(old_meghalaya_pattern, html):
    updated_html = re.sub(old_meghalaya_pattern, new_replacement, html)
    with open('c:/Users/vk320/Downloads/tourism/destinations.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    print("SUCCESS: destinations.html updated with complete Meghalaya showcase!")
else:
    print("Pattern not matched, please check HTML structure.")
