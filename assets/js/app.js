// Utilidades
function buildWhatsAppUrl(number, text) {
  const message = encodeURIComponent(text);
  return `https://wa.me/${number}?text=${message}`;
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
}

// WhatsApp links en tarjetas de producto
function setupProductWhatsAppLinks() {
  document.querySelectorAll('.whatsapp-link').forEach((el) => {
    const product = el.getAttribute('data-product') || 'Producto';
    const text = `${window.ErosConfig.WHATSAPP_BASE_MESSAGE}: ${product}`;
    el.href = buildWhatsAppUrl(window.ErosConfig.WHATSAPP_NUMBER, text);
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
