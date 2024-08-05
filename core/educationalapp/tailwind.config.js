/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html'
  ],
  theme: {},
  plugins: [
    require("@xpd/tailwind-3dtransforms")
  ],
}