"""
Generate Tripura 4-circuit HTML and replace the old Tripura section in destinations.html.
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

TRIPURA_HTML = '''      <!-- Tripura Destination Showcase: 4 Core Circuits -->
      <div class="state-section" id="tripura" style="margin-bottom: 5rem; opacity: 1 !important; transform: none !important;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">&#10022; GT TRAVELS TRIPURA PACKAGES</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Tripura <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">&mdash; Land of Fourteen Gods &amp; Water Palaces</span></h3>
              <p style="max-width: 780px; font-size: 1.05rem; color: #475569;">Book sanitized cabs and complete sightseeing packages across Tripura with GT Travels Shillong. Explore the grand white Ujjayanta Palace, the floating castle of Neermahal on Rudrasagar Lake, the colossal rock carvings of Unakoti, and the lush orange groves of Jampui Hills.</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20customize%20a%20Tripura%20cab%20tour" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Itinerary</a>
          </div>
        </div>

        <div class="circuits-container">

          <!-- 1. Royal Palaces, Lake Castles & Wildlife (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Royal Palaces, Lake Castles &amp; Wildlife</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Agartala (Ujjayanta Palace &amp; Heritage Park) &#10132; Sepahijala Sanctuary &#10132; Neermahal (Rudrasagar Lake Palace) &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/tripura/ujjayanta-palace.jpg" alt="Ujjayanta Palace" loading="lazy">
                <div class="circuit-place-name">Ujjayanta Palace</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/neermahal.jpg" alt="Neermahal Water Palace" loading="lazy">
                <div class="circuit-place-name">Neermahal Palace</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/rudrasagar-lake.jpg" alt="Rudrasagar Lake" loading="lazy">
                <div class="circuit-place-name">Rudrasagar Lake</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/sepahijala.jpg" alt="Sepahijala Sanctuary" loading="lazy">
                <div class="circuit-place-name">Sepahijala Sanctuary</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/heritage-park.jpg" alt="Heritage Park Agartala" loading="lazy">
                <div class="circuit-place-name">Heritage Park</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Royal%20Palaces,%20Lake%20Castles%20%26%20Wildlife%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 2. Sacred Temples & River Canyon Adventure (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Sacred Temples &amp; River Canyon Adventure</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Agartala &#10132; Udaipur (Tripura Sundari Matabari &amp; Kalyan Sagar) &#10132; Chabimura River Boat Safari (Rock Idols) &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/tripura/tripura-sundari.jpg" alt="Tripura Sundari Temple" loading="lazy">
                <div class="circuit-place-name">Tripura Sundari (Matabari)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/chabimura.jpg" alt="Chabimura Rock Carvings" loading="lazy">
                <div class="circuit-place-name">Chabimura (River Canyon)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/kalyan-sagar.jpg" alt="Kalyan Sagar Lake" loading="lazy">
                <div class="circuit-place-name">Kalyan Sagar</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/udaipur-tripura.jpg" alt="Udaipur City of Lakes" loading="lazy">
                <div class="circuit-place-name">Udaipur (City of Lakes)</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Sacred%20Temples%20%26%20River%20Canyon%20Adventure%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 3. Ancient Unakoti & Jampui Hills Expedition (3-4 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 3-4 Days Expedition</span>
                <h4 class="circuit-title">Ancient Unakoti &amp; Jampui Hills Expedition</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Agartala &#10132; Unakoti Rock-Cut Reliefs &#10132; Jampui Hills (Orange Valleys &amp; Sunrise Peak) &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/tripura/unakoti.jpg" alt="Unakoti Rock-Cut Carvings" loading="lazy">
                <div class="circuit-place-name">Unakoti (Shiva Reliefs)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/jampui-hills.jpg" alt="Jampui Hills" loading="lazy">
                <div class="circuit-place-name">Jampui Hills</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/agartala.jpg" alt="Agartala City" loading="lazy">
                <div class="circuit-place-name">Agartala City</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Ancient%20Unakoti%20%26%20Jampui%20Hills%20Expedition%20(3-4%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 4. Archaeological & Lake Island Discovery (3-4 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 3-4 Days Tour</span>
                <h4 class="circuit-title">Archaeological &amp; Lake Island Discovery</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Agartala &#10132; Pilak Buddhist Heritage &#10132; Trishna Bison Sanctuary &#10132; Dumboor Lake &amp; Narkel Kunja &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/tripura/dumboor-lake.jpg" alt="Dumboor Lake & Narkel Kunja" loading="lazy">
                <div class="circuit-place-name">Dumboor Lake (Narkel Kunja)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/pilak.jpg" alt="Pilak Buddhist Site" loading="lazy">
                <div class="circuit-place-name">Pilak (Buddhist Heritage)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/tripura/trishna-sanctuary.jpg" alt="Trishna Wildlife Sanctuary" loading="lazy">
                <div class="circuit-place-name">Trishna Wildlife Sanctuary</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Archaeological%20%26%20Lake%20Island%20Discovery%20(3-4%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
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

    start_marker = "      <!-- Tripura -->"
    end_marker = "    </div>\n  </section>"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print("ERROR: Could not find <!-- Tripura --> marker!")
        return
    if end_idx == -1:
        print("ERROR: Could not find </div>\\n  </section> marker!")
        return

    old_section = content[start_idx:end_idx]
    print(f"Found old Tripura section ({len(old_section)} chars)")
    print(f"  From char {start_idx} to {end_idx}")

    new_content = content[:start_idx] + TRIPURA_HTML + "\n\n" + content[end_idx:]

    with open(DEST_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSuccessfully replaced Tripura section!")
    print(f"Old length: {len(content)} chars")
    print(f"New length: {len(new_content)} chars")
    print(f"Added: {len(new_content) - len(content)} chars")


if __name__ == "__main__":
    main()
