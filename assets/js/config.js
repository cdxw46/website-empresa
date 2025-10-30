// Configuración de WhatsApp y textos
// Cambia este número por el tuyo en formato internacional sin espacios ni guiones.
// Ejemplo: "5215512345678" para México; "34600123456" para España.
const WHATSAPP_NUMBER = "34647089399"; // Número de WhatsApp real

// Mensaje base que se añade al iniciar el chat
const WHATSAPP_BASE_MESSAGE = "Hola, quiero comprar en Arbrep";

// Control de acceso por edad
const AGE_GATE_KEY = "arbrep_age_verified";

// Exportar a window para uso simple en HTML
window.ErosConfig = {
  WHATSAPP_NUMBER,
  WHATSAPP_BASE_MESSAGE,
  AGE_GATE_KEY,
};
