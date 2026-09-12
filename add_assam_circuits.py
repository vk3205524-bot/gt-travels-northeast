"""
Generate Assam 4-circuit HTML and replace the old Assam section in destinations.html.
Uses the same CSS classes as Meghalaya and Arunachal circuits.
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

ASSAM_HTML = '''      <!-- Assam Destination Showcase: 4 Core Circuits -->
      <div class="state-section" id="assam" style="margin-bottom: 5rem; opacity: 1 !important; transform: none !important;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">&#10022; GT TRAVELS ASSAM PACKAGES</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Assam <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">&mdash; Gateway to the Northeast</span></h3>
              <p style="max-width: 780px; font-size: 1.05rem; color: #475569;">Book sanitized cabs and complete sightseeing packages across Assam with GT Travels Shillong. Explore our 4 most popular circuits &mdash; from Kaziranga safaris to Majuli heritage and Haflong hills &mdash; with verified local drivers and 4-seater or 7-seater fleet options.</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20customize%20an%20Assam%20cab%20tour" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Itinerary</a>
          </div>
        </div>

        <div class="circuits-container">

          <!-- 1. Kaziranga & Wildlife Safari (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Safari</span>
                <h4 class="circuit-title">Kaziranga &amp; Wildlife Safari</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Guwahati &#10132; Pobitora &#10132; Kaziranga (Jeep &amp; Elephant Safari) &#10132; Nameri &#10132; Guwahati</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/assam/kaziranga.jpg" alt="Kaziranga National Park" loading="lazy">
                <div class="circuit-place-name">Kaziranga National Park</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/pobitora.jpg" alt="Pobitora Wildlife Sanctuary" loading="lazy">
                <div class="circuit-place-name">Pobitora Sanctuary</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/manas.jpg" alt="Manas National Park" loading="lazy">
                <div class="circuit-place-name">Manas National Park</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/nameri.jpg" alt="Nameri National Park" loading="lazy">
                <div class="circuit-place-name">Nameri National Park</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/dibru-saikhowa.jpg" alt="Dibru-Saikhowa National Park" loading="lazy">
                <div class="circuit-place-name">Dibru-Saikhowa</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Kaziranga%20%26%20Wildlife%20Safari%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 2. Guwahati & Spiritual Heritage (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Guwahati &amp; Spiritual Heritage</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Guwahati (Kamakhya + Umananda + Brahmaputra Cruise) &#10132; Hajo &#10132; Sualkuchi &#10132; Tezpur &#10132; Guwahati</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/assam/kamakhya.jpg" alt="Kamakhya Temple" loading="lazy">
                <div class="circuit-place-name">Kamakhya Temple</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/umananda.jpg" alt="Umananda Island" loading="lazy">
                <div class="circuit-place-name">Umananda Island</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/brahmaputra.jpg" alt="Brahmaputra River Cruise" loading="lazy">
                <div class="circuit-place-name">Brahmaputra Cruise</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/hajo.jpg" alt="Hajo Pilgrimage" loading="lazy">
                <div class="circuit-place-name">Hajo</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/sualkuchi.jpg" alt="Sualkuchi Silk Village" loading="lazy">
                <div class="circuit-place-name">Sualkuchi (Silk Village)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/tezpur.jpg" alt="Tezpur" loading="lazy">
                <div class="circuit-place-name">Tezpur</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/guwahati.jpg" alt="Guwahati City" loading="lazy">
                <div class="circuit-place-name">Guwahati City</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Guwahati%20%26%20Spiritual%20Heritage%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 3. Majuli, Ahom Dynasty & Tea Trail (4-5 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 4-5 Days Tour</span>
                <h4 class="circuit-title">Majuli, Ahom Dynasty &amp; Tea Trail</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Jorhat &#10132; Majuli Island (2 Nights) &#10132; Sivasagar (Rang Ghar) &#10132; Charaideo Moidams &#10132; Dibrugarh (Tea Gardens) &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/assam/majuli.jpg" alt="Majuli Island" loading="lazy">
                <div class="circuit-place-name">Majuli Island</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/rang-ghar.jpg" alt="Rang Ghar Sivasagar" loading="lazy">
                <div class="circuit-place-name">Rang Ghar (Sivasagar)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/charaideo.jpg" alt="Charaideo Moidams UNESCO" loading="lazy">
                <div class="circuit-place-name">Charaideo Moidams</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/dibrugarh.jpg" alt="Dibrugarh Tea Gardens" loading="lazy">
                <div class="circuit-place-name">Dibrugarh (Tea City)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/jorhat.jpg" alt="Jorhat" loading="lazy">
                <div class="circuit-place-name">Jorhat</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/silchar.jpg" alt="Silchar" loading="lazy">
                <div class="circuit-place-name">Silchar</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Majuli%20Ahom%20Dynasty%20%26%20Tea%20Trail%20(4-5%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 4. Offbeat Hills & Dima Hasao (3-4 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 3-4 Days Adventure</span>
                <h4 class="circuit-title">Offbeat Hills &amp; Dima Hasao</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Guwahati &#10132; Haflong (Hill Station) &#10132; Umrangso (Kopili Gorge) &#10132; Dima Hasao &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/assam/haflong.jpg" alt="Haflong Hill Station" loading="lazy">
                <div class="circuit-place-name">Haflong</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/umrangso.jpg" alt="Umrangso" loading="lazy">
                <div class="circuit-place-name">Umrangso</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/assam/dima-hasao.jpg" alt="Dima Hasao" loading="lazy">
                <div class="circuit-place-name">Dima Hasao</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Offbeat%20Hills%20%26%20Dima%20Hasao%20(3-4%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
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

    # Find the old Assam section
    # It starts with <!-- Assam --> and ends before <!-- Nagaland -->
    start_marker = "      <!-- Assam -->"
    end_marker = "      <!-- Nagaland -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print("ERROR: Could not find <!-- Assam --> marker!")
        return
    if end_idx == -1:
        print("ERROR: Could not find <!-- Nagaland --> marker!")
        return

    old_section = content[start_idx:end_idx]
    print(f"Found old Assam section ({len(old_section)} chars)")
    print(f"  From char {start_idx} to {end_idx}")
    print(f"  Preview: {old_section[:150]}...")

    # Replace
    new_content = content[:start_idx] + ASSAM_HTML + "\n\n" + content[end_idx:]

    with open(DEST_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSuccessfully replaced Assam section!")
    print(f"Old length: {len(content)} chars")
    print(f"New length: {len(new_content)} chars")
    print(f"Added: {len(new_content) - len(content)} chars")


if __name__ == "__main__":
    main()
