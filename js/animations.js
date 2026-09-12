/* ============================================
   WANDERLUST TRAVELS — Scroll Animations
   Intersection Observer based scroll-triggered animations
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  // ─── Scroll-triggered Animations ───
  const animateElements = document.querySelectorAll('.animate-on-scroll');
  
  if (animateElements.length === 0) return;
  
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -80px 0px',
    threshold: 0.15
  };
  
  const animationObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animated');
        animationObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  animateElements.forEach(el => {
    animationObserver.observe(el);
  });
  
  // ─── Parallax Effect for Hero ───
  const heroSection = document.querySelector('.hero-bg img');
  if (heroSection) {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const rate = scrolled * 0.3;
      heroSection.style.transform = `translateY(${rate}px) scale(1.1)`;
    });
  }
  
  // ─── Parallax for Page Hero ───
  const pageHeroBg = document.querySelector('.page-hero .hero-bg img');
  if (pageHeroBg) {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      const rate = scrolled * 0.2;
      pageHeroBg.style.transform = `translateY(${rate}px)`;
    });
  }
  
  // ─── Text Reveal Animation ───
  const revealTexts = document.querySelectorAll('.reveal-text');
  revealTexts.forEach(text => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animation = 'fadeInUp 0.8s ease forwards';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    
    observer.observe(text);
  });
  
  // ─── Stagger Animation for Grid Children ───
  const staggerContainers = document.querySelectorAll('.stagger-children');
  
  staggerContainers.forEach(container => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const children = entry.target.children;
          Array.from(children).forEach((child, index) => {
            setTimeout(() => {
              child.classList.add('animated');
            }, index * 100);
          });
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    
    observer.observe(container);
  });
  
  // ─── Number Counter with Easing ───
  const counterElements = document.querySelectorAll('[data-count]');
  
  counterElements.forEach(counter => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !counter.dataset.counted) {
          counter.dataset.counted = 'true';
          const target = parseInt(counter.dataset.count);
          const suffix = counter.dataset.suffix || '';
          const prefix = counter.dataset.prefix || '';
          const duration = 2500;
          const startTime = performance.now();
          
          function easeOutExpo(t) {
            return t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
          }
          
          function updateCount(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easedProgress = easeOutExpo(progress);
            const current = Math.floor(easedProgress * target);
            
            counter.textContent = prefix + current.toLocaleString() + suffix;
            
            if (progress < 1) {
              requestAnimationFrame(updateCount);
            } else {
              counter.textContent = prefix + target.toLocaleString() + suffix;
            }
          }
          
          requestAnimationFrame(updateCount);
          observer.unobserve(counter);
        }
      });
    }, { threshold: 0.5 });
    
    observer.observe(counter);
  });
  
  // ─── Tilt Effect for Cards ───
  const tiltCards = document.querySelectorAll('.destination-card');
  
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = (y - centerY) / 20;
      const rotateY = (centerX - x) / 20;
      
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
    });
    
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
  });
  
  // ─── Image Lazy Loading ───
  const lazyImages = document.querySelectorAll('img[data-src]');
  
  if (lazyImages.length > 0) {
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      });
    }, { rootMargin: '100px' });
    
    lazyImages.forEach(img => imageObserver.observe(img));
  }
});
