/* ============================================
   WANDERLUST TRAVELS — Main JavaScript
   ============================================ */

// ─── Page Loader ───
window.addEventListener('load', () => {
  const loader = document.querySelector('.page-loader');
  if (loader) {
    setTimeout(() => loader.classList.add('loaded'), 500);
    setTimeout(() => loader.style.display = 'none', 1000);
  }
});

// ─── Sticky Navbar ───
const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;
  
  if (currentScroll > 50) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
  
  lastScroll = currentScroll;
});

// ─── Mobile Menu ───
function toggleMobileMenu() {
  const mobileBtn = document.querySelector('.mobile-menu-btn');
  const mobileMenu = document.querySelector('.mobile-menu');
  
  mobileBtn.classList.toggle('active');
  mobileMenu.classList.toggle('active');
  document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
}

// Close mobile menu on link click
document.querySelectorAll('.mobile-menu a').forEach(link => {
  link.addEventListener('click', () => {
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    mobileBtn.classList.remove('active');
    mobileMenu.classList.remove('active');
    document.body.style.overflow = '';
  });
});

// ─── Scroll to Top ───
const scrollTopBtn = document.querySelector('.scroll-top');

window.addEventListener('scroll', () => {
  if (window.pageYOffset > 400) {
    scrollTopBtn.classList.add('visible');
  } else {
    scrollTopBtn.classList.remove('visible');
  }
});

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ─── Stats Counter Animation ───
function animateCounters() {
  const counters = document.querySelectorAll('.stat-number');
  
  counters.forEach(counter => {
    if (counter.dataset.animated) return;
    
    const target = parseInt(counter.getAttribute('data-target'));
    const suffix = counter.getAttribute('data-suffix') || '';
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;
    
    const updateCounter = () => {
      current += step;
      if (current < target) {
        counter.textContent = Math.ceil(current) + suffix;
        requestAnimationFrame(updateCounter);
      } else {
        counter.textContent = target + suffix;
        counter.dataset.animated = 'true';
      }
    };
    
    updateCounter();
  });
}

// Trigger counter animation when stats section is visible
const statsSection = document.querySelector('.stats-section');
if (statsSection) {
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounters();
        statsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  
  statsObserver.observe(statsSection);
}

// ─── Testimonial Carousel ───
class TestimonialCarousel {
  constructor() {
    this.track = document.querySelector('.testimonial-track');
    this.dots = document.querySelectorAll('.testimonial-dot');
    this.currentIndex = 0;
    this.totalSlides = document.querySelectorAll('.testimonial-card').length;
    this.autoplayInterval = null;
    
    if (!this.track || this.totalSlides === 0) return;
    
    this.init();
  }
  
  init() {
    this.dots.forEach((dot, index) => {
      dot.addEventListener('click', () => this.goTo(index));
    });
    
    this.startAutoplay();
    
    // Pause on hover
    this.track.addEventListener('mouseenter', () => this.stopAutoplay());
    this.track.addEventListener('mouseleave', () => this.startAutoplay());
  }
  
  goTo(index) {
    this.currentIndex = index;
    this.track.style.transform = `translateX(-${index * 100}%)`;
    
    this.dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
  }
  
  next() {
    const nextIndex = (this.currentIndex + 1) % this.totalSlides;
    this.goTo(nextIndex);
  }
  
  startAutoplay() {
    this.autoplayInterval = setInterval(() => this.next(), 5000);
  }
  
  stopAutoplay() {
    clearInterval(this.autoplayInterval);
  }
}

// Initialize testimonial carousel
document.addEventListener('DOMContentLoaded', () => {
  new TestimonialCarousel();
});

// ─── Gallery Lightbox ───
class Lightbox {
  constructor() {
    this.lightbox = document.querySelector('.lightbox');
    this.lightboxImg = this.lightbox ? this.lightbox.querySelector('img') : null;
    this.galleryItems = document.querySelectorAll('.gallery-item');
    this.currentIndex = 0;
    this.images = [];
    
    if (!this.lightbox || this.galleryItems.length === 0) return;
    
    this.init();
  }
  
  init() {
    this.galleryItems.forEach((item, index) => {
      const img = item.querySelector('img');
      this.images.push(img.src);
      
      item.addEventListener('click', () => this.open(index));
    });
    
    // Close button
    const closeBtn = this.lightbox.querySelector('.lightbox-close');
    if (closeBtn) closeBtn.addEventListener('click', () => this.close());
    
    // Navigation
    const prevBtn = this.lightbox.querySelector('.lightbox-prev');
    const nextBtn = this.lightbox.querySelector('.lightbox-next');
    if (prevBtn) prevBtn.addEventListener('click', () => this.prev());
    if (nextBtn) nextBtn.addEventListener('click', () => this.next());
    
    // Close on background click
    this.lightbox.addEventListener('click', (e) => {
      if (e.target === this.lightbox) this.close();
    });
    
    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (!this.lightbox.classList.contains('active')) return;
      if (e.key === 'Escape') this.close();
      if (e.key === 'ArrowLeft') this.prev();
      if (e.key === 'ArrowRight') this.next();
    });
  }
  
  open(index) {
    this.currentIndex = index;
    this.lightboxImg.src = this.images[index];
    this.lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
  
  close() {
    this.lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }
  
  prev() {
    this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    this.lightboxImg.src = this.images[this.currentIndex];
  }
  
  next() {
    this.currentIndex = (this.currentIndex + 1) % this.images.length;
    this.lightboxImg.src = this.images[this.currentIndex];
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new Lightbox();
});

// ─── FAQ Accordion ───
document.querySelectorAll('.faq-question').forEach(question => {
  question.addEventListener('click', () => {
    const faqItem = question.parentElement;
    const answer = faqItem.querySelector('.faq-answer');
    const isActive = faqItem.classList.contains('active');
    
    // Close all other FAQs
    document.querySelectorAll('.faq-item').forEach(item => {
      item.classList.remove('active');
      item.querySelector('.faq-answer').style.maxHeight = '0';
    });
    
    // Toggle current
    if (!isActive) {
      faqItem.classList.add('active');
      answer.style.maxHeight = answer.scrollHeight + 'px';
    }
  });
});

// ─── Wishlist Toggle ───
document.querySelectorAll('.package-card-wishlist').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    btn.classList.toggle('active');
    
    const icon = btn.querySelector('i');
    if (btn.classList.contains('active')) {
      icon.classList.remove('far');
      icon.classList.add('fas');
    } else {
      icon.classList.remove('fas');
      icon.classList.add('far');
    }
  });
});

// ─── Newsletter Form ───
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
  newsletterForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = newsletterForm.querySelector('input');
    if (input.value.trim()) {
      alert('Thank you for subscribing! 🎉 We\'ll send you the best travel deals.');
      input.value = '';
    }
  });
}

// ─── Hero Particles ───
function createParticles() {
  const particlesContainer = document.querySelector('.hero-particles');
  if (!particlesContainer) return;
  
  for (let i = 0; i < 20; i++) {
    const particle = document.createElement('div');
    particle.classList.add('hero-particle');
    particle.style.left = Math.random() * 100 + '%';
    particle.style.animationDelay = Math.random() * 8 + 's';
    particle.style.animationDuration = (Math.random() * 6 + 5) + 's';
    particle.style.width = (Math.random() * 4 + 2) + 'px';
    particle.style.height = particle.style.width;
    particlesContainer.appendChild(particle);
  }
}

document.addEventListener('DOMContentLoaded', createParticles);

// ─── Multi-step Form ───
class MultiStepForm {
  constructor(formElement) {
    this.form = formElement;
    if (!this.form) return;
    
    this.steps = this.form.querySelectorAll('.form-step');
    this.indicators = this.form.querySelectorAll('.step-indicator');
    this.currentStep = 0;
    
    this.init();
  }
  
  init() {
    this.form.querySelectorAll('.btn-next-step').forEach(btn => {
      btn.addEventListener('click', () => this.nextStep());
    });
    
    this.form.querySelectorAll('.btn-prev-step').forEach(btn => {
      btn.addEventListener('click', () => this.prevStep());
    });
  }
  
  nextStep() {
    if (this.currentStep < this.steps.length - 1) {
      this.steps[this.currentStep].classList.remove('active');
      this.indicators[this.currentStep].classList.remove('active');
      this.indicators[this.currentStep].classList.add('completed');
      
      this.currentStep++;
      
      this.steps[this.currentStep].classList.add('active');
      this.indicators[this.currentStep].classList.add('active');
    }
  }
  
  prevStep() {
    if (this.currentStep > 0) {
      this.steps[this.currentStep].classList.remove('active');
      this.indicators[this.currentStep].classList.remove('active');
      
      this.currentStep--;
      
      this.steps[this.currentStep].classList.add('active');
      this.indicators[this.currentStep].classList.remove('completed');
      this.indicators[this.currentStep].classList.add('active');
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const multiForm = document.querySelector('.multi-step-form');
  if (multiForm) new MultiStepForm(multiForm);
});

// ─── Contact Form Submission ───
const contactForm = document.querySelector('#contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Thank you for reaching out! 🙏 We\'ll get back to you within 24 hours.');
    contactForm.reset();
  });
}

// ─── Smooth Scroll for Anchor Links ───
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href');
    if (targetId === '#') return;
    
    e.preventDefault();
    const target = document.querySelector(targetId);
    if (target) {
      const navHeight = document.querySelector('.navbar').offsetHeight;
      const targetPosition = target.offsetTop - navHeight;
      window.scrollTo({ top: targetPosition, behavior: 'smooth' });
    }
  });
});

// ─── Active Nav Link ───
function setActiveNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

document.addEventListener('DOMContentLoaded', setActiveNav);

// ─── Meghalaya Tourist Attractions Filter & Search ───
window.filterMeghalaya = function(circuit, btn) {
  if (btn) {
    document.querySelectorAll('.meghalaya-pill').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
  }
  const activeBtn = document.querySelector('.meghalaya-pill.active');
  const currentCircuit = circuit || (activeBtn ? activeBtn.getAttribute('data-circuit') : 'all');
  const searchInput = document.getElementById('meghalayaSearch');
  const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
  
  const cards = document.querySelectorAll('.spot-card');
  let visibleCount = 0;
  cards.forEach(card => {
    const cardCircuit = card.getAttribute('data-circuit') || '';
    const text = (card.textContent || '').toLowerCase();
    const matchesCircuit = (currentCircuit === 'all' || cardCircuit === currentCircuit);
    const matchesQuery = (!query || text.includes(query));
    
    if (matchesCircuit && matchesQuery) {
      card.classList.remove('hidden');
      visibleCount++;
    } else {
      card.classList.add('hidden');
    }
  });
  
  const countDisplay = document.getElementById('spotCountDisplay');
  if (countDisplay) {
    countDisplay.textContent = `Showing ${visibleCount} places`;
  }
};

// ─── Ensure Hero Video Autoplay ───
document.addEventListener('DOMContentLoaded', () => {
  const heroVideo = document.querySelector('.hero-video');
  if (heroVideo) {
    heroVideo.muted = true;
    const playPromise = heroVideo.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        document.body.addEventListener('click', () => {
          heroVideo.play();
        }, { once: true });
      });
    }
  }
});

// ─── Handle URL Query Params on Destinations Page ───
document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const searchParam = urlParams.get('search');
  if (searchParam && typeof filterMeghalaya === 'function') {
    const searchInput = document.getElementById('meghalayaSearch');
    if (searchInput) {
      searchInput.value = searchParam;
      filterMeghalaya();
    }
  }
});


