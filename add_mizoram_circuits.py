"""
Generate Mizoram 4-circuit HTML and replace the old Mizoram section in destinations.html.
Uses the same CSS classes as Meghalaya, Arunachal, Assam, Nagaland, and Manipur circuits.
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

MIZORAM_HTML = '''      <!-- Mizoram Destination Showcase: 4 Core Circuits -->
      <div class="state-section" id="mizoram" style="margin-bottom: 5rem; opacity: 1 !important; transform: none !important;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">&#10022; GT TRAVELS MIZORAM PACKAGES</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Mizoram <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">&mdash; Land of the Hill People &amp; Blue Mountains</span></h3>
              <p style="max-width: 780px; font-size: 1.05rem; color: #475569;">Book sanitized cabs and complete sightseeing packages across Mizoram with GT Travels Shillong. Explore the grand Solomon\'s Temple in Aizawl, the breathtaking Vantawng and Tuirihiau waterfalls, the mystic heart-shaped Rih Dil lake, and the highest peak Phawngpui (Blue Mountain).</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20customize%20a%20Mizoram%20cab%20tour" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Itinerary</a>
          </div>
        </div>

        <div class="circuits-container">

          <!-- 1. Aizawl & Highlands Discovery (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Aizawl &amp; Highlands Discovery</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Aizawl (Solomon\'s Temple &amp; State Museum) &#10132; Reiek Peak &amp; Heritage Village &#10132; Hmuifang Tlang &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/mizoram/solomons-temple.jpg" alt="Solomon's Temple" loading="lazy">
                <div class="circuit-place-name">Solomon\'s Temple</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/reiek-peak.jpg" alt="Reiek Peak" loading="lazy">
                <div class="circuit-place-name">Reiek Peak</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/hmuifang.jpg" alt="Hmuifang Tlang" loading="lazy">
                <div class="circuit-place-name">Hmuifang Tlang</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/aizawl-city.jpg" alt="Aizawl City View" loading="lazy">
                <div class="circuit-place-name">Aizawl City View</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/falkawn-village.jpg" alt="Falkawn Heritage Village" loading="lazy">
                <div class="circuit-place-name">Falkawn Village</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Aizawl%20%26%20Highlands%20Discovery%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 2. Thenzawl Waterfalls & Handloom Circuit (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Thenzawl Waterfalls &amp; Handloom Circuit</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Aizawl &#10132; Thenzawl Golf Resort &#10132; Vantawng Falls &#10132; Tuirihiau Waterfall (Walk Behind) &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/mizoram/vantawng-falls.jpg" alt="Vantawng Falls" loading="lazy">
                <div class="circuit-place-name">Vantawng Falls</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/tuirihiau-falls.jpg" alt="Tuirihiau Falls" loading="lazy">
                <div class="circuit-place-name">Tuirihiau Falls</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/thenzawl-golf.jpg" alt="Thenzawl Golf Resort" loading="lazy">
                <div class="circuit-place-name">Thenzawl Golf Resort</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/chawngchilhi-cave.jpg" alt="Chawngchilhi Cave" loading="lazy">
                <div class="circuit-place-name">Chawngchilhi Cave</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Thenzawl%20Waterfalls%20%26%20Handloom%20Circuit%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 3. Champhai, Rih Dil & Border Valley (4-5 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4-5 Days Tour</span>
                <h4 class="circuit-title">Champhai, Rih Dil &amp; Border Valley</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Aizawl &#10132; Champhai Valley &#10132; Rih Dil (Heart Lake) &#10132; Murlen National Park &#10132; Lianchhiari Tlang &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/mizoram/champhai-valley.jpg" alt="Champhai Valley" loading="lazy">
                <div class="circuit-place-name">Champhai Valley</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/rih-dil.jpg" alt="Rih Dil Heart Lake" loading="lazy">
                <div class="circuit-place-name">Rih Dil (Heart Lake)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/lianchhiari-tlang.jpg" alt="Lianchhiari Tlang" loading="lazy">
                <div class="circuit-place-name">Lianchhiari Tlang</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/murlen-park.jpg" alt="Murlen National Park" loading="lazy">
                <div class="circuit-place-name">Murlen National Park</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Champhai,%20Rih%20Dil%20%26%20Border%20Valley%20(4-5%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 4. Phawngpui Blue Mountain & Southern Adventure (4-5 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4-5 Days Adventure</span>
                <h4 class="circuit-title">Phawngpui Blue Mountain &amp; Southern Adventure</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Aizawl &#10132; Lunglei &#10132; Lawngtlai &#10132; Phawngpui National Park (Blue Mountain Trek) &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/mizoram/phawngpui-peak.jpg" alt="Phawngpui Peak Blue Mountain" loading="lazy">
                <div class="circuit-place-name">Phawngpui (Blue Mountain)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/lunglei.jpg" alt="Lunglei" loading="lazy">
                <div class="circuit-place-name">Lunglei</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/lawngtlai.jpg" alt="Lawngtlai" loading="lazy">
                <div class="circuit-place-name">Lawngtlai</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/mizoram/dampa-reserve.jpg" alt="Dampa Tiger Reserve" loading="lazy">
                <div class="circuit-place-name">Dampa Tiger Reserve</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Phawngpui%20Blue%20Mountain%20%26%20Southern%20Adventure%20(4-5%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
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

    start_marker = "      <!-- Mizoram -->"
    end_marker = "      <!-- Tripura -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print("ERROR: Could not find <!-- Mizoram --> marker!")
        return
    if end_idx == -1:
        print("ERROR: Could not find <!-- Tripura --> marker!")
        return

    old_section = content[start_idx:end_idx]
    print(f"Found old Mizoram section ({len(old_section)} chars)")
    print(f"  From char {start_idx} to {end_idx}")

    new_content = content[:start_idx] + MIZORAM_HTML + "\n\n" + content[end_idx:]

    with open(DEST_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSuccessfully replaced Mizoram section!")
    print(f"Old length: {len(content)} chars")
    print(f"New length: {len(new_content)} chars")
    print(f"Added: {len(new_content) - len(content)} chars")


if __name__ == "__main__":
    main()
