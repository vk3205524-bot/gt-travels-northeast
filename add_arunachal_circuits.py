"""
Generate the Arunachal Pradesh 4-circuit HTML and replace the old section
in destinations.html. Uses the same CSS classes as the Meghalaya circuits.
"""
import re

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

# The new Arunachal Pradesh section HTML with 4 circuit cards
ARUNACHAL_HTML = '''      <!-- Arunachal Pradesh Destination Showcase: 4 Core Circuits -->
      <div class="state-section" id="arunachal" style="margin-bottom: 5rem; opacity: 1 !important; transform: none !important;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">&#10022; GT TRAVELS ARUNACHAL PACKAGES</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Arunachal Pradesh <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">&mdash; Land of the Rising Sun</span></h3>
              <p style="max-width: 780px; font-size: 1.05rem; color: #475569;">Book sanitized cabs and complete sightseeing packages across Arunachal Pradesh with GT Travels Shillong. Explore our 4 most popular circuits with verified local drivers, pick-up from Guwahati/Dibrugarh, and 4-seater or 7-seater fleet options.</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20customize%20an%20Arunachal%20Pradesh%20cab%20tour" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Itinerary</a>
          </div>
        </div>

        <div class="circuits-container">

          <!-- 1. Classic Tawang Circuit (6 Nights / 7 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 6 Nights / 7 Days</span>
                <h4 class="circuit-title">Classic Tawang Circuit</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Guwahati &#10132; Bhalukpong &#10132; Dirang &#10132; Sela Pass &#10132; Tawang (Bum La, Madhuri Lake, Monasteries) &#10132; Bomdila &#10132; Guwahati</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/arunachal/tawang-monastery.jpg" alt="Tawang Monastery" loading="lazy">
                <div class="circuit-place-name">Tawang Monastery</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/sela-pass.jpg" alt="Sela Pass" loading="lazy">
                <div class="circuit-place-name">Sela Pass</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/madhuri-lake.jpg" alt="Madhuri Lake" loading="lazy">
                <div class="circuit-place-name">Madhuri Lake</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/bum-la-pass.jpg" alt="Bum La Pass" loading="lazy">
                <div class="circuit-place-name">Bum La Pass</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/nuranang-falls.jpg" alt="Nuranang Falls" loading="lazy">
                <div class="circuit-place-name">Nuranang Falls</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/dirang.jpg" alt="Dirang Dzong" loading="lazy">
                <div class="circuit-place-name">Dirang</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/bomdila.jpg" alt="Bomdila Monastery" loading="lazy">
                <div class="circuit-place-name">Bomdila</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Classic%20Tawang%20Circuit%20(6N/7D)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 2. Cultural Ziro Valley Tour (3 Nights / 4 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 3 Nights / 4 Days</span>
                <h4 class="circuit-title">Cultural Ziro Valley Tour</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Guwahati/Naharlagun &#10132; Itanagar &#10132; Ziro Valley (Apatani Villages, Tarin, Talley) &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/arunachal/ziro-valley.jpg" alt="Ziro Valley" loading="lazy">
                <div class="circuit-place-name">Ziro Valley</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/apatani-village.jpg" alt="Apatani Villages" loading="lazy">
                <div class="circuit-place-name">Apatani Villages</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/talley-valley.jpg" alt="Talley Valley" loading="lazy">
                <div class="circuit-place-name">Talley Valley</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/itanagar.jpg" alt="Ita Fort Itanagar" loading="lazy">
                <div class="circuit-place-name">Itanagar (Ita Fort)</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Cultural%20Ziro%20Valley%20Tour%20(3N/4D)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 3. Offbeat Mechuka Adventure (6 Nights / 7 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 6 Nights / 7 Days</span>
                <h4 class="circuit-title">Offbeat Mechuka Adventure</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Dibrugarh &#10132; Aalo &#10132; Mechuka Valley (2 Nights) &#10132; Pasighat &#10132; Dibrugarh</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/arunachal/mechuka-valley.jpg" alt="Mechuka Valley" loading="lazy">
                <div class="circuit-place-name">Mechuka Valley</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/siyom-river.jpg" alt="Siyom River" loading="lazy">
                <div class="circuit-place-name">Siyom River</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/samten-yongcha.jpg" alt="Samten Yongcha Monastery" loading="lazy">
                <div class="circuit-place-name">Samten Yongcha Monastery</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/aalo.jpg" alt="Aalo" loading="lazy">
                <div class="circuit-place-name">Aalo (Along)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/pasighat.jpg" alt="Pasighat" loading="lazy">
                <div class="circuit-place-name">Pasighat</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Offbeat%20Mechuka%20Adventure%20(6N/7D)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 4. Eastern Sunrise & Golden Pagoda (4 Nights / 5 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4 Nights / 5 Days</span>
                <h4 class="circuit-title">Eastern Sunrise &amp; Golden Pagoda</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Dibrugarh &#10132; Namsai (Golden Pagoda) &#10132; Roing / Mayodia Pass &#10132; Parasuram Kund / Dong Valley &#10132; Dibrugarh</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/arunachal/golden-pagoda.jpg" alt="Golden Pagoda Namsai" loading="lazy">
                <div class="circuit-place-name">Golden Pagoda (Namsai)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/roing.jpg" alt="Roing" loading="lazy">
                <div class="circuit-place-name">Roing</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/mayodia-pass.jpg" alt="Mayodia Pass" loading="lazy">
                <div class="circuit-place-name">Mayodia Pass</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/parasuram-kund.jpg" alt="Parasuram Kund" loading="lazy">
                <div class="circuit-place-name">Parasuram Kund</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/dong-valley.jpg" alt="Dong Valley" loading="lazy">
                <div class="circuit-place-name">Dong Valley</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/arunachal/namsai.jpg" alt="Namsai" loading="lazy">
                <div class="circuit-place-name">Namsai</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Eastern%20Sunrise%20%26%20Golden%20Pagoda%20(4N/5D)%20cab%20tour." target="_blank" class="circuit-btn-book">
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
    
    # Find the old Arunachal Pradesh section (lines 319-334)
    # Pattern: <!-- Arunachal Pradesh --> ... until next <!-- state -->
    old_pattern = r'      <!-- Arunachal Pradesh -->.*?</div>\s*</div>\s*</div>'
    
    match = re.search(old_pattern, content, re.DOTALL)
    if match:
        old_section = match.group(0)
        print(f"Found old Arunachal section ({len(old_section)} chars)")
        print(f"Preview: {old_section[:200]}...")
        
        # Replace old section with new 4-circuit section
        new_content = content.replace(old_section, ARUNACHAL_HTML)
        
        with open(DEST_FILE, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"\nSuccessfully replaced Arunachal Pradesh section!")
        print(f"Old length: {len(content)} chars")
        print(f"New length: {len(new_content)} chars")
        print(f"Added: {len(new_content) - len(content)} chars")
    else:
        print("ERROR: Could not find old Arunachal Pradesh section!")
        print("Searching for 'Arunachal' in file...")
        for i, line in enumerate(content.split('\n'), 1):
            if 'arunachal' in line.lower():
                print(f"  Line {i}: {line.strip()[:100]}")

if __name__ == "__main__":
    main()
