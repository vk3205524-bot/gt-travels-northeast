"""
Rebuild destinations.html cleanly with all 7 states (Meghalaya, Sikkim, Arunachal, Assam, Nagaland, Manipur, Mizoram, Tripura).
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

# Let's read the current file and find the first occurrence of each section up to Tripura
with open(DEST_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# The clean state sections up to Mizoram end:
mizoram_marker = '<!-- Mizoram Destination Showcase: 4 Core Circuits -->'
miz_idx = content.find(mizoram_marker)

# Find the end of Mizoram circuits container (the closing </div>\n      </div> for state-section)
# Looking after miz_idx for the old Tripura or next state section
old_tripura_marker = '      <!-- Tripura -->'
trip_idx = content.find(old_tripura_marker)

if trip_idx == -1:
    # Look for id="tripura"
    trip_idx = content.find('<div class="state-section" id="tripura"')

print(f"Mizoram at {miz_idx}, Tripura at {trip_idx}")

# The HTML from start of file up to Tripura
base_content = content[:trip_idx]

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

CLOSING_HTML = '''    </div>
  </section>

  <!-- CTA Section -->
  <section class="section animate-on-scroll" style="background-color: var(--primary); color: white; text-align: center;">
    <div class="container">
      <h2 style="color: white; margin-bottom: 1rem;">Not sure where to go? Let our NE experts help!</h2>
      <p style="margin-bottom: 2rem; font-size: 1.1rem; opacity: 0.9;">We curate personalized itineraries based on your interests, travel style, and budget.</p>
      <a href="contact.html" class="btn" style="background-color: var(--secondary); color: var(--primary);">Contact an Expert</a>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand"><a href="index.html" class="nav-logo"><img src="images/logo.png" alt="GT Travels" class="nav-logo-img" style="height: 52px; max-height: 52px; width: auto; max-width: 160px; object-fit: contain; display: block; margin-bottom: 1rem;"></a>
          <p>Creating unforgettable travel experiences across India since 2015. Your trusted partner for personalized journeys, cultural immersion, and adventure.</p>
          <div class="footer-social">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-twitter"></i></a>
            <a href="#"><i class="fab fa-youtube"></i></a>
          </div>
        </div>
        <div class="footer-column">
          <h4>Quick Links</h4>
          <ul>
            <li><a href="destinations.html">Destinations</a></li>
            <li><a href="packages.html">Tour Packages</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="blog.html">Travel Blog</a></li>
            <li><a href="contact.html">Contact Us</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Top Destinations</h4>
          <ul>
            <li><a href="packages.html">Meghalaya</a></li>
            <li><a href="packages.html">Sikkim</a></li>
            <li><a href="packages.html">Arunachal Pradesh</a></li>
            <li><a href="packages.html">Assam</a></li>
            <li><a href="packages.html">Nagaland</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h4>Contact Info</h4>
          <ul class="footer-contact">
            <li><i class="fas fa-map-marker-alt"></i><span>Jail Road, Near Subash Chandra Bose,<br>Shillong, Meghalaya 793001</span></li>
            <li><i class="fas fa-phone"></i><span>+91 96129 46960</span></li>
            <li><i class="fas fa-envelope"></i><span>gttravels12345@gmail.com</span></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2024 GT Travels. All Rights Reserved.</p>
        <p>Made with <i class="fas fa-heart" style="color: var(--secondary);"></i> in India</p>
      </div>
    </div>
  </footer>

  <!-- WhatsApp Float -->
  <div class="whatsapp-float">
    <div class="whatsapp-pulse"></div>
    <a href="https://wa.me/919612946960?text=Hi! I'm interested in your tour packages." target="_blank">
      <i class="fab fa-whatsapp"></i>
      <span>Chat with us</span>
    </a>
  </div>

  <!-- Scroll to Top -->
  <div class="scroll-top" onclick="scrollToTop()">
    <i class="fas fa-arrow-up"></i>
  </div>

  <!-- Page Loader -->
  <div class="page-loader">
    <div class="loader-spinner"></div>
  </div>

  <script src="js/main.js"></script>
  <script src="js/animations.js"></script>
  <script src="js/forms.js"></script>
</body>
</html>
'''

final_content = base_content + TRIPURA_HTML + "\n\n" + CLOSING_HTML

with open(DEST_FILE, "w", encoding="utf-8") as f:
    f.write(final_content)

print("Rebuilt destinations.html successfully!")
print(f"Total characters: {len(final_content)}")
