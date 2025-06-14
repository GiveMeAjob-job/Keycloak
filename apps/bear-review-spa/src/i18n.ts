import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import HttpBackend from 'i18next-http-backend';

const urlLang = new URLSearchParams(window.location.search).get('lang') || undefined;

void i18n
  .use(HttpBackend)
  .use(initReactI18next)
  .init({
    lng: urlLang,
    fallbackLng: 'en',
    ns: ['common'],
    defaultNS: 'common',
    interpolation: { escapeValue: false },
    backend: {
      loadPath: '/locales/{{lng}}/{{ns}}.json'
    }
  });

export default i18n;
