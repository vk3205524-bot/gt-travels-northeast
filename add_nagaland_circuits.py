"""
Generate Nagaland 4-circuit HTML and replace the old Nagaland section in destinations.html.
Uses the same CSS classes as Meghalaya, Arunachal, and Assam circuits.
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

NAGALAND_HTML = '''      <!-- Nagaland Destination Showcase: 4 Core Circuits -->
      <div class="state-section" id="nagaland" style="margin-bottom: 5rem; opacity: 1 !important; transform: none !important;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">&#10022; GT TRAVELS NAGALAND PACKAGES</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Nagaland <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">&mdash; Land of Festivals</span></h3>
              <p style="max-width: 780px; font-size: 1.05rem; color: #475569;">Book sanitized cabs and complete sightseeing packages across Nagaland with GT Travels Shillong. Experience the world-famous Hornbill Festival, the emerald Dzükou Valley trek, ancient Konyak headhunter heritage, and scenic Ao tribal homelands with verified local drivers.</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20customize%20a%20Nagaland%20cab%20tour" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Itinerary</a>
          </div>
        </div>

        <div class="circuits-container">

          <!-- 1. Hornbill, Kohima & Dzükou Trek (3N/4D – 4N/5D) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4 Nights / 5 Days</span>
                <h4 class="circuit-title">Hornbill, Kohima &amp; Dzükou Trek</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Dimapur &#10132; Kohima &#10132; Kisama Heritage Village &#10132; Khonoma Green Village &#10132; Dzükou Valley Trek &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/nagaland/kisama.jpg" alt="Kisama Heritage Village" loading="lazy">
                <div class="circuit-place-name">Kisama Heritage Village</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/dzukou-valley.jpg" alt="Dzükou Valley" loading="lazy">
                <div class="circuit-place-name">Dzükou Valley</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/khonoma.jpg" alt="Khonoma Green Village" loading="lazy">
                <div class="circuit-place-name">Khonoma Green Village</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/kohima.jpg" alt="Kohima Town & War Cemetery" loading="lazy">
                <div class="circuit-place-name">Kohima</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/dimapur.jpg" alt="Dimapur & Kachari Ruins" loading="lazy">
                <div class="circuit-place-name">Dimapur (Kachari Ruins)</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Hornbill,%20Kohima%20%26%20Dzukou%20Trek%20(4N/5D)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 2. Konyak Headhunters & Mon Expedition (4 Nights / 5 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4 Nights / 5 Days</span>
                <h4 class="circuit-title">Konyak Headhunters &amp; Mon Expedition</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Dibrugarh / Dimapur &#10132; Mon Town &#10132; Longwa (India-Myanmar Border) &#10132; Shangnyu Village &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/nagaland/longwa.jpg" alt="Longwa Village Konyak Headhunters" loading="lazy">
                <div class="circuit-place-name">Longwa Village</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/mon.jpg" alt="Mon District" loading="lazy">
                <div class="circuit-place-name">Mon Town</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/shangnyu.jpg" alt="Shangnyu Village" loading="lazy">
                <div class="circuit-place-name">Shangnyu Village</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Konyak%20Headhunters%20%26%20Mon%20Expedition%20(4N/5D)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 3. Cultural Ao Heartlands & Mokokchung (3 Nights / 4 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 3 Nights / 4 Days</span>
                <h4 class="circuit-title">Cultural Ao Heartlands &amp; Mokokchung</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Dimapur &#10132; Wokha (Doyang Falcon Valley) &#10132; Mokokchung Town &#10132; Ungma Village &#10132; Longkhum Village &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/nagaland/wokha-doyang.jpg" alt="Doyang Reservoir Wokha" loading="lazy">
                <div class="circuit-place-name">Wokha (Doyang Reservoir)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/mokokchung.jpg" alt="Mokokchung Town" loading="lazy">
                <div class="circuit-place-name">Mokokchung</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/ungma.jpg" alt="Ungma Village" loading="lazy">
                <div class="circuit-place-name">Ungma Village</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/longkhum.jpg" alt="Longkhum Village" loading="lazy">
                <div class="circuit-place-name">Longkhum Village</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Cultural%20Ao%20Heartlands%20%26%20Mokokchung%20(3N/4D)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 4. Wildlife, Lakes & Offbeat Phek (4 Nights / 5 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4 Nights / 5 Days</span>
                <h4 class="circuit-title">Wildlife, Lakes &amp; Offbeat Phek</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Dimapur &#10132; Ntangki National Park &#10132; Pfutsero (Highest Town) &#10132; Shilloi Lake &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/nagaland/ntangki.jpg" alt="Ntangki National Park" loading="lazy">
                <div class="circuit-place-name">Ntangki National Park</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/pfutsero.jpg" alt="Pfutsero Town & Glory Peak" loading="lazy">
                <div class="circuit-place-name">Pfutsero (Glory Peak)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/nagaland/shilloi-lake.jpg" alt="Shilloi Lake Phek" loading="lazy">
                <div class="circuit-place-name">Shilloi Lake</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Wildlife,%20Lakes%20%26%20Offbeat%20Phek%20(4N/5D)%20cab%20tour." target="_blank" class="circuit-btn-book">
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

    # Find the old Nagaland section
    start_marker = "      <!-- Nagaland -->"
    end_marker = "      <!-- Manipur -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print("ERROR: Could not find <!-- Nagaland --> marker!")
        return
    if end_idx == -1:
        print("ERROR: Could not find <!-- Manipur --> marker!")
        return

    old_section = content[start_idx:end_idx]
    print(f"Found old Nagaland section ({len(old_section)} chars)")
    print(f"  From char {start_idx} to {end_idx}")

    # Replace
    new_content = content[:start_idx] + NAGALAND_HTML + "\n\n" + content[end_idx:]

    with open(DEST_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSuccessfully replaced Nagaland section!")
    print(f"Old length: {len(content)} chars")
    print(f"New length: {len(new_content)} chars")
    print(f"Added: {len(new_content) - len(content)} chars")


if __name__ == "__main__":
    main()
