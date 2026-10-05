/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        navy: { 50:'#e8edf5', 100:'#c5d0e6', 200:'#9fb3d4', 300:'#7996c3', 400:'#5c81b6', 500:'#3f6ca9', 600:'#3660a2', 700:'#2b5199', 800:'#214290', 900:'#0B2545' },
        royal: { 500:'#0077B6', 600:'#134074' },
        gold: { 400:'#D4A373', 500:'#EE9B00', 600:'#CA6702' }
      },
      fontFamily: {
        heading: ['Montserrat', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
        honor: ['Cinzel', 'serif']
      }
    }
  },
  plugins: [],
}
