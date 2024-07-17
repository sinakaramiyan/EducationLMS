/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html'
  ],
  theme: {
    screens: {
      'sm': {'max': '601px'},

      'md': {'max': '1280px'},

      'lg': {'max': '1920px'},
    },
  },
  plugins: [],
}