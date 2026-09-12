/* ============================================
   GT TRAVELS — Form Submission Handler
   Sends form data to Google Sheets via Apps Script
   ============================================ */

// ⚠️ IMPORTANT: Replace this URL with your Google Apps Script Web App URL
// Follow the setup guide to get your URL
const GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbzDAkIPC1b8wTMR8WOxAr5PdBFJFFyH145vaQdOMvvsQyT8-77a9GbrYbzIXGUFMClr7A/exec';

// ─── Toast Notification ───
function showToast(message, type = 'success') {
  // Remove existing toast
  const existing = document.querySelector('.toast-notification');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = 'toast-notification';
  toast.innerHTML = `
    <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
    <span>${message}</span>
  `;
  toast.style.cssText = `
    position: fixed; bottom: 2rem; left: 50%; transform: translateX(-50%) translateY(100px);
    background: ${type === 'success' ? '#2ecc71' : '#e74c3c'}; color: white;
    padding: 1rem 2rem; border-radius: 12px; font-family: 'Poppins', sans-serif;
    font-size: 0.95rem; font-weight: 500; display: flex; align-items: center; gap: 0.75rem;
    box-shadow: 0 8px 30px rgba(0,0,0,0.2); z-index: 99999;
    transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  `;

  document.body.appendChild(toast);

  // Animate in
  requestAnimationFrame(() => {
    toast.style.transform = 'translateX(-50%) translateY(0)';
  });

  // Auto remove after 4 seconds
  setTimeout(() => {
    toast.style.transform = 'translateX(-50%) translateY(100px)';
    setTimeout(() => toast.remove(), 400);
  }, 4000);
}

// ─── Submit Data to Google Sheets ───
async function submitToGoogleSheets(data, formType) {
  // Add metadata
  data.formType = formType;
  data.timestamp = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });
  data.page = window.location.pathname;

  try {
    const response = await fetch(GOOGLE_SCRIPT_URL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    return true;
  } catch (error) {
    console.error('Form submission error:', error);
    return false;
  }
}

// ─── Get form field value helper ───
function getFieldValue(form, selector) {
  const el = form.querySelector(selector);
  return el ? el.value.trim() : '';
}

// ─── Multi-Step Inquiry Form (Contact Page) ───
document.addEventListener('DOMContentLoaded', () => {

  // Handle the multi-step form submit button
  const multiStepSubmitBtn = document.querySelector('.multi-step-form .btn-lg[onclick]');
  if (multiStepSubmitBtn) {
    // Remove the inline onclick
    multiStepSubmitBtn.removeAttribute('onclick');

    multiStepSubmitBtn.addEventListener('click', async (e) => {
      e.preventDefault();

      const form = document.querySelector('.multi-step-form');
      const selects = form.querySelectorAll('select');
      const inputs = form.querySelectorAll('input');
      const textareas = form.querySelectorAll('textarea');

      const data = {
        destination: selects[0] ? selects[0].value : '',
        tripType: selects[1] ? selects[1].value : '',
        budget: selects[2] ? selects[2].value : '',
        startDate: inputs[0] ? inputs[0].value : '',
        endDate: inputs[1] ? inputs[1].value : '',
        adults: selects[3] ? selects[3].value : '',
        children: selects[4] ? selects[4].value : '',
        accommodation: selects[5] ? selects[5].value : '',
        specialRequirements: textareas[0] ? textareas[0].value : '',
        fullName: inputs[2] ? inputs[2].value : '',
        phone: inputs[3] ? inputs[3].value : '',
        email: inputs[4] ? inputs[4].value : '',
        city: inputs[5] ? inputs[5].value : '',
        heardFrom: selects[6] ? selects[6].value : ''
      };

      // Disable button while submitting
      multiStepSubmitBtn.disabled = true;
      multiStepSubmitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';

      const success = await submitToGoogleSheets(data, 'Inquiry Form');

      if (success) {
        showToast('Thank you! 🎉 Your inquiry has been submitted. We\'ll contact you within 24 hours.');
        setTimeout(() => location.reload(), 2000);
      } else {
        showToast('Something went wrong. Please call us at +91 96129 46960', 'error');
        multiStepSubmitBtn.disabled = false;
        multiStepSubmitBtn.innerHTML = '<i class="fas fa-check"></i> Submit Inquiry';
      }
    });
  }

  // ─── Quick Contact Form ───
  const contactForm = document.querySelector('#contact-form');
  if (contactForm) {
    // Remove any existing listeners set by main.js
    const newForm = contactForm.cloneNode(true);
    contactForm.parentNode.replaceChild(newForm, contactForm);

    newForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const inputs = newForm.querySelectorAll('input');
      const textarea = newForm.querySelector('textarea');

      const data = {
        fullName: inputs[0] ? inputs[0].value : '',
        email: inputs[1] ? inputs[1].value : '',
        message: textarea ? textarea.value : ''
      };

      const submitBtn = newForm.querySelector('button[type="submit"]');
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

      const success = await submitToGoogleSheets(data, 'Quick Message');

      if (success) {
        showToast('Message sent! ✉️ We\'ll reply within 24 hours.');
        newForm.reset();
      } else {
        showToast('Failed to send. Please email us at gttravels12345@gmail.com', 'error');
      }

      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Send Message';
    });
  }

  // ─── Sidebar Inquiry Form (Package Detail Page) ───
  const sidebarForm = document.querySelector('.sidebar-inquiry form');
  if (sidebarForm) {
    sidebarForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const inputs = sidebarForm.querySelectorAll('input');
      const selects = sidebarForm.querySelectorAll('select');
      const textarea = sidebarForm.querySelector('textarea');

      const data = {
        fullName: inputs[0] ? inputs[0].value : '',
        email: inputs[1] ? inputs[1].value : '',
        phone: inputs[2] ? inputs[2].value : '',
        travelDate: inputs[3] ? inputs[3].value : '',
        travelers: selects[0] ? selects[0].value : '',
        message: textarea ? textarea.value : '',
        package: document.querySelector('.page-hero-content h1') ?
                 document.querySelector('.page-hero-content h1').textContent : 'Unknown Package'
      };

      const submitBtn = sidebarForm.querySelector('button[type="submit"]');
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';

      const success = await submitToGoogleSheets(data, 'Package Inquiry');

      if (success) {
        showToast('Inquiry sent! 🎉 Our team will contact you shortly.');
        sidebarForm.reset();
      } else {
        showToast('Failed to send. Please call +91 96129 46960', 'error');
      }

      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Send Inquiry';
    });
  }

  // ─── Newsletter Form ───
  const newsletterForm = document.querySelector('.newsletter-form');
  if (newsletterForm) {
    // Remove existing listener from main.js
    const newNewsletter = newsletterForm.cloneNode(true);
    newsletterForm.parentNode.replaceChild(newNewsletter, newsletterForm);

    newNewsletter.addEventListener('submit', async (e) => {
      e.preventDefault();

      const input = newNewsletter.querySelector('input');
      if (!input || !input.value.trim()) return;

      const data = {
        email: input.value.trim()
      };

      const success = await submitToGoogleSheets(data, 'Newsletter');

      if (success) {
        showToast('Subscribed! 🎉 You\'ll receive our best NE travel deals.');
        input.value = '';
      } else {
        showToast('Failed to subscribe. Please try again.', 'error');
      }
    });
  }
});
