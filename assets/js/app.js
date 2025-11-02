// Utilidades
function buildWhatsAppUrl(number, text) {
  const message = encodeURIComponent(text);
  // Asegura formato internacional sin símbolos
  const clean = String(number).replace(/\D+/g, "");
  // Usamos api.whatsapp.com que funciona en más navegadores que wa.me
  return `https://api.whatsapp.com/send?phone=${clean}&text=${message}`;
}

function getYear() {
  return new Date().getFullYear();
}

function updateFooterYear() {
  const y = document.getElementById('year');
  if (y) y.textContent = getYear();
}

// Puerta de edad
function setupAgeGate() {
  const gate = document.querySelector('.age-gate');
  if (!gate) return;
  const verified = localStorage.getItem(window.ErosConfig.AGE_GATE_KEY) === 'true';
  if (verified) {
    gate.style.display = 'none';
    return;
  }
  const btn = document.getElementById('confirmAge');
  if (btn) {
    btn.addEventListener('click', () => {
      localStorage.setItem(window.ErosConfig.AGE_GATE_KEY, 'true');
      gate.style.display = 'none';
    });
  }
}

// WhatsApp CTA principal
function setupHeroWhatsApp() {
  const a = document.getElementById('whatsappHero');
  if (!a) return;
  a.href = buildWhatsAppUrl(
    window.ErosConfig.WHATSAPP_NUMBER,
    window.ErosConfig.WHATSAPP_BASE_MESSAGE
  );
  a.target = '_blank';
  a.rel = 'noopener noreferrer';
}

// WhatsApp links en tarjetas de producto
function setupProductWhatsAppLinks() {
  document.querySelectorAll('.whatsapp-link').forEach((el) => {
    const product = el.getAttribute('data-product') || 'Producto';
    const text = `${window.ErosConfig.WHATSAPP_BASE_MESSAGE}: ${product}`;
    el.href = buildWhatsAppUrl(window.ErosConfig.WHATSAPP_NUMBER, text);
    el.target = '_blank';
    el.rel = 'noopener noreferrer';
    // Fallback por si el entorno bloquea la navegación directa
    el.addEventListener('click', (e) => {
      if (!el.href || el.href === '#') {
        e.preventDefault();
        const url = buildWhatsAppUrl(window.ErosConfig.WHATSAPP_NUMBER, text);
        window.open(url, '_blank');
      }
    });
  });
}

// Página de contacto
function setupContactPage() {
  const display = document.getElementById('whatsappNumberDisplay');
  const link = document.getElementById('whatsappContactLink');
  if (display) display.textContent = `+${window.ErosConfig.WHATSAPP_NUMBER}`;
  if (link) {
    link.href = buildWhatsAppUrl(
      window.ErosConfig.WHATSAPP_NUMBER,
      window.ErosConfig.WHATSAPP_BASE_MESSAGE
    );
  }
}

document.addEventListener('DOMContentLoaded', () => {
  updateFooterYear();
  setupAgeGate();
  setupHeroWhatsApp();
  setupProductWhatsAppLinks();
  setupContactPage();
});
