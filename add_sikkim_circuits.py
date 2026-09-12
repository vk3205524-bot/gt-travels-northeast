"""
Generate Sikkim 4-circuit HTML and replace the old single card Sikkim section in destinations.html.
Uses the same CSS classes as Meghalaya, Arunachal, Assam, Nagaland, Manipur, Mizoram, and Tripura circuits.
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

SIKKIM_HTML = '''      <!-- Sikkim Destination Showcase: 4 Core Circuits -->
      <div class="state-section" id="sikkim" style="margin-bottom: 5rem; opacity: 1 !important; transform: none !important;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">&#10022; GT TRAVELS SIKKIM PACKAGES</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Sikkim <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">&mdash; Mountain Kingdom &amp; Land of Kanchenjunga</span></h3>
              <p style="max-width: 780px; font-size: 1.05rem; color: #475569;">Book sanitized cabs and complete sightseeing packages across Sikkim with GT Travels Shillong. Journey from the crystal turquoise waters of Gurudongmar Lake (17,800 ft) and blooming Yumthang Valley to the historic Old Silk Route at Nathula Pass and the iconic Pelling Skywalk facing Mount Kanchenjunga.</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20customize%20a%20Sikkim%20cab%20tour" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Itinerary</a>
          </div>
        </div>

        <div class="circuits-container">

          <!-- 1. North Sikkim Glacial Paradise (3N/4D – 4N/5D) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4 Nights / 5 Days</span>
                <h4 class="circuit-title">North Sikkim Glacial Paradise</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Gangtok &#10132; Lachen &#10132; Gurudongmar Lake (17,800 ft) &#10132; Lachung &#10132; Yumthang Valley &#10132; Zero Point &#10132; Gangtok</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/sikkim/gurudongmar-lake.jpg" alt="Gurudongmar Lake" loading="lazy">
                <div class="circuit-place-name">Gurudongmar Lake</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/yumthang-valley.jpg" alt="Yumthang Valley of Flowers" loading="lazy">
                <div class="circuit-place-name">Yumthang Valley</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/zero-point.jpg" alt="Zero Point Yumesamdong" loading="lazy">
                <div class="circuit-place-name">Zero Point</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/lachung.jpg" alt="Lachung Village" loading="lazy">
                <div class="circuit-place-name">Lachung</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/lachen.jpg" alt="Lachen Village" loading="lazy">
                <div class="circuit-place-name">Lachen</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20North%20Sikkim%20Glacial%20Paradise%20(4N/5D)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 2. Gangtok & High-Altitude Silk Route (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Gangtok &amp; High-Altitude Silk Route</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Gangtok City (MG Marg, Rumtek) &#10132; Tsomgo Lake (12,400 ft) &#10132; Baba Mandir &#10132; Nathula Pass (Indo-China Border)</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/sikkim/tsomgo-lake.jpg" alt="Tsomgo Changu Lake" loading="lazy">
                <div class="circuit-place-name">Tsomgo Lake</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/nathula-pass.jpg" alt="Nathula Pass" loading="lazy">
                <div class="circuit-place-name">Nathula Pass</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/rumtek-monastery.jpg" alt="Rumtek Monastery" loading="lazy">
                <div class="circuit-place-name">Rumtek Monastery</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/gangtok.jpg" alt="Gangtok MG Marg" loading="lazy">
                <div class="circuit-place-name">Gangtok (MG Marg)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/baba-mandir.jpg" alt="Baba Harbhajan Singh Mandir" loading="lazy">
                <div class="circuit-place-name">Baba Mandir</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Gangtok%20%26%20High-Altitude%20Silk%20Route%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 3. Pelling & West Sikkim Kanchenjunga Heritage (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Pelling &amp; West Sikkim Kanchenjunga Heritage</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Gangtok / Siliguri &#10132; Pelling Skywalk &#10132; Rabdentse Ruins &#10132; Pemayangtse Monastery &#10132; Khecheopalri Lake &#10132; Yuksom</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/sikkim/pelling-skywalk.jpg" alt="Pelling Skywalk & Chenrezig Statue" loading="lazy">
                <div class="circuit-place-name">Pelling Skywalk</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/rabdentse-ruins.jpg" alt="Rabdentse Ruins" loading="lazy">
                <div class="circuit-place-name">Rabdentse Ruins</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/pemayangtse.jpg" alt="Pemayangtse Monastery" loading="lazy">
                <div class="circuit-place-name">Pemayangtse Monastery</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/khecheopalri-lake.jpg" alt="Khecheopalri Lake" loading="lazy">
                <div class="circuit-place-name">Khecheopalri Lake</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/yuksom.jpg" alt="Yuksom First Capital" loading="lazy">
                <div class="circuit-place-name">Yuksom</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Pelling%20%26%20West%20Sikkim%20Kanchenjunga%20Heritage%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 4. Namchi, Ravangla & Temi Tea Trail (1-2 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 1-2 Days Tour</span>
                <h4 class="circuit-title">Namchi, Ravangla &amp; Temi Tea Trail</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Gangtok &#10132; Temi Tea Garden &#10132; Buddha Park (Ravangla) &#10132; Char Dham (Namchi) &#10132; Samdruptse</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/sikkim/temi-tea-garden.jpg" alt="Temi Tea Garden" loading="lazy">
                <div class="circuit-place-name">Temi Tea Garden</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/buddha-park-ravangla.jpg" alt="Buddha Park Ravangla" loading="lazy">
                <div class="circuit-place-name">Buddha Park (Ravangla)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/char-dham-namchi.jpg" alt="Char Dham Namchi" loading="lazy">
                <div class="circuit-place-name">Char Dham (Namchi)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/sikkim/samdruptse.jpg" alt="Samdruptse Guru Padmasambhava" loading="lazy">
                <div class="circuit-place-name">Samdruptse</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Namchi,%20Ravangla%20%26%20Temi%20Tea%20Trail%20(1-2%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

        </div>
      </div>'''


def main():
    with open(DEST_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "      <!-- Sikkim -->"
    end_marker = "      <!-- Arunachal Pradesh Destination Showcase: 4 Core Circuits -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print("ERROR: Could not find <!-- Sikkim --> marker!")
        return
    if end_idx == -1:
        print("ERROR: Could not find Arunachal Pradesh marker!")
        return

    old_section = content[start_idx:end_idx]
    print(f"Found old Sikkim section ({len(old_section)} chars)")
    print(f"  From char {start_idx} to {end_idx}")

    new_content = content[:start_idx] + SIKKIM_HTML + "\n\n" + content[end_idx:]

    with open(DEST_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSuccessfully replaced Sikkim section!")
    print(f"Old length: {len(content)} chars")
    print(f"New length: {len(new_content)} chars")
    print(f"Added: {len(new_content) - len(content)} chars")


if __name__ == "__main__":
    main()
