"""
Trim the duplicated second half and cleanly close destinations.html.
"""

DEST_FILE = r"c:\Users\vk320\Downloads\tourism\destinations.html"

with open(DEST_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# First tripura is at pos 81920
# Second meghalaya is at pos 94368
# So let's cut right before pos 94368 (find the end of the tripura circuits container)
first_half = content[:94368]

# Find the last </div>\n      </div> inside first_half
# Which is the closing tags for the tripura state section
last_state_div = first_half.rfind('        </div>\n      </div>')
tripura_section_end = last_state_div + len('        </div>\n      </div>')

clean_content = first_half[:tripura_section_end] + "\n\n" + '''    </div>
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

with open(DEST_FILE, "w", encoding="utf-8") as f:
    f.write(clean_content)

print(f"Fixed destinations.html perfectly! Total length: {len(clean_content)}")
