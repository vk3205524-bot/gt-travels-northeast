/* ============================================
   WANDERLUST TRAVELS — Package Filter System
   Northeast India Focused
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  const packagesGrid = document.querySelector('.packages-grid');
  if (!packagesGrid) return;

  // ─── Package Data — Northeast India ───
  const packages = [
    {
      id: 1, title: 'Meghalaya Explorer',
      location: 'Shillong - Cherrapunji - Dawki',
      region: 'meghalaya', type: 'adventure', budget: 'mid',
      duration: '5-7', days: 6, rating: 4.9, reviews: 156,
      badge: 'Bestseller',
      desc: 'Discover living root bridges, crystal-clear Umngot River at Dawki, majestic waterfalls at Cherrapunji, and the Scotland of the East — Shillong.',
      img: 'images/meghalaya/double-decker.jpg'
    },
    {
      id: 2, title: 'Tawang Monastery Trail',
      location: 'Guwahati - Bhalukpong - Tawang',
      region: 'arunachal', type: 'cultural', budget: 'mid',
      duration: '7+', days: 8, rating: 4.8, reviews: 98,
      badge: 'Spiritual',
      desc: 'Visit India\'s largest Buddhist monastery in Tawang, drive through stunning Sela Pass, and explore the untouched beauty of Arunachal Pradesh.',
      img: 'images/arunachal/tawang-monastery-exterior.jpg'
    },
    {
      id: 3, title: 'Kaziranga Wildlife Safari',
      location: 'Guwahati - Kaziranga - Majuli',
      region: 'assam', type: 'wildlife', budget: 'mid',
      duration: '5-7', days: 5, rating: 4.7, reviews: 132,
      badge: 'Top Rated',
      desc: 'Spot the one-horned rhinoceros at Kaziranga National Park, visit the world\'s largest river island Majuli, and cruise on the mighty Brahmaputra.',
      img: 'images/assam/kaziranga-rhino-card.jpg'
    },
    {
      id: 4, title: 'Sikkim & Gangtok Delight',
      location: 'Gangtok - Pelling - Lachung - Nathula',
      region: 'sikkim', type: 'adventure', budget: 'mid',
      duration: '5-7', days: 7, rating: 4.8, reviews: 143,
      badge: 'Popular',
      desc: 'Witness sunrise over Kanchenjunga, visit Nathula Pass on the Indo-China border, explore monasteries, and soak in Sikkim\'s mountain magic.',
      img: 'images/sikkim/gurudongmar-lake.jpg'
    },
    {
      id: 5, title: 'Nagaland Hornbill Festival',
      location: 'Dimapur - Kohima - Khonoma',
      region: 'nagaland', type: 'cultural', budget: 'mid',
      duration: '5-7', days: 6, rating: 4.7, reviews: 67,
      badge: 'Unique',
      desc: 'Experience the Festival of Festivals — vibrant tribal dances, traditional Naga cuisine, warrior culture, and the green village of Khonoma.',
      img: 'images/nagaland/dzukou-valley.jpg'
    },
    {
      id: 6, title: 'Assam Tea Garden Retreat',
      location: 'Guwahati - Jorhat - Sivasagar - Majuli',
      region: 'assam', type: 'cultural', budget: 'budget',
      duration: '3-5', days: 5, rating: 4.6, reviews: 89,
      badge: '',
      desc: 'Walk through lush tea estates of Jorhat, explore Ahom dynasty ruins in Sivasagar, and experience the living culture of Majuli island.',
      img: 'images/assam/majuli.jpg'
    },
    {
      id: 7, title: 'Manipur — The Jewel of India',
      location: 'Imphal - Loktak Lake - Moirang',
      region: 'manipur', type: 'cultural', budget: 'budget',
      duration: '3-5', days: 4, rating: 4.5, reviews: 54,
      badge: '',
      desc: 'Discover the floating phumdis of Loktak Lake, visit the historic INA Memorial, and experience Manipuri classical dance and cuisine.',
      img: 'images/manipur/loktak-lake.jpg'
    },
    {
      id: 8, title: 'Complete Northeast Circuit',
      location: 'Assam - Meghalaya - Arunachal',
      region: 'meghalaya', type: 'adventure', budget: 'luxury',
      duration: '7+', days: 14, rating: 4.9, reviews: 78,
      badge: 'Premium',
      desc: 'The ultimate Northeast India experience — covering three states, from Kaziranga\'s wildlife to Meghalaya\'s waterfalls to Tawang\'s monasteries.',
      img: 'images/arunachal/sela-pass.jpg'
    },
    {
      id: 9, title: 'Ziro Valley & Tribal Trails',
      location: 'Itanagar - Ziro Valley - Daporijo',
      region: 'arunachal', type: 'cultural', budget: 'mid',
      duration: '5-7', days: 6, rating: 4.6, reviews: 45,
      badge: 'Offbeat',
      desc: 'Explore the UNESCO tentative site Ziro Valley, meet the Apatani tribe, attend the Ziro Music Festival, and trek through pristine forests.',
      img: 'images/arunachal/ziro-valley.jpg'
    },
    {
      id: 10, title: 'Mizoram Hidden Paradise',
      location: 'Aizawl - Reiek - Phawngpui',
      region: 'mizoram', type: 'adventure', budget: 'budget',
      duration: '3-5', days: 5, rating: 4.5, reviews: 38,
      badge: 'Hidden Gem',
      desc: 'Trek to the Blue Mountain (Phawngpui), experience Mizo culture and hospitality, and explore the charming hill city of Aizawl.',
      img: 'images/mizoram/tuirihiau-falls.jpg'
    },
    {
      id: 11, title: 'Tripura Heritage Circuit',
      location: 'Agartala - Ujjayanta - Neermahal - Unakoti',
      region: 'tripura', type: 'cultural', budget: 'budget',
      duration: '3-5', days: 4, rating: 4.4, reviews: 42,
      badge: '',
      desc: 'Visit the lake palace Neermahal, ancient rock carvings at Unakoti, the magnificent Ujjayanta Palace, and experience Bengali-Tripuri culture.',
      img: 'images/tripura/neermahal-lake.jpg'
    },
    {
      id: 12, title: 'Darjeeling & Sikkim Combo',
      location: 'Darjeeling - Gangtok - Ravangla - Pelling',
      region: 'sikkim', type: 'adventure', budget: 'luxury',
      duration: '7+', days: 9, rating: 4.8, reviews: 119,
      badge: 'Must Do',
      desc: 'Ride the iconic toy train, watch Tiger Hill sunrise, explore Buddhist monasteries in Sikkim, and camp under the Himalayan sky.',
      img: 'images/sikkim/yumthang-valley.jpg'
    }
  ];

  // ─── Render Package Card ───
  function renderPackageCard(pkg) {
    return `
      <div class="package-card animate-on-scroll" data-region="${pkg.region}" data-type="${pkg.type}" data-budget="${pkg.budget}" data-duration="${pkg.duration}">
        <div class="package-card-img">
          <img src="${pkg.img}" alt="${pkg.title}" loading="lazy">
          ${pkg.badge ? `<span class="package-card-badge">${pkg.badge}</span>` : ''}
          <div class="package-card-wishlist"><i class="far fa-heart"></i></div>
        </div>
        <div class="package-card-body">
          <div class="package-card-location">
            <i class="fas fa-map-marker-alt"></i> ${pkg.location}
          </div>
          <h3 class="package-card-title">${pkg.title}</h3>
          <p class="package-card-desc">${pkg.desc}</p>
          <div class="package-card-meta">
            <span><i class="far fa-clock"></i> ${pkg.days} Days</span>
            <span><i class="far fa-star"></i> ${pkg.rating}</span>
            <span><i class="far fa-user"></i> ${pkg.reviews} reviews</span>
          </div>
          <div class="package-card-footer">
            <div class="package-card-action">
              <span style="color: var(--secondary-dark); font-weight: 600; font-size: 0.88rem; display: flex; align-items: center; gap: 0.35rem;"><i class="fas fa-check-circle" style="color: #28a745;"></i> Guided Tour</span>
            </div>
            <a href="package-detail.html" class="btn btn-primary btn-sm">View Details</a>
          </div>
        </div>
      </div>
    `;
  }

  // ─── Render All Packages ───
  function renderPackages(filteredPackages) {
    if (filteredPackages.length === 0) {
      packagesGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 2rem;">
          <i class="fas fa-search" style="font-size: 3rem; color: var(--secondary); margin-bottom: 1rem;"></i>
          <h3>No packages found</h3>
          <p style="color: var(--text-light); margin-top: 0.5rem;">Try adjusting your filters to find more options.</p>
        </div>
      `;
      return;
    }

    packagesGrid.innerHTML = filteredPackages.map(renderPackageCard).join('');

    // Re-initialize wishlist buttons
    document.querySelectorAll('.package-card-wishlist').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        btn.classList.toggle('active');
        const icon = btn.querySelector('i');
        icon.classList.toggle('far');
        icon.classList.toggle('fas');
      });
    });

    // Re-initialize scroll animations
    const animateEls = packagesGrid.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animated');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });
    animateEls.forEach(el => observer.observe(el));
  }

  // ─── Filter Logic ───
  const filterTags = document.querySelectorAll('.filter-tag');
  const regionSelect = document.getElementById('filter-region');
  const budgetSelect = document.getElementById('filter-budget');
  const durationSelect = document.getElementById('filter-duration');
  const searchInput = document.getElementById('filter-search');
  const sortSelect = document.getElementById('filter-sort');
  const resultsCount = document.getElementById('results-count');

  let activeType = 'all';

  function applyFilters() {
    let filtered = [...packages];

    if (activeType !== 'all') {
      filtered = filtered.filter(p => p.type === activeType);
    }
    if (regionSelect && regionSelect.value) {
      filtered = filtered.filter(p => p.region === regionSelect.value);
    }
    if (budgetSelect && budgetSelect.value) {
      filtered = filtered.filter(p => p.budget === budgetSelect.value);
    }
    if (durationSelect && durationSelect.value) {
      filtered = filtered.filter(p => p.duration === durationSelect.value);
    }
    if (searchInput && searchInput.value.trim()) {
      const query = searchInput.value.toLowerCase().trim();
      filtered = filtered.filter(p =>
        p.title.toLowerCase().includes(query) ||
        p.location.toLowerCase().includes(query) ||
        p.desc.toLowerCase().includes(query)
      );
    }
    if (sortSelect) {
      switch (sortSelect.value) {
        case 'rating': filtered.sort((a, b) => b.rating - a.rating); break;
        case 'popular': filtered.sort((a, b) => b.reviews - a.reviews); break;
      }
    }
    if (resultsCount) {
      resultsCount.textContent = `${filtered.length} package${filtered.length !== 1 ? 's' : ''} found`;
    }
    renderPackages(filtered);
  }

  filterTags.forEach(tag => {
    tag.addEventListener('click', () => {
      filterTags.forEach(t => t.classList.remove('active'));
      tag.classList.add('active');
      activeType = tag.dataset.type || 'all';
      applyFilters();
    });
  });

  [regionSelect, budgetSelect, durationSelect, sortSelect].forEach(el => {
    if (el) el.addEventListener('change', applyFilters);
  });

  if (searchInput) {
    let debounceTimer;
    searchInput.addEventListener('input', () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(applyFilters, 300);
    });
  }

  renderPackages(packages);
});
