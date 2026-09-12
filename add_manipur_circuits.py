"""
Generate Manipur 4-circuit HTML and replace the old Manipur section in destinations.html.
Uses the same CSS classes as Meghalaya, Arunachal, Assam, and Nagaland circuits.
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

MANIPUR_HTML = '''      <!-- Manipur Destination Showcase: 4 Core Circuits -->
      <div class="state-section" id="manipur" style="margin-bottom: 5rem; opacity: 1 !important; transform: none !important;">
        <div class="state-header" style="margin-bottom: 2rem;">
          <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 1rem;">
            <div>
              <span class="hero-badge" style="margin-bottom: 0.5rem; display: inline-block;">&#10022; GT TRAVELS MANIPUR PACKAGES</span>
              <h3 style="color: var(--primary); font-size: 2.3rem; margin-bottom: 0.5rem;">Manipur <span style="color: var(--secondary); font-size: 1.25rem; font-family: var(--font-body); font-weight: 500;">&mdash; Jewel of India</span></h3>
              <p style="max-width: 780px; font-size: 1.05rem; color: #475569;">Book sanitized cabs and complete sightseeing packages across Manipur with GT Travels Shillong. Explore the world\'s only floating national park on Loktak Lake, the historic citadel of Kangla Fort, the rare Shirui Lily of Ukhrul, and the bustling Indo-Myanmar border at Moreh.</p>
            </div>
            <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels,%20I%20want%20to%20customize%20a%20Manipur%20cab%20tour" target="_blank" class="btn btn-primary" style="white-space: nowrap;"><i class="fab fa-whatsapp"></i> Custom Itinerary</a>
          </div>
        </div>

        <div class="circuits-container">

          <!-- 1. Loktak Lake, Floating Park & Moirang Circuit (1-2 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 1-2 Days Tour</span>
                <h4 class="circuit-title">Loktak Lake, Floating Park &amp; Moirang Circuit</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Imphal &#10132; Sendra Island &#10132; Keibul Lamjao (Sangai Deer) &#10132; INA Memorial Moirang &#10132; Loktak Boating &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/manipur/loktak-lake.jpg" alt="Loktak Lake" loading="lazy">
                <div class="circuit-place-name">Loktak Lake (Phumdis)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/keibul-lamjao.jpg" alt="Keibul Lamjao National Park" loading="lazy">
                <div class="circuit-place-name">Keibul Lamjao Park</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/sangai-deer.jpg" alt="Sangai Deer" loading="lazy">
                <div class="circuit-place-name">Sangai Deer</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/sendra-island.jpg" alt="Sendra Island" loading="lazy">
                <div class="circuit-place-name">Sendra Island</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/ina-memorial.jpg" alt="INA Memorial Moirang" loading="lazy">
                <div class="circuit-place-name">INA Memorial (Moirang)</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Loktak%20Lake,%20Floating%20Park%20%26%20Moirang%20Circuit%20(1-2%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 2. Imphal Heritage & Cultural City Tour (1-2 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 1-2 Days Tour</span>
                <h4 class="circuit-title">Imphal Heritage &amp; Cultural City Tour</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Kangla Fort &#10132; Ima Keithel &#10132; Shree Govindajee Temple &#10132; War Cemetery &#10132; State Museum &#10132; Singda Dam</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/manipur/kangla-fort.jpg" alt="Kangla Fort" loading="lazy">
                <div class="circuit-place-name">Kangla Fort</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/ima-keithel.jpg" alt="Ima Keithel Mothers Market" loading="lazy">
                <div class="circuit-place-name">Ima Keithel (Mother\'s Market)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/govindajee-temple.jpg" alt="Shree Govindajee Temple" loading="lazy">
                <div class="circuit-place-name">Govindajee Temple</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/imphal-war-cemetery.jpg" alt="Imphal War Cemetery" loading="lazy">
                <div class="circuit-place-name">Imphal War Cemetery</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/state-museum.jpg" alt="Manipur State Museum" loading="lazy">
                <div class="circuit-place-name">State Museum</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/singda-dam.jpg" alt="Singda Dam" loading="lazy">
                <div class="circuit-place-name">Singda Dam</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Imphal%20Heritage%20%26%20Cultural%20City%20Tour%20(1-2%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 3. Ukhrul & Shirui Lily Highland Expedition (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Expedition</span>
                <h4 class="circuit-title">Ukhrul &amp; Shirui Lily Highland Expedition</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Imphal &#10132; Ukhrul Town &#10132; Shirui Kashong Peak &#10132; Khangkhui Caves &#10132; Hundung &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/manipur/shirui-hills.jpg" alt="Shirui Kashong Peak" loading="lazy">
                <div class="circuit-place-name">Shirui Hills</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/shirui-lily.jpg" alt="Shirui Lily" loading="lazy">
                <div class="circuit-place-name">Shirui Lily</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/khangkhui-caves.jpg" alt="Khangkhui Caves" loading="lazy">
                <div class="circuit-place-name">Khangkhui Caves</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/ukhrul.jpg" alt="Ukhrul Town" loading="lazy">
                <div class="circuit-place-name">Ukhrul Town</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Ukhrul%20%26%20Shirui%20Lily%20Highland%20Expedition%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
                  <i class="fab fa-whatsapp"></i> Book This Cab Tour
                </a>
                <a href="tel:+919612946960" class="circuit-btn-call">
                  <i class="fas fa-phone"></i> Call 96129 46960
                </a>
              </div>
            </div>
          </div>

          <!-- 4. Border Trade & Historical Trail (2-3 Days) -->
          <div class="circuit-card">
            <div class="circuit-header">
              <div>
                <span class="circuit-duration-badge"><i class="far fa-clock"></i> 2-3 Days Tour</span>
                <h4 class="circuit-title">Border Trade &amp; Historical Trail</h4>
                <div class="circuit-route">
                  <i class="fas fa-route"></i>
                  <span>Imphal &#10132; Thoubal (Khongjom War Memorial) &#10132; Tengnoupal &#10132; Moreh (Indo-Myanmar Border) &#10132; Andro Heritage Village &#10132; Return</span>
                </div>
              </div>
            </div>

            <div class="circuit-places-label"><i class="fas fa-camera"></i> Attractions Covered (Exact Places with Photos):</div>
            <div class="circuit-places-grid">
              <div class="circuit-place-item">
                <img src="images/manipur/moreh-border.jpg" alt="Moreh Border Town" loading="lazy">
                <div class="circuit-place-name">Moreh (Myanmar Border)</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/khongjom-memorial.jpg" alt="Khongjom War Memorial" loading="lazy">
                <div class="circuit-place-name">Khongjom Memorial</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/andro-village.jpg" alt="Andro Heritage Village" loading="lazy">
                <div class="circuit-place-name">Andro Heritage Village</div>
              </div>
              <div class="circuit-place-item">
                <img src="images/manipur/thoubal.jpg" alt="Thoubal" loading="lazy">
                <div class="circuit-place-name">Thoubal</div>
              </div>
            </div>

            <div class="circuit-footer">
              <div class="circuit-fleet-info">
                <i class="fas fa-car-side"></i>
                <span>Cars: <strong>Swift Dzire / Baleno / Fronx / Etios</strong> (4 Seater) &bull; <strong>Innova / Crysta / Ertiga / XL6</strong> (7 Seater)</span>
              </div>
              <div class="circuit-actions">
                <a href="https://wa.me/919612946960?text=Hi%20GT%20Travels!%20I%20want%20to%20book%20the%20Border%20Trade%20%26%20Historical%20Trail%20(2-3%20Days)%20cab%20tour." target="_blank" class="circuit-btn-book">
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

    start_marker = "      <!-- Manipur -->"
    end_marker = "      <!-- Mizoram -->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1:
        print("ERROR: Could not find <!-- Manipur --> marker!")
        return
    if end_idx == -1:
        print("ERROR: Could not find <!-- Mizoram --> marker!")
        return

    old_section = content[start_idx:end_idx]
    print(f"Found old Manipur section ({len(old_section)} chars)")
    print(f"  From char {start_idx} to {end_idx}")

    new_content = content[:start_idx] + MANIPUR_HTML + "\n\n" + content[end_idx:]

    with open(DEST_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"\nSuccessfully replaced Manipur section!")
    print(f"Old length: {len(content)} chars")
    print(f"New length: {len(new_content)} chars")
    print(f"Added: {len(new_content) - len(content)} chars")


if __name__ == "__main__":
    main()
